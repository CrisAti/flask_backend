from flask import Flask, request, jsonify
from flask_cors import CORS
from model import db, Product
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# Crear producto
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data.get('price', 0.0)  # ✅ por defecto 0.0 si no se envía
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

# Listar productos
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'price': p.price  # ✅ incluido
        }
        for p in products
    ])

# Obtener un producto por ID
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price  # ✅ incluido
    })

# Actualizar producto
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.description = data['description']
    product.price = data.get('price', product.price)  # ✅ mantiene precio si no se envía
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

# Eliminar producto
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
