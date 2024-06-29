# Описание проекта


* **Описание**: API для проекта YaTube

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

* **Примеры запросов к API**  
  * Создание публикации
  
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
  * Обновление комментария
  
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
  * Список сообществ
  
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
  * Получить JWT-токен
  
  http://127.0.0.1:8000/api/v1/jwt/create/  
  Request
  ```
  {
  "username": "string",
  "password": "string"
  }
  ```
  Response
  ```
  {
  "refresh": "string",
  "access": "string"
  }
  ```
