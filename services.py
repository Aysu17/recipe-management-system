from sqlalchemy.orm import Session
from models import Recipe
from schemas import RecipeCreate, RecipeUpdate

class RecipeService:

    @staticmethod
    def create_recipe(db: Session, recipe: RecipeCreate):
        db_recipe = Recipe(
            name=recipe.name,
            description=recipe.description,
            ingredients=recipe.ingredients,
            instructions=recipe.instructions
        )
        db.add(db_recipe)
        db.commit()
        db.refresh(db_recipe)
        return db_recipe

    @staticmethod
    def get_recipes(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Recipe).offset(skip).limit(limit).all()

    @staticmethod
    def get_recipe(db: Session, recipe_id: int):
        return db.query(Recipe).filter(Recipe.id == recipe_id).first()

    @staticmethod
    def update_recipe(db: Session, recipe_id: int, recipe_data: RecipeUpdate):
        db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if db_recipe:
            db_recipe.name = recipe_data.name
            db_recipe.description = recipe_data.description
            db_recipe.ingredients = recipe_data.ingredients
            db_recipe.instructions = recipe_data.instructions
            db.commit()
            db.refresh(db_recipe)
            return db_recipe
        return None

    @staticmethod
    def delete_recipe(db: Session, recipe_id: int):
        db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
        if db_recipe:
            db.delete(db_recipe)
            db.commit()
            return db_recipe
        return None
