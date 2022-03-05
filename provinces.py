import csv
with open("provinces.txt", "rt") as provinces:
    reader = csv.reader(provinces)

    provinces_list = []
    for province in provinces:
        provinces_list.append(province)
    print(provinces_list)