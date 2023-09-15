# Імпортуємо модуль роботи з базою даних
import sqlite3
#Імпортуємо модулі для роботи з запитами
from bs4 import BeautifulSoup
import requests
#Наступній змінній присвоюємо запит для отримання данних із сайта
response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%87%D1%83%D0%BA")
print(response.text)
#Робимо перевірку (Якщо доступ до сайту успішний, тобто статус код =200(що свідчить про успішність з'єднання))
#то викликаємо модуль BeautifulSoup, що дозволяє нап вибирати дані із сайту
if response.status_code == 200:
    soup = BeautifulSoup(response.text,features="html.parser")
    #шуккаємо елемент з властивостями "p",class_="today-temp" (це наша температура), виводимо її значення
    today_temp = soup.find("p", class_="today-temp")
    print(today_temp.text)
    #ПІдключаємось до БД, попередньо створивши файл БД з ім'ям dz_2911.sl3
    connect = sqlite3.connect("dz_2911.sl3")
    #створюємо об’єкт керування підключенням (курсор)
    cur = connect.cursor()
    # ця змінна буде потрібна для передачі даних щодо температури в Кременчузі до БД
    parametri=('Kremenchuk', today_temp.text)
    # Спочатку створюємо (CREATE TABLE) таблицю БД з полями: name та  temperature
    # Після створення прибираємо данний рядок коду
    #сur.execute("CREATE TABLE dz_2911 (name TEXT, temperature TEXT);")
    #Додаємо до полів name та  temperature записи: Kremenchuk' та  today_temp.text зі списка parametri
    cur.execute("INSERT INTO dz_2911 (name, temperature) VALUES (?, ?)", parametri)
    #Зберігаємо зміни в БД
    connect.commit()
    # Закриваємо з'єднання з БД
    connect.close()