import requests
import json

#запрос к веб-сервису jsonplaceholder.typicode.com и получает все записи (посты) в виде JSON-объекта.
# Затем он проходит по всем элементам ответа и выводит названия постов (title).
def get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    for x in response:
        print(x['title'])

#возвращает конкретный пост под номером 42 в формате JSON.
#После этого код просто выводит содержимое полученного JSON-объекта на экран.
def get_one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response)

#Этот код позволяет создать новый пост на сервисе jsonplaceholder.typicode.com.
#Он создает объект JSON с полями title, body и userId, затем кодирует этот объект в строку с помощью функции json.dumps
#Затем код отправляет POST-запрос к URL 'https://jsonplaceholder.typicode.com/posts' с использованием метода requests
#передав тело запроса и заголовки. В конце код выводит ответ сервера в формате JSON.
def post_new_post():
    headers = {"Content-type": 'application/json; charset=UTF-8'}
    body = json.dumps({'title': 'foo', 'body': 'bar', 'userId': 1})
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
         data=body, headers=headers)
    print(response.json())


get_all_posts()
get_one_post()
post_new_post()


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')
df2 = pd.DataFrame.from_dict({'a': [1, 2], 'b': [3, 4]})
print(df2)

df.to_csv('./tmp.csv')  # Запись в файл

print(df.info) # Вся информация
print(df.head(3)) # Первые 3 записи
print(df.tail(5)) # Последние 5 записей
print(df.dtypes) # Типы всех колонок

from PIL import Image

img1 = Image.open("image.png")
img2 = Image.open("2024-09-12_23-06-07.png")

#img1.show() # Открывает изображение
print(img2.size) # Информация об изображении
new_size = (240, 320)
img2.thumbnail(new_size) # Меняем размер изображения
print(img2.save("2024.png"))  # Сохраняем

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'a:\n {a}')
# получаем количество вложенности массива
print(f'a.ndim:\n {a.ndim}')
# размер матрицы массива
print(f'a.shape:\n {a.shape}')
# получаем числа с равным интервалом в определенном промежутке
print(np.linspace(0, 21, num=8, dtype=np.int64))