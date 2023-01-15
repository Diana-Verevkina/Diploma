# Портал и рекомендательная система по психологической литературе
 <img src="img.png">

## Описание
В данном проекте реализован портал и рекомендательная система по психологической 
литературе.
На портале можно просмотреть множество книг по психологии и саморазвитию и 
подобрать подходящую для себя с помощью реализованного алгоритма рекомендаций.

Реализованы возможности:
- Регистрация и авторизация пользователей на платформе 
- Смена пароль
- Добавление новый книг и авторов
- Просмотр всех книг в базе данных 
- Просмотр описания для каждой книги
- Добавление книги в избранное
- Просмотр всех добавленных в базу авторов
- Общение между пользователями в комментариях под книгами
- Подбор книги по рекомендациям

## Рекомендательная система
В проекте реализована рекомендательная система content-based, которая позволяет 
пользователю подобрать книги, похожие на те, которые ему нравятся.
Система работает по следующему принципу:

Описания всех книг приводятся к наиболее удобному для анализа виду 
(приведение к нижнему регистру, удаление окончаний слов, приведение слов к 
начальной форме, удаление стоп-слов).
Далее между векторами, созданными по описаниями, вычисляется косинусное 
расстояние и в результате выводятся наиболее похожие книги на ту, которую задал пользователь.

## Использованные технологии

Python 3.7.9, Django~=2.2.16, Pandas, HTML, CSS, BootStrap, Git, SQL, SQLite, 
nltk, spacy, pymorphy2, scipy, matplotlib

# Запуск проекта в dev-режиме
- Клонирование репозитория
```python
git clone git@github.com:Diana-Verevkina/Diploma.git
cd Diploma
```
- Установка и активация виртуального окружения
```python
python -m venv venv
source venv/bin/activate
```
- Установка зависимостей
```python
pip install -r requirements.txt
```
- Выполнить миграции
```python
python3 manage.py migrate
```
- Запуск проект
В папке с файлом manage.py выполните команду:
```python
python3 manage.py runserver
```