from flask import request
from flask_restful import Resource
from Model import db, Ingredients, IngredientsSchema

categories_schema = IngredientsSchema(many=True)
category_schema = IngredientsSchema()

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        categories = categories_schema.dump(categories).data
        return {'status': 'success', 'data': categories}, 200