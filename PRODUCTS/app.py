from flask import Flask, request, jsonify
from model import db, Product
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_prduct = Product(name=data['name'], description=data['description'])
    db.session.add(new_prduct)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@app.route('/products', methods=['GET'])
def get_products():
    prds = Product.query.all()
    return jsonify([{'id': prd.id, 'name': prd.name, 'description': prd.description} for prd in prds])

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    prd = Product.query.get_or_404(id)
    return jsonify({'id': prd.id, 'name': prd.name, 'description': prd.description})

@app.route('/products/<int:id>', methods=['PUT'])
def update_prd(id):
    data = request.get_json()
    prd = Product.query.get_or_404(id)
    prd.name = data['name']
    prd.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_prd(id):
    prd = Product.query.get_or_404(id)
    db.session.delete(prd)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
