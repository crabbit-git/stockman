from db.run_sql import run_sql
from models.category import Category

def save(category):
    '''
    Takes a Category object, turns it into key:value pairs, writes it into
    an SQL database record, then reads back the auto-generated SQL ID and
    writes it to the Python object, which it then returns for use in a
    confirmation message and for debugging purposes:
    '''
    sql = "INSERT INTO categories (name) VALUES (%s) RETURNING id"
    category.id = run_sql(sql, [category.name])[0]['id']
    return category

def select_all():
    '''
    Selects all category records in the database
    and returns them as a list of Python objects:
    '''
    return [
        Category(
            record['name'],
            record['id']
        )
        for record in run_sql("SELECT * FROM categories ORDER BY name")
    ]

def select(id):
    '''
    Selects a given category record by ID and, if the SQL query successfully
    returns a list containing only one record, returns all of its attributes
    by constructing a Category object in Python:
    '''
    query = run_sql("SELECT * FROM categories WHERE id = %s", [id])
    if len(query) == 1:
        record = query[0]
        return Category(
            record['name'],
            record['id']
    )

def update(category):
    '''
    Renames a given category in the database:
    '''
    run_sql(
        "UPDATE categories SET name = %s WHERE id = %s",
        [category.name, category.id]
    )

def delete(id):
    '''
    If there are no products from a given category in the database,
    deletes the category record by targeting its ID in the table,
    then returns its name for use in a confirmation message.
    Otherwise, returns None and leaves the database alone.
    '''
    if len(
        run_sql("SELECT FROM products WHERE category_id = %s", [id])
    ) == 0:
        return run_sql(
            "DELETE FROM categories WHERE id = %s RETURNING name",
            [id]
        )[0]['name']

def delete_all():
    '''
    Delete all categories. Mostly for debugging and testing purposes;
    intentionally unavailable to the user interface to avoid catastrophes.
    '''
    run_sql("DELETE FROM categories")
