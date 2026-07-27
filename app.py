import os
from typing import Any, Optional
from fastapi import FastAPI, File, Form, HTTPException, Response, Depends, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import json
from mockdata import mockTrees, mockUsers #,mockAdopterGroup
#50.505295, -104.662981

app = FastAPI()
app.mount("/script", StaticFiles(directory="script"), name="script")
app.mount("/css", StaticFiles(directory="css"), name="css")

@app.get("/")
async def root():
    return FileResponse("templates/index.html")

@app.get("/api/v1/trees")
async def get_trees():
    return {"data": mockTrees}

@app.post("/api/v1/add/trees")
async def add_tree(
    treeSpecies: str = Form(...),
    treeHeight: Optional[float] = Form(None),
    treeNotes: Optional[str] = Form(None),
    treeSpeciesUp: Optional[UploadFile] = File(None),
    treePhoto: Optional[UploadFile] = File(None),
    loc : str = Form(...)
):
    loc_dict = json.loads(loc)

    tree_data = {
        "treeSpecies": treeSpecies,
        "treeHeight": treeHeight,
        "treeNotes": treeNotes,
        "long": loc_dict.get("longitude"),
        "lat": loc_dict.get("latitude")
    }
    mockTrees.append(tree_data)
    return {"message": "Done Posting"}
