# Simple Flask Web App

Это простое веб-приложение на Flask, которое позволяет пользователям добавлять и удалять элементы в базе данных SQLite через веб-интерфейс.

## Интерфейс
![alt text](https://github.com/azat-git/to-do-list/blob/master/ui/ui.png)


## Особенности

- Добавление элементов в базу данных через веб-форму.
- Удаление элементов из списка.
- Отображение списка всех добавленных элементов.

## Технологии

- **Python 3**: Язык программирования.
- **Flask**: Веб-фреймворк для Python.
- **SQLite**: Легковесная база данных для хранения элементов.

## Установка и запуск

Для запуска этого приложения следуйте приведенным ниже шагам:

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/azat-git/to-do-list.git
   ```
2. Установите зависимости:
   ```
   pip install flask sqlite3
   ```
3. Запустите приложение:
   ```
   python app.py
   ```

После запуска, приложение будет доступно по адресу `http://127.0.0.1:5000/` в вашем браузере.

## Структура проекта

- `app.py`: Основной файл приложения Flask.
- `db.py`: Файл для работы с базой данных SQLite.
- `templates/`: Каталог для HTML-шаблонов.
  - `index.html`: Шаблон веб-страницы.
