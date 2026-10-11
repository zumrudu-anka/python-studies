from modules.fileReader import read_excel_file, read_excel_file_only_item_numbers
from modules.fileWriter import write_data_to_excel_file

def deleteDataFromGKNToTebosan(deletedDataRefs, data):
    newDeletedData = []

    for datum in data:
        for key, value in datum.items():
            if key == "Item Number":
                if value in deletedDataRefs:
                    newDeletedData.append(datum)
    return newDeletedData

def saveMatchedData(data, itemNumbersToMatch):
    matchedData = []

    for datum in data:
        for key, value in datum.items():
            if key == "Item Number":
                if value in itemNumbersToMatch:
                    matchedData.append(datum)
    return matchedData

def getRowsByColValue(data, colName, colValue):
    rows = []
    for datum in data:
        for key, value in datum.items():
            if key == colName:
                if value == colValue:
                    rows.append(datum)
    return rows

if __name__ == "__main__":

    # arnageToGKNUniqueRefs = read_excel_file("data.xls", "Arnage'dan GKN'ye")
    # GKNToTebosanUniqueRefs = read_excel_file("data.xls", "GKN'den Tebosan'a")
    # TebosanToGKNUniqueRefs = read_excel_file("data.xls", "Tebosan'dan GKN'ye")

    # titles, values = read_excel_file("data.xls", "GKN'den Tebosan'a", allCols = True)

    # deletedDataReferencesFromGKNToTebosan = read_excel_file("data - silinenler.xls", "Sayfa2 (2)", is_float = True)
    # deletedData = deleteDataFromGKNToTebosan(deletedDataReferencesFromGKNToTebosan, values)
    # write_data_to_excel_file(titles, deletedData, "deletedData")
    
    
    ##################################################### NOTE 15.01.2023
    # SECTION 1
    # titles, data = read_excel_file("data.xls", "Arnage'dan GKN'ye")
    # itemNumbersToMatch = read_excel_file_only_item_numbers("arnageToTebosan.xls")
    # matchedData = saveMatchedData(data, itemNumbersToMatch)
    # write_data_to_excel_file(titles, matchedData, "No1", "No1")
    # exit()
    # !SECTION 1

    # SECTION 2
    # titles, data = read_excel_file("data.xls", "GKN'den Tebosan'a")
    # itemNumbersToMatch = read_excel_file_only_item_numbers("silinmisHali.xls")
    # matchedData = saveMatchedData(data, itemNumbersToMatch)
    # write_data_to_excel_file(titles, matchedData, "No2", "No2")
    # exit()
    # !SECTION 2

    # SECTION 3
    titles, data1 = read_excel_file("data.xls", "Arnage schedule part 1")
    titles, data2 = read_excel_file("data.xls", "Arnage schedule part 2")
    titles, data3 = read_excel_file("data.xls", "Arnage schedule part 3")
    data1.extend(data2)
    data1.extend(data3)
    print("data1 len: ", len(data1))
    itemNumbersToMatch = read_excel_file_only_item_numbers("arnageToTebosan.xls")
    matchedData = saveMatchedData(data1, itemNumbersToMatch)
    print("matced len: ", len(matchedData))
    del data1
    matchedData = getRowsByColValue(matchedData, "Q", "F")
    print("matced len: ", len(matchedData))
    # write_data_to_excel_file(titles, matchedData, "No3", "No3")

    print(matchedData[0:10])
    print("-------------")
    matchedData = sorted(matchedData, key = lambda item : item["Item Number"])
    print(matchedData[0:10])

    exit()
    # !SECTION 3

    # SECTION 4
    # titles, data = read_excel_file("data.xls", "Tebosan'dan GKN'ye")
    # itemNumbersToMatch = read_excel_file_only_item_numbers("tmp18117.xls", "Data")
    # matchedData = saveMatchedData(data, itemNumbersToMatch)
    # write_data_to_excel_file(titles, matchedData, "No4", "No4")
    # exit()
    # !SECTION 4

    print(len(arnageToGKNUniqueRefs))
    print(len(GKNToTebosanUniqueRefs))
    print(len(TebosanToGKNUniqueRefs))

    arnageToGKNDifferencies = []
    GKNToArnageDifferencies = []
    arnageToTebosan = []
    for key, value in enumerate(GKNToTebosanUniqueRefs):
        if value not in arnageToGKNUniqueRefs:
            GKNToArnageDifferencies.append(value)
        else:
            arnageToTebosan.append(value)
    
    for key, value in enumerate(arnageToGKNUniqueRefs):
        if value not in GKNToTebosanUniqueRefs:
            arnageToGKNDifferencies.append(value)
        else:
            pass

    olmayanlar = []
    olanlar = []
    for key, value in enumerate(TebosanToGKNUniqueRefs):
        if value not in GKNToTebosanUniqueRefs:
            olmayanlar.append(value)
        else:
            olanlar.append(value)

    # write_data_to_excel_file(["Reference No"], arnageToGKNUniqueRefs, "arnageToGKN")
    # write_data_to_excel_file(["Reference No"], GKNToTebosanUniqueRefs, "GKNToTebosan")
    # write_data_to_excel_file(["Reference No"], TebosanToGKNUniqueRefs, "TebosanToGKNUniqueRefs")
    # write_data_to_excel_file(["Reference No"], GKNToArnageDifferencies, "GKNToArnageDifferencies")
    # write_data_to_excel_file(["Reference No"], arnageToGKNDifferencies, "arnageToGKNDifferencies")
    # write_data_to_excel_file(["Reference No"], arnageToTebosan, "arnageToTebosan")
    write_data_to_excel_file(olmayanlar, "olmayanlar")
    write_data_to_excel_file(olanlar, "olanlar")
