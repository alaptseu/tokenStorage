from terminaltables import AsciiTable

def print_list_data(list_data, header):
    if len(list_data) > 0:
        for el in list_data:
            table_data = [el.keys(), el.values()]
            table = AsciiTable(table_data)
            table.title = el[header]
            print (table.table)
            print("\n")
