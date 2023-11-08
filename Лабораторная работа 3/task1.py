# TODO Напишите функцию для поиска индекса товара
# TODO Вызовите функцию, что получить индекс товара

#

def find_item_index(products_list, find_item):
    if find_item in products_list:
        return products_list.index(find_item)
    else:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, item)
    if index_item is not None:
        print(f"Первое вхождение товара '{item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{item}' не найден в списке.")