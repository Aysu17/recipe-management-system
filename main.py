from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import engine, get_db
from models import Base
from schemas import Recipe, RecipeCreate, RecipeUpdate
from services import RecipeService

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    return RecipeService.create_recipe(db=db, recipe=recipe)

@app.get("/recipes/", response_model=List[Recipe])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return RecipeService.get_recipes(db=db, skip=skip, limit=limit)

@app.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = RecipeService.get_recipe(db=db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@app.put("/recipes/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db)):
    db_recipe = RecipeService.update_recipe(db=db, recipe_id=recipe_id, recipe_data=recipe)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@app.delete("/recipes/{recipe_id}", response_model=Recipe)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = RecipeService.delete_recipe(db=db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe
