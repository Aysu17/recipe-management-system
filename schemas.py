from pydantic import BaseModel
from typing import List, Optional

class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: str
    instructions: str

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True
