from db.run_sql import run_sql

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
