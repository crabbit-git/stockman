from db.run_sql import run_sql
from models.category import Category

def save(category):
    sql = "INSERT INTO categories (name) VALUES (%s) RETURNING id"
    category.id = run_sql(sql, [category.name])[0]['id']
    return category

def delete_all():
    run_sql("DELETE FROM categories")

def select_all():
    return [
        Category(
            record['name'],
            record['id']
        )
        for record in run_sql("SELECT * FROM categories ORDER BY name")
    ]

def select(id):
    query = run_sql("SELECT * FROM categories WHERE id = %s", [id])
    if len(query) == 1:
        record = query[0]
    return Category(
        record['name'],
        record['id']
    )

def update(category):
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
