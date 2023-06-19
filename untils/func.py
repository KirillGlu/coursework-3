from datetime import datetime
import json

def get_data(filename):
    """Достает список операций из файла json"""
    with open(filename, "r", encoding='utf-8') as f:
        result = f.read()
        profile = json.loads(result)
        return profile

def last_executed(profile):
    """Добавляет в новый список словари с успешно выполненной операцией"""
    executed_lst = []
    for i in profile:
        if i.get("state") == "EXECUTED":
            executed_lst.append(i)
    return executed_lst

def format_account(account: list):
    """Скрывает цифры счета и номера карты"""
    if len(account[-1]) == 20:
        formatted_account = " ".join(account[:-1]) + ' ' + f'**{account[-1][-4:]}'
    elif len(account[-1]) == 16:
        formatted_account = " ".join(
            account[:-1]) + ' ' + f'{account[-1][:4]} {account[-1][4:6]}** **** {account[-1][-4:]}'
    return formatted_account


def format_data(data):
    """Выводит результат транзакции в необходимом формате"""
    formatted_data = []
    arrow = ' -> '
    for transaction in data:
        date = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = transaction['description']
        to = format_account(transaction['to'].split())

        if 'from' in transaction:
            where_from = format_account(transaction['from'].split())
            transaction_info = where_from + arrow + to
        else:
            transaction_info = to

        amount = transaction['operationAmount']['amount'] + ' ' + transaction['operationAmount']['currency']['name']
        formatted_data.append(f"""
{date} {description}
{transaction_info}
{amount}\n""")
    return formatted_data