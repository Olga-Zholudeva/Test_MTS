# Test_MTS

## Что делает web-приложение:


На сайт подгружаются данные с внешнего открытого API https://jservice.io/api/ . По данному адресу можно получить рандомные вопросы для викторины. Вопросы, ответы и баллы за правильнный ответ подгружаются в таблицу на странице приложения. Пользователь может обновить данные в таблице нажав на кнопку **Update the table**. При нажатии на кнопку произойдет обновлениие данных только в таблице, остальные данные на странице обновляться не будут. Также пользователь может применить фильтр к данным в таблице - выбрать необходимое количество вопросов. Данный фильтр будет учен при нажатии на кнопку обновления страницы.

## Технологии проекта:

- Flask 2.2.5
- Jinja2 3.1.2

## Локальный запуск проекта:

- Клонируем репозиторий: **git clone [Test_MTS](https://github.com/Olga-Zholudeva/Test_MTS.git)**
- Cоздаем виртуальное окружение: **python3 -m venv venv**
- Активируем виртуальное окружение: **. venv/bin/activate**
- Устанавливаем зависимости из файла requirements.txt: **pip install -r requirements.txt**
- Запускаем приложение: **flask run**
- Приложение доступно по адерсу: **http://127.0.0.1:5000/**


## Автор проекта:   
Ольга Жолудева
