from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calories.db'
db = SQLAlchemy(app)
api = Api(app, version='1.0', title='Calorie Calculator API', description='API for calculating calories')

# Модель для продукту
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories_per_100g = db.Column(db.Float, nullable=False)

# Модель для запиту на підрахунок калорій
calorie_request_model = api.model('CalorieRequest', {
    'product_id': fields.Integer(required=True, description='ID продукту'),
    'weight': fields.Float(required=True, description='Вага продукту в грамах')
})

# API для додавання продукту
@api.route('/products')
class ProductResource(Resource):
    def post(self):
        data = request.json
        new_product = Product(name=data['name'], calories_per_100g=data['calories_per_100g'])
        db.session.add(new_product)
        db.session.commit()
        return {'message': 'Product added successfully'}, 201

# API для підрахунку калорій
@api.route('/calculate')
class CalculateResource(Resource):
    @api.expect([calorie_request_model])
    def post(self):
        data = request.json
        total_calories = 0
        for item in data:
            product = Product.query.get(item['product_id'])
            if product:
                total_calories += (product.calories_per_100g * item['weight']) / 100
        return {'total_calories': total_calories}

# Створення бази даних всередині контексту додатку
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # API для видалення та оновлення продукту
    @api.route('/products/<int:id>')
    class ProductDetailResource(Resource):
        def delete(self, id):
            product = Product.query.get_or_404(id)
            db.session.delete(product)
            db.session.commit()
            return {'message': 'Product deleted successfully'}, 200

        def put(self, id):
            product = Product.query.get_or_404(id)
            data = request.json
            product.name = data.get('name', product.name)
            product.calories_per_100g = data.get('calories_per_100g', product.calories_per_100g)
            db.session.commit()
            return {'message': 'Product updated successfully'}, 200

    app.run(debug=True)
