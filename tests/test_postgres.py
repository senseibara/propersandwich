from propersandwich.postgres import query, replace_table, upsert, create_table, _get_postgres_type, delete_table
import pandas as pd


def test_postgres_functions():
    # Setup
    assert create_table('TEST', 'test_postgres_functions', {'testcolumn1': 'bigint', 'testcolumn 2': 'text'}) == True

    data = pd.DataFrame({'testcolumn1': [1], 'testcolumn 2': ['Business']})
    data = data.rename_axis('index', axis='index')
    assert replace_table('TEST', 'test_postgres_functions', data) == True

    # Test that the table has been replaced
    data = query('TEST', 'SELECT * from test_postgres_functions')
    assert len(data) == 1

    # Test that the values are the new ones
    row = data.loc[data['testcolumn1'] == 1]
    assert row['testcolumn 2'].at[row.index[0]] == 'Business'

    # Teardown
    assert delete_table('TEST', 'test_postgres_functions') == True


def test_upsert():
    delete_table('TEST', 'test_upsert')

    data = pd.DataFrame({'testcolumn1': [1], 'testcolumn 2': ['Business']})
    data = data.rename_axis('index', axis='index')
    assert upsert('TEST', 'test_upsert', data, 'testcolumn1') == True

    result = query('TEST', 'SELECT * from test_upsert')
    assert len(result) == 1
    assert result.query("testcolumn1 == 1")['testcolumn 2'].iloc[0] == 'Business'

    data = pd.DataFrame({'testcolumn1': [1, 2], 'testcolumn 2': ['Work', 'Trump']})
    data = data.rename_axis('index', axis='index')
    assert upsert('TEST', 'test_upsert', data, 'testcolumn1') == True

    result = query('TEST', 'SELECT * from test_upsert')
    assert len(result) == 2
    assert result.query("testcolumn1 == 1")['testcolumn 2'].iloc[0] == 'Work'
    assert result.query("testcolumn1 == 2")['testcolumn 2'].iloc[0] == 'Trump'

    # Teardown
    assert delete_table('TEST', 'test_upsert') == True


def test_get_postgres_type():
    assert _get_postgres_type('int64') == 'bigint'
    assert _get_postgres_type('float64') == 'double precision'
    assert _get_postgres_type('object') == 'text'
    assert _get_postgres_type('datetime64[ns]') == 'timestamp'
    assert _get_postgres_type('bool') == 'boolean'
