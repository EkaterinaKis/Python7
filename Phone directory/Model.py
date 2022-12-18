def search_contact(data, contact):
    data = data.split('\n')
    list1 = []
    contact_found = True
    for i in data:
        if contact in i:
            contact_found = False
            list1.append(i)
    if contact_found is True:
        list1.append(f'Данные по запросу ({contact}) не найдены')
    return list1
