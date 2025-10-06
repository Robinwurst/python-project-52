Task Manager
Django-приложение для управления задачами

[![hexlet-check](https://github.com/Robinwurst/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Robinwurst/python-project-52/actions/workflows/hexlet-check.yml)
[![SonarCloud Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Robinwurst_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Robinwurst_python-project-52)
[![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=Robinwurst_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Robinwurst_python-project-52)
[![SonarCloud Bugs](https://sonarcloud.io/api/project_badges/measure?project=Robinwurst_python-project-52&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Robinwurst_python-project-52)
[![SonarCloud Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Robinwurst_python-project-52&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Robinwurst_python-project-52)


Простое, но функциональное веб-приложение на **Django** для управления задачами. Подойдёт как для личного использования, так и в качестве основы для учебного или pet-проекта.

## 🔧 Возможности

- Регистрация и вход по учётной записи  
- Полный контроль над задачами: создание, редактирование, удаление  
- Гибкая система статусов («в работе», «завершено» и т.д.)  
- Метки для категоризации задач  
- Поддержка нескольких языков (включая русский)  
- Адаптивный интерфейс — удобно и на компьютере, и на телефоне  

## 🛠 Технологии

- **Python 3.11+**  
- **Django 4.2**  
- **PostgreSQL**
- **Bootstrap 5**   

Как запустить

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/Robinwurst/python-project-52.git
   cd python-project-52
   ```
2. Установи зависимости:
   ```bash
   make install
   ```
3. Запусти приложение:
   ```bash
   make start
   ```
# Готово! Открой браузер — по умолчанию сервер запустится на http://localhost:8000


## Запустить тесты:
   ```bash
   make test
   ```  
   
## Проверить код на соответствие стилю:
   ```bash
   make lint
   ```