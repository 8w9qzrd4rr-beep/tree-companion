import os
from typing import Any, Optional
from fastapi import FastAPI, File, Form, HTTPException, Response, Depends, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import json
from mockdata import mockTrees, mockUsers #,mockAdopterGroup
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import date, datetime
import bcrypt
from fastapi import HTTPException
import secrets
import string

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()
app.mount("/script", StaticFiles(directory="script"), name="script")
app.mount("/css", StaticFiles(directory="css"), name="css")

@app.get("/")
async def root():
    return FileResponse("templates/login.html")

@app.get("/profile")
async def profile_page():
    return FileResponse("templates/profile.html")

@app.get("/history")
async def history_page():
    return FileResponse("templates/history.html")

@app.get("/dictionary")
async def dictionary_page():
    return FileResponse("templates/dictionary.html")

@app.get("/signup")
async def signup_page():
    return FileResponse("templates/signup.html")

@app.get("/signup/verify")
async def otp_page():
    return FileResponse("templates/otp.html")

@app.get("/signup/info")
async def info_page():
    return FileResponse("templates/details.html")

@app.get("/home")
async def home_page():
    return FileResponse("templates/index.html")

@app.get("/api/v1/trees")
async def get_trees():
    response = supabase.table("trees").select("*").execute()
    return {"data": response.data}

@app.post("/api/auth/signup")
async def signup_request(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)):

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    try:
        response = (
            supabase.table("users")
            .insert({
                "username": username,
                "email": email,
                "password_hash": password_hash,
            })
            .execute()
        )
    except Exception as e:
        print("SIGNUP ERROR:", repr(e))
        raise HTTPException(status_code=400, detail="Signup failed. Username or email may already be in use.")
    return {"message": "Signup successful"}

@app.post("/api/auth/verify-otp")
async def verify_otp(email : str = Form(...), 
                     code : int = Form(...)):
    code_data = None
    try:
        resp = supabase.table("otp_cache").select("code").eq("email", email).execute()
        if resp.data:
            code_data = resp.data[0]["code"]
            print(code)
        else:
            print("No matching record found for this email.")
    except Exception as e:
        print("No OTP was generated ERROR:", repr(e))
        raise HTTPException(status_code=400, detail="OTP generation Failed. Valid OTP does't exists.")

    if(code == code_data):
        return True
    else:
        return False

@app.post("/api/v1/add/trees")
async def add_tree(
    treeSpecies: str = Form(...),
    treeHeight: Optional[float] = Form(None),
    treeNotes: Optional[str] = Form(None),
    treeSpeciesUp: Optional[UploadFile] = File(None),
    treePhoto: Optional[UploadFile] = File(None),
    loc: str = Form(...),
):
    loc_dict = json.loads(loc)

    tree_data = {
        "species": treeSpecies,
        "description": treeNotes,
        "height": treeHeight,
        "diameter": None,
        "planting_date": date.today().isoformat(),
        "verified_bool": False,
        "last_activity": datetime.today().isoformat(),
        "status": "active",
        "latitude": loc_dict.get("latitude"),
        "longitude": loc_dict.get("longitude"),
        "address": loc_dict.get("address"),
        "owner_id": 7
    }

    response = supabase.table("trees").insert(tree_data).execute()
    return {"message": "Done Posting", "tree": response.data[0]}

@app.post('/api/auth/signup/otp')
async def otp_verify(
    email: str = Form(...),
):
    pin = "".join(secrets.choice(string.digits) for _ in range(6))
    print(pin)
    try:
        res = supabase.table("otp_cache").insert({"email" : email, "code" : pin}).execute()
    except Exception as e:
        print("OTPGen ERROR:", repr(e))
        raise HTTPException(status_code=400, detail="New OTP generation Failed. Valid OTP already exists.")
    return {"message": "OTP generation successful"}




