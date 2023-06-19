from untils.func import get_data, last_executed, format_data

#Задаем файл из которого достаем список операций
filename = 'operations.json'

executed_lst = last_executed(get_data(filename))

#Используем только 5 последних операций
last_executed_lst = executed_lst[:-6:-1]
#Сортируем операции по дате
last_executed_lst.sort(key=lambda x: x.get("date"), reverse=True)

#Выводим результат
print(*(format_data(last_executed_lst)))