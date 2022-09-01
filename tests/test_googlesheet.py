from dotenv import load_dotenv
from sandw1ch.googlesheet import read_worksheet, create_worksheet, delete_worksheet

load_dotenv()

def test_read_worksheet():
    data = read_worksheet('test_sheet','Test worksheet')
    assert len(data.index) == 3

def test_create_worksheet():
    worksheet_tab_name = 'random test worksheet'
    create_worksheet('test_sheet',worksheet_tab_name)
    data = read_worksheet('test_sheet',worksheet_tab_name)
    assert len(data.index) == 0
    delete_worksheet('test_sheet',worksheet_tab_name)
