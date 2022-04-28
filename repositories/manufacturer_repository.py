from db.run_sql import run_sql
from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = """
    INSERT INTO manufacturers (name, country)
    VALUES (%s, %s)
    RETURNING id
    """
    values = [
        manufacturer.name,
        manufacturer.country
    ]
    manufacturer.id = run_sql(sql, values)[0]['id']
    return manufacturer

def delete_all():
    run_sql("DELETE FROM manufacturers")

def select_all():
    return [
        Manufacturer(record['name'], record['country'], record['id'])
        for record in run_sql("SELECT * FROM manufacturers")
    ]

def select(id):
    query = run_sql("SELECT * FROM manufacturers WHERE id = %s", [id])[0]
    return Manufacturer(query['name'], query['country'], query['id'])
