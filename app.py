import os
from typing import Any, Optional
from fastapi import FastAPI, File, Form, HTTPException, Response, Depends, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

mockTrees = [{
    "species":"Neem",
    "height":2.5,
    "note":"It's planted by the pole"
},
{
    "species":"Apple",
    "height":3,
    "note":"It's planted by the mobile shopee"
}
]
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
):
    print(f"Received tree: species={treeSpecies}, height={treeHeight}, notes={treeNotes}")
    return {
        "message": "Tree added",
        "species": treeSpecies,
        "height": treeHeight,
        "notes": treeNotes,
    }
