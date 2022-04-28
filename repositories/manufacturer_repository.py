from db.run_sql import run_sql

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
