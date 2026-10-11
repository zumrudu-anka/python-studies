import xlrd

def read_excel_file(fileName, sheetName = "Sheet1", colNames = ["all"], is_float = False):

    workbook = xlrd.open_workbook(f'./data/{fileName}')
    sheet = workbook.sheet_by_name(sheetName)
    
    titles = sheet.row_values(0)
    values = []

    if len(colNames) == 1 and colNames[0] == "all":
        for rownum in range(1, sheet.nrows):
            value = {}
            for colNum in range(0, len(titles)):
                value[f"{titles[colNum]}"] = sheet.row_values(rownum)[colNum]
            values.append(value)
        return titles, values
    else:
        colIndexes = []
        for colName in colNames:
            colIndexes.append(titles.index(colName))
        for rownum in range(1, sheet.nrows):
            value = {}
            for colIndex in colIndexes:
                value[f"{titles[colIndex]}"] = sheet.row_values(rownum)[colIndex]
            values.append(value)
        return colNames, values

def read_excel_file_only_item_numbers(fileName, sheetName = "Sheet1", is_float = False):
    workbook = xlrd.open_workbook(f'./data/{fileName}')
    sheet = workbook.sheet_by_name(sheetName)
    
    titles = sheet.row_values(0)
    itemNumberColumn = titles.index("Item Number")
    itemNumbers = []
    for rownum in range(1, sheet.nrows):
        itemNumber = sheet.row_values(rownum)[itemNumberColumn]
        if is_float:
            itemNumber = str(int(itemNumber)) if isinstance(itemNumber, float) else str(itemNumber)
        itemNumbers.append(itemNumber)
    return itemNumbers