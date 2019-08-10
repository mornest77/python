# %%
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'NTUB BOOK CLUB -bd78520cee37.json', scope)

gc = gspread.authorize(credentials)

worksheet = gc.open("Book Club Test").sheet1

# %%

val = worksheet.acell('A1').value
print(val)

# %%

values_list = worksheet.row_values(2)
# values_list = worksheet.col_values(1)
print(values_list)

# %%

list_of_lists = worksheet.get_all_values()
print(list_of_lists)

# %%

worksheet.update_acell('B1', 'B1')


# %%

cell_list = worksheet.range('A1:C7')

for cell in cell_list:
    cell.value = 'O_o'

# Update in batch
worksheet.update_cells(cell_list)

# %%

cell_list = worksheet.range('A1:C7')

for cell in cell_list:
    print(cell.__dict__)

# %%

cell_list = worksheet.range('A1:C7')


col_dict = {
    1: 'A',
    2: 'B',
    3: 'C'
}

for cell in cell_list:
    col = col_dict.get(cell._col)
    cell.value = f'{col}{cell._row}'

# Update in batch
worksheet.update_cells(cell_list)


# %%
# json_key = json.load(open('gspread_credentials.json'))
# scope = ['https://spreadsheets.google.com/feeds']

# credentials = SignedJwtAssertionCredentials(
#     json_key['client_email'],
#     json_key['private_key'],
#     scope)

# gc = gspread.authorize(credentials)
# ss = gc.open('Microbe-scope')


# %%
