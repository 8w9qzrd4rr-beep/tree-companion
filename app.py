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

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()
app.mount("/script", StaticFiles(directory="script"), name="script")
app.mount("/css", StaticFiles(directory="css"), name="css")

@app.get("/")
async def root():
    return FileResponse("templates/index.html")

@app.get("/api/v1/trees")
async def get_trees():
    response = supabase.table("trees").select("*").execute()
    return {"data": response.data}

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
        "owner_id": 11
    }

    response = supabase.table("trees").insert(tree_data).execute()
    return {"message": "Done Posting", "tree": response.data[0]}