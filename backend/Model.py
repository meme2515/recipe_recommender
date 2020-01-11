from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, password, name, email):
        self.password = password
        self.name = name
        self.email = email


class FridgeInventory(db.Model):
    __tablename__ = 'fridge_inventory'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, user_id, ingredient_id):
        self.user_id = user_id
        self.ingredient_id = ingredient_id


class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    category = db.Column(db.String(250), nullable=False)
    img_file = db.Column(db.String(250), nullable=False)

    def __init__(self, name, category, img_file):
        self.name = name
        self.category = category
        self.img_file = img_file


class RecipeIngredients(db.Model):
    __tablename__ = 'recipe_ingredients'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id', ondelete='CASCADE'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, recipe_id, ingredient_id):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id


class Recipes(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_region = db.Column(db.String(100), nullable=False)
    category_portion = db.Column(db.String(100), nullable=False)
    img_file = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(10000), nullable=False)

    def __init__(self, name, category_region, category_portion, img_file, content):
        self.name = name
        self.category_region = category_region
        self.category_portion = category_portion
        self.img_file = img_file
        self.content = content


class UsersSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)
    creation_date = fields.DateTime


class FridgeInventorySchema(ma.Schema):
    id = fields.Integer()
    user_id = fields.Integer(required=True)
    ingredient_id = fields.Integer(required=True)


class IngredientsSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    category = fields.String(required=True)
    img_file = fields.String(required=True)


class RecipeIngredientsSchema(ma.Schema):
    id = fields.Integer()
    recipe_id = fields.Integer(required=True)
    ingredient_id = fields.Integer(required=True)


class RecipesSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    category_region = fields.String(required=True)
    category_portion = fields.String(required=True)
    img_file = fields.DateTime()
    content = fields.String(required=True)