from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer
from models.category import Category
from repositories import manufacturer_repository, category_repository

def save(product):
    '''
    Takes a Product object, turns it into key:value pairs, writes it into an
    SQL database record, then reads back the auto-generated SQL ID and writes
    it to the Python object, which it then returns for use in a confirmation
    message and for debugging purposes:
    '''
    sql = """
    INSERT INTO products (
        name, category_id, description, quantity, cost, price, manufacturer_id
    )
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

def select_all(filter = None):
    '''
    Select all products satisfying a given filter condition.
    If no filter is specified, it simply selects all products in the table.
    If the filter is passed the string "in stock", only products with a stock
    quantity of more than 0 will be returned.
    If passed "out of stock", only products with 0 stock are returned.
    If passed a Manufacturer object, it returns only their products,
    and if passed a Category object, it returns products from that category.
    '''
    sort = "manufacturer_id, id"
    values = None
    if filter == None:
        condition = ""
    elif filter == "in stock":
        condition = "WHERE quantity > 0"
    elif filter == "out of stock":
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
    '''
    Selects a given product record by ID and, if the SQL query successfully
    returns a list containing only one record, returns all of its attributes by
    constructing a Product object in Python:
    '''
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

def count(id, quantity):
    '''
    Updates only the quantity in stock for a given product, since this is the
    most frequently edited attribute for day-to-day use case:
    '''
    run_sql(
        "UPDATE products SET quantity = %s WHERE id = %s",
        [quantity, id]
    )

def update(product):
    '''
    Updates every attribute for a given product except for its in stock
    quantity and its SQL record ID:
    '''
    sql = """
    UPDATE products
    SET (
        name, description, quantity, cost, price, manufacturer_id
    ) = (
        %s, %s, %s, %s, %s, %s
    )
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

def delete(id):
    '''
    Deletes a given product record by targeting its ID in the table,
    then returns its name for use in a confirmation message:
    '''
    return run_sql(
        "DELETE FROM products WHERE id = %s RETURNING name",
        [id]
    )[0]['name']

def delete_all():
    '''
    Delete all products. Mostly for debugging and testing purposes;
    intentionally unavailable to the user interface to avoid catastrophes.
    '''
    run_sql("DELETE FROM products")
