from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer
from models.category import Category
from repositories import manufacturer_repository, category_repository

def save(product):
    sql = """
    INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    RETURNING id
    """
    values = [
        product.name,
        product.category.id,
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

def select_all(filter = None):
    sort = "manufacturer_id, id"
    values = None
    if filter == None:
        condition = ""
    elif filter == 1:
        condition = "WHERE quantity > 0"
    elif filter == 0:
        condition = "WHERE quantity = 0"
    elif type(filter) is Manufacturer:
        condition = "WHERE manufacturer_id = %s"
        sort = "id"
        values = [filter.id]
    elif type(filter) is Category:
        condition = "WHERE category_id = %s"
        values = [filter.id]
    else:
        return []
    sql = f"SELECT * FROM products {condition} ORDER BY {sort}"
    return [
        Product(
            record['name'],
            category_repository.select(record['category_id']),
            record['description'],
            record['quantity'],
            record['cost'],
            record['price'],
            manufacturer_repository.select(record['manufacturer_id']),
            record['id']
        )
        for record in run_sql(sql, values)
    ]

def select(id):
    query = run_sql("SELECT * FROM products WHERE id = %s", [id])
    if len(query) == 1:
        record = query[0]
    return Product(
        record['name'],
        category_repository.select(record['category_id']),
        record['description'],
        record['quantity'],
        record['cost'],
        record['price'],
        manufacturer_repository.select(record['manufacturer_id']),
        record['id']
    )

def update(product):
    sql = """
    UPDATE products
    SET (name, description, quantity, cost, price, manufacturer_id) = (%s, %s, %s, %s, %s, %s)
    WHERE id = %s
    """
    values = [
        product.name,
        product.description,
        product.quantity,
        product.cost,
        product.price,
        product.manufacturer.id,
        product.id
    ]
    run_sql(sql, values)

def count(id, quantity):
    run_sql(
        "UPDATE products SET quantity = %s WHERE id = %s",
        [quantity, id]
    )

def delete(id):
    run_sql(
        "DELETE FROM products WHERE id = %s",
        [id]
    )
