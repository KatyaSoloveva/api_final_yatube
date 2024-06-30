# Описание проекта


* **Описание**: API для проекта YaTube, версия 1. Предоставляет доступ к функциональности YaTube другим приложениям и сервисам. 
Неавторизованным пользователям разрешены просмотр списка постов, комментариев и групп, а также отдельного поста, комментария и группы (GET-запросы). Для расширеня функциональности нужно пройти JWT-аутентификацию.  
Как это сделать: отправьте POST-запрос на эндпоинт /api/v1/jwt/create/, передав действующий логин и пароль в полях username и password. API вернёт JWT-токен, содержащий поля access (сам токен) и refresh (данные для обновления токена). При каждом запросе к API нужно в заголовке запроса, в поле Authorization, передавать основной токен доступа, полученный в поле access. Перед самим токеном должно стоять ключевое слово Bearer и пробел: Bearer токен.   
Теперь у вас есть доступ к остальной функционалиности: создание публикаций и комментариев (POST-запрос), обновление (PUT-запрос),частичное обновление (PATCH-запрос) и удаление (DELETE-запрос) постов и комментариев (для автора), получение подписок пользователя(GET-запрос) и подписка пользователя на другого пользователя (POST-запрос).

* **Стек**  
  Фреймворки: Django, Django REST Framework.
  Система управления базами данных: Sqlite3. 
  Язык программирования Python.


* **Установка**

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/KatyaSoloveva/api_final_yatube.git
```  

```
cd api_final_yatube
```  
Создать и активировать виртуальное окружение:

```
python3 -m venv env
```
Если у вас Linux/macOS

```
source env/bin/activate
```
Если у вас windows

```
source env/scripts/activate
```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Выполнить миграции:

```
python3 manage.py migrate
```
Запустить проект:

```
python3 manage.py runserver
```

* **Документация для API Yatube**  
  доступна по ссылке http://127.0.0.1:8000/redoc/

* **Примеры запросов к API**  
  * Создание публикации (POST)
  
  http://127.0.0.1:8000/api/v1/posts/  
  Request  
  ```
  {
  "text": "string",
  "image": "string",
  "group": 0
  }
  ```
  Response  
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
  }
  ```
  * Обновление комментария (PUT)
  
  http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/  
  Request  
  ```
  {
  "text": "string"
  }
  ```
  Response  
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
  }
  ```
  * Список сообществ (GET)
  
  http://127.0.0.1:8000/api/v1/groups/  
  Response
  ```
  [
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
  ]
  ```


* **Created by Ekaterina Soloveva**  
https://github.com/KatyaSoloveva
