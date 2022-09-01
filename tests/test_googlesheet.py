import pandas as pd
from dotenv import load_dotenv
from propersandwich.googlesheet import read_worksheet, create_worksheet, delete_worksheet, update_worksheet

load_dotenv()

def test_read_worksheet():
    data = read_worksheet('TEST_SHEET','Test worksheet')
    assert len(data.index) == 3

def test_create_worksheet():
    worksheet_tab_name = 'random test worksheet'
    create_worksheet('TEST_SHEET',worksheet_tab_name)
    data = read_worksheet('TEST_SHEET',worksheet_tab_name)
    assert len(data.index) == 0
    delete_worksheet('TEST_SHEET',worksheet_tab_name)

def test_update_worksheet():
    worksheet_tab_name = 'random test worksheet'
    list_of_numbers = [10, 20, 30, 40, 50, 60]
    data = pd.DataFrame(list_of_numbers, columns=['Numbers'])
    update_worksheet('TEST_SHEET', worksheet_tab_name, data)
    data_from_updated_worksheet = read_worksheet('TEST_SHEET', worksheet_tab_name)
    assert len(data_from_updated_worksheet.index) == 6
    delete_worksheet('TEST_SHEET',worksheet_tab_name)
