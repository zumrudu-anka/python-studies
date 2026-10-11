def write_dictionary_to_json(dictionary, output):
    """Write Dictionary to File

    Args:
        dictionary (dict): Dictionary to Write
        output (str): Output File Name
    """
    import json

    json.dump(dictionary, open(f"./data/{output}.json", 'w'), indent = 4)
    
def write_data_to_excel_file(titles, data, outputFileName, sheetName = "Sheet1"):
    """Write data to Excel File with Titles

    Args:
        titles (list): Titles
        data (list[dict]): Data as Dictionary List
        outputFileName (_type_): Output File Name
        sheetName (str, optional): Sheet Name. Defaults to "Sheet1".
    """
    import xlwt
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)
    
    style_string = "font: bold on;"
    style = xlwt.easyxf(style_string)

    for index, title in enumerate(titles):
        sheet.write(0, index, title, style = style)
    
    style_string = "font: bold off;"
    style = xlwt.easyxf(style_string)
    
    index = 1
    for datum in data:
        for datumIndex, key in enumerate(datum):
            sheet.write(index, datumIndex, datum[f"{key}"], style = style)
        index += 1

    workbook.save(f"./data/{outputFileName}.xls")