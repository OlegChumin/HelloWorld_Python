import psycopg2

# Настройки подключения к базе данных
db_config = {
    "dbname": "testdb",  # Имя базы данных
    "user": "your_username",  # Имя пользователя
    "password": "your_password",  # Пароль
    "host": "localhost",  # Хост (обычно localhost) 127.0.0.0
    "port": "5432"  # Порт PostgreSQL (по умолчанию 5432)
}

# Подключение к базе данных
try:
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    print("Успешное подключение к базе данных!")

    # Выполняем SQL запрос (например, выбор всех записей из таблицы users)
    cursor.execute("SELECT * FROM users;")

    # Получаем все результаты запроса
    rows = cursor.fetchall()

    # Выводим результаты
    for row in rows:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Ошибка при работе с базой данных: {error}")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Подключение к базе данных закрыто.")

        # CREATE
        # TABLE
        # users(
        #     id
        # SERIAL
        # PRIMARY
        # KEY,
        # name
        # VARCHAR(50),
        # age
        # INT
        # );
        #
        # INSERT
        # INTO
        # users(name, age)
        # VALUES('Alexey', 30), ('Maria', 25), ('Ivan', 28);