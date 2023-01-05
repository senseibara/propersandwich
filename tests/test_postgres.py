from propersandwich.postgres import query, destructive_write
import pandas as pd


def test_query():
    data = query('TEST', 'SELECT * from test_query')
    assert len(data) == 3

    row = data.loc[data['testcolumn2'] == 'Marc']
    assert row['testcolumn3'].at[row.index[0]] == 5


def test_destructive_write():
    data = pd.DataFrame({'testcolumn1': [1], 'testcolumn2': ['Business']})
    data = data.rename_axis('index', axis='index')
    assert destructive_write('TEST', 'test_destructive_write', data) == True

    data = query('TEST', 'SELECT * from test_destructive_write')
    assert len(data) == 1

    row = data.loc[data['testcolumn1'] == 1]
    assert row['testcolumn2'].at[row.index[0]] == 'Business'
