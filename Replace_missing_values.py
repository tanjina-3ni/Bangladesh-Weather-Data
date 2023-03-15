


import xlrd
import csv

# Load the Excel file
book = xlrd.open_workbook("Daily Sunshine Till Jun_2014.xls")
sheet = book.sheet_by_index(0)

# Loop through all cells in the sheet
for row_idx in range(sheet.nrows):
    for col_idx in range(sheet.ncols):
        # Check if the cell contains the string "****"
        if sheet.cell_value(row_idx, col_idx) == "****" or sheet.cell_value(row_idx, col_idx) == "*** *" or sheet.cell_value(row_idx, col_idx) == "***" or sheet.cell_value(row_idx, col_idx) == "**" or sheet.cell_value(row_idx, col_idx) == "":
            # Replace the string with the value 30.5
            sheet.put_cell(row_idx, col_idx, xlrd.XL_CELL_NUMBER, 6.4, None)

# Convert the modified Excel file to CSV
with open("Daily_Sunshine.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for row_idx in range(sheet.nrows):
        writer.writerow([sheet.cell_value(row_idx, col_idx) for col_idx in range(sheet.ncols)])
