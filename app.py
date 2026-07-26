import os
from typing import Any, Optional
from fastapi import FastAPI, File, Form, HTTPException, Response, Depends, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import json

#50.505295, -104.662981

mockTrees = [
  {
    "species": "American Elm",
    "height": 12.5,
    "note": "Planted near the entrance of Wascana Park",
    "lat": 50.435012,
    "long": -104.615034
  },
  {
    "species": "Bur Oak",
    "height": 5.2,
    "note": "Next to the downtown public library",
    "lat": 50.448021,
    "long": -104.610011
  },
  {
    "species": "Manitoba Maple",
    "height": 8.0,
    "note": "Front yard of a brick house in Cathedral area",
    "lat": 50.452145,
    "long": -104.621458
  },
  {
    "species": "White Spruce",
    "height": 15.3,
    "note": "Behind the university campus buildings",
    "lat": 50.415099,
    "long": -104.590022
  },
  {
    "species": "Green Ash",
    "height": 4.1,
    "note": "Close to the transit stop",
    "lat": 50.470055,
    "long": -104.630045
  },
  {
    "species": "Paper Birch",
    "height": 7.2,
    "note": "Along the Devonian Pathway",
    "lat": 50.485012,
    "long": -104.670088
  },
  {
    "species": "Colorado Blue Spruce",
    "height": 10.0,
    "note": "Corner of a residential intersection in the north end",
    "lat": 50.510044,
    "long": -104.600077
  },
  {
    "species": "Cottonwood",
    "height": 20.5,
    "note": "Growing near Wascana Creek",
    "lat": 50.420088,
    "long": -104.750012
  },
  {
    "species": "Trembling Aspen",
    "height": 11.4,
    "note": "Bordering the eastern industrial park",
    "lat": 50.440023,
    "long": -104.450099
  },
  {
    "species": "Weeping Willow",
    "height": 6.8,
    "note": "By the neighborhood drainage pond",
    "lat": 50.530015,
    "long": -104.700055
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
