from db.run_sql import run_sql
from models.product import Product
from repositories import manufacturer_repository

def save(product):
    sql = """
    INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING id
    """
    values = [
        product.name,
        product.description,
        product.quantity,
        product.cost,
        product.price,
        product.manufacturer.id
    ]
    product.id = run_sql(sql, values)[0]['id']
    return product

def delete_all():
    run_sql("DELETE FROM products")

def select_all():
    return [
        Product(
            record['name'],
            record['description'],
            record['quantity'],
            record['cost'],
            record['price'],
            manufacturer_repository.select(record['manufacturer_id']),
            record['id']
        )
        for record in run_sql("SELECT * FROM products ORDER BY manufacturer_id, id")
    ]

def select(id):
    query = run_sql("SELECT * FROM products WHERE id = %s", [id])[0]
    return Product(
        query['name'],
        query['description'],
        query['quantity'],
        query['cost'],
        query['price'],
        manufacturer_repository.select(query['manufacturer_id']),
        query['id']
    )
