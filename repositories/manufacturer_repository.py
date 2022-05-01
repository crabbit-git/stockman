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
        for record in run_sql("SELECT * FROM manufacturers ORDER BY id")
    ]

def select(id):
    query = run_sql("SELECT * FROM manufacturers WHERE id = %s", [id])
    if len(query) == 1:
        record = query[0]
    return Manufacturer(record['name'], record['country'], record['id'])

def update(manufacturer):
    sql = """
    UPDATE manufacturers
    SET (name, country) = (%s, %s)
    WHERE id = %s
    """
    values = [manufacturer.name, manufacturer.country, manufacturer.id]
    run_sql(sql, values)

def delete(id):
    run_sql(
        "DELETE FROM manufacturers WHERE id = %s",
        [id]
    )
