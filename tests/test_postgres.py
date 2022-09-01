from propersandwich.postgres import query

def test_query():
    data = query('TEST', 'SELECT * from test')
    assert len(data) == 3
