from propersandwich.postgres import query, replace_table, _get_postgres_type
import pandas as pd


def test_query():
    data = query('TEST', 'SELECT * from test_query')
    assert len(data) == 3

    row = data.loc[data['testcolumn2'] == 'Marc']
    assert row['testcolumn3'].at[row.index[0]] == 5


def test_replace_table():
    data = pd.DataFrame({'testcolumn1': [1.6], 'testcolumn 2': ['Business']})
    data = data.rename_axis('index', axis='index')
    assert replace_table('TEST', 'test_replace_table', data) == True

    data = query('TEST', 'SELECT * from test_replace_table')
    assert len(data) == 1

    row = data.loc[data['testcolumn1'] == 1.6]
    assert row['testcolumn 2'].at[row.index[0]] == 'Business'


def test_get_postgres_type():
    assert _get_postgres_type('int64') == 'bigint'
    assert _get_postgres_type('float64') == 'double precision'
    assert _get_postgres_type('object') == 'text'
    assert _get_postgres_type('datetime64[ns]') == 'timestamp'
    assert _get_postgres_type('bool') == 'boolean'
