from sandw1ch.postgres import query

def test_query():
    data = query('test', 'SELECT * from test')
    assert len(data) == 3