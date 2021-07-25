Homework 17 - Classwork
"Контрольная на все темы"

Overview

The main features that have currently been implemented are:

    There are models for posts and comments.
    
    Текущее состояние по задачам:
        1. --Пока нет: Пользователь может зарегистрироваться + логин/логаут.
        2. Готово! Пользователь может создавать посты (http://127.0.0.1:8000/classwork/userpost/).
        3. Готово! Пользователь может публиковать посты или убирать их в заготовки (там же).
        4. Готово! Анонимные пользователи могут публиковать комментарии (/classwork/post/).
        5. Готово! Комментарии модерируется перед публикацией (см. admin page).
        6. --Пока нет: Администратор получает уведомление на почту о новом посте или комментарии.
        7. --Пока нет: Пользователь получает уведомление о новом комментарии под постом с сылкой на пост.
        8. Готово! Есть страница с списком всех постов (/classwork/post/).
        9. Готово! Есть страница с списком постов пользователя (/classwork/userpost/).
        10. Готово! Есть страница поста (/classwork/userpost/<int:pk>).
        11. --Пока нет: Есть страница профиля публичная.
        12. --Пока нет: Есть профиль в котором можно изменять свои данные.
        13. Готово! Пагинация постов и комментариев.
        14. Готово! У поста есть заголовок, краткое описание, картинка(опционально ссылка или реальное изображение) и полное описание.
        15. Готово! У комментария есть юзернейм и текст.
        16. Готово! Фикстуры loremipsum (пока самописные данные).
        17. Готово! Админка с функционалом.
        18. --Пока нет: Форма обратной связи с админом (в консоль).
        19. Готово! Темплейты с стилизацией.
        20. --Пока нет: Разные настройки для разработки и продакшена.
        21. Готово! Оптимизация запросов в базу
        22. --Пока нет: Кеширование *
        23. --Пока нет: Селера и парсинг постов из рсс ленты или сайта *
        24. --Пока нет: Pythonanywhere (без кеширования и бэкграунд задач) **

Quick Start

To get this project up and running locally on your computer:

    Set up the Python development environment. We recommend using a Python virtual environment.
    Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):

    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver

    There is a dump of some data in the file classwork/fixtures/db.json
    Available users: 
    "admin" with password "adm123456" - superuser
    "admin2" with password "adm123456"

    Open a browser to http://127.0.0.1:8000/admin/ to open the admin site.
