from db.run_sql import run_sql
from models.manufacturer import Manufacturer

def save(manufacturer):
    '''
    Takes a Manufacturer object, turns it into key:value pairs, writes it into
    an SQL database record, then reads back the auto-generated SQL ID and
    writes it to the Python object, which it then returns for use in a
    confirmation message and for debugging purposes:
    '''
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

def select_all():
    '''
    Selects all manufacturer records in the database
    and returns them as a list of Python objects:
    '''
    return [
        Manufacturer(record['name'], record['country'], record['id'])
        for record in run_sql("SELECT * FROM manufacturers ORDER BY id")
    ]

def select(id):
    '''
    Selects a given manufacturer record by ID and, if the SQL query
    successfully returns a list containing only one record, returns all of its
    attributes by constructing a Manufacturer object in Python:
    '''
    query = run_sql("SELECT * FROM manufacturers WHERE id = %s", [id])
    if len(query) == 1:
        record = query[0]
    return Manufacturer(record['name'], record['country'], record['id'])

def update(manufacturer):
    '''
    Updates all of a given manufacturer's attributes in the database:
    '''
    sql = "UPDATE manufacturers SET (name, country) = (%s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.country, manufacturer.id]
    run_sql(sql, values)

def delete(id):
    '''
    If there are no products by a given manufacturer in the database,
    deletes the manufacturer record by targeting its ID in the table,
    then returns its name for use in a confirmation message.
    Otherwise, returns None and leaves the database alone.
    '''
    if len(
        run_sql("SELECT FROM products WHERE manufacturer_id = %s", [id])
    ) == 0:
        return run_sql(
            "DELETE FROM manufacturers WHERE id = %s RETURNING name",
            [id]
        )[0]['name']

def delete_all():
    '''
    Delete all manufacturers. Mostly for debugging and testing purposes;
    intentionally unavailable to the user interface to avoid catastrophes.
    '''
    run_sql("DELETE FROM manufacturers")
