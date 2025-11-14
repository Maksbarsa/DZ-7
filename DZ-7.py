# with open('myenv2/text.txt', 'r', encoding='utf-8') as text_file:
#     bludo = []
#     for i in text_file:
#         name_bluda = i.strip()
#         kol_ingrid = int(text_file.readline())
#         ingrid = []
#         for _ in range(kol_ingrid):
#             ingr = text_file.readline().strip().split(' | ')
#             ingredient_name, quantity, measure = ingr
#             ingrid.append({"ingredient_name": ingredient_name,
#                            "quantity": quantity,
#                            "measure": measure})
#         text_file.readline()
#         bludo.append({name_bluda: ingrid})
#     result = {}
#     for dish in bludo:
#         result.update(dish)
#     print(result)







#     bludo1 = name_bluda
#     bludo2 = ['Запеченный картофель', 'Омлет', 'Утка по-пекински']
#     kol_person = 3
#
#     def menu (bludo2, kol_person = 0):
#         lst = []
#         for i in bludo2:
#             b = [i if i in result.keys() else None]
#             lst.append(result[i])
#         lst1 = []
#         for x in lst:
#             lst1 += x
#         result_dict = {
#             item['ingredient_name']: {'measure': item['measure'], 'quantity': int(item['quantity']) * kol_person}
#             for item in lst1
#         }
#
#         print(result_dict)
#
#     menu(bludo2, kol_person)





filenames = ['DZ7/1.txt', 'DZ7/2.txt', 'DZ7/3.txt']

filenames_sort = []

filenames_sort1 = []

for i in filenames:
    with open(i, 'r', encoding='utf-8') as infile:
        a = infile.readlines()
        x = {i : int(len(a))}
        filenames_sort.append(x)
sorted_list = sorted(filenames_sort, key=lambda x: list(x.values())[0])
b = sorted_list
for x in b:
    for o in x:
        filenames_sort1.append(o)
with open('DZ7/4.txt', 'w', encoding='utf-8') as text4:
    for i in filenames_sort1:
        with open(i, 'r', encoding='utf-8') as infile:
            text4.write(infile.read())
            text4.write('\n')
print("Слияние завершено!")