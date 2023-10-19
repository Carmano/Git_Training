import requests
import fake_useragent
from bs4 import BeautifulSoup
import pandas
import sqlite3 as sq
import csv

link = 'https://sibsutis.ru/students/eios/otsenki/3352939/'
useragent = fake_useragent.UserAgent().random
session = requests.Session()

header = {
    'User-Agent': useragent
}

data = {
    'backurl': '/students/eios/otsenki/3352939/',
    'AUTH_FORM': 'Y',
    'TYPE': 'AUTH',
    'POPUP_AUTH': 'Y',
    'USER_LOGIN': 'tumen_tuvanchap@mail.ru',
    'USER_PASSWORD': 'Ezonut15!'
}


def parser_rare():
    result_list = {'Дисциплина': [], 'Период контроля': [], 'Вид контроля': [], 'Отметка': [], 'Преподаватели': []}
    session.post(link, data)
    response = session.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    count = 0
    for tr in soup.tbody.find_all('tr'):
        td_list = [child for child in tr.children if child.name is not None and not child.text.strip().isdigit()]
        td_list.pop()
        td_list.pop()
        if len(td_list) == 4:
            continue
        # print(td_list)
        # if count == 5:
        #     break
        # count += 1
        result_list['Дисциплина'].append(td_list[0].text.strip())
        result_list['Период контроля'].append(td_list[1].text.strip())
        result_list['Вид контроля'].append(td_list[2].text.strip())
        result_list['Отметка'].append(td_list[3].text.strip())
        result_list['Преподаватели'].append(td_list[4].text.strip())
    return result_list


def parser_csv():
    bd = sq.connect('C:\\Users\\tuvan\\Desktop\\MyProject\\Rare\\project\\db.sqlite3')
    cursor = bd.cursor()
    with open('C:\\Users\\tuvan\\Desktop\\MyProject\\Test\\result.csv', encoding='utf-8') as file_csv:
        file_reader = csv.reader(file_csv, delimiter=',')
        count = 0
        for row in file_reader:
            if count == 0:
                count += 1
                continue
    bd.commit()


def main():
    df = pandas.DataFrame(data=parser_rare())
    df.to_csv('result.csv')
    # result = pandas.read_csv('result.csv')
    parser_csv()

    # (result)


if __name__ == "__main__":
    main()


# post_requst = session.post(link, data)
# cookies_dict = [
#     {
#         'domain': key.domain,
#         'name': key.name,
#         'path': key.path,
#         'value': key.value
#     }
#     for key in session.cookies
# ]
# session2 = requests.Session()
#
# for cookies in cookies_dict:
#     session2.cookies.set(**cookies)
#
# response = session2.get(link)
# soup = BeautifulSoup(response.text, 'lxml')
# rare = soup.find_all('div', class_='ContentCenterCol')
# print(rare)
