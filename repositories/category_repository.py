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
