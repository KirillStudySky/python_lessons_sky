from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://qa:skyqa@139.100.217.192:5432/x_clients"


def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[1] == 'employee'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 =rows[-1]

    assert row1["id"] == 154
    assert row1["name"] == "SQL School"

# "select * from company where id = XXX"
def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 105).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "Autotest"

def test_select_1_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"is_active\" = :is_active and id >= :id")

    my_params ={
        'id': 150,
        'is_active': True
    }
    rows = db.execute(sql_statement, my_params).fetchall()
    # rows = db.execute(sql_statement, id = 150, is_active = True).fetchall()

    assert len(rows) == 3

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("INSERT INTO company(\"name\") VALUES (:new_name)")
    rows = db.execute(sql, new_name = 'SkyPro')

def test_update():
    db = create_engine(db_connection_string)
    sql = text("UPDATE company SET description = :descr WHERE id = :id")
    db.execute(sql, descr = 'New descr', id = 156)

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    db.execute(sql, id=153)






