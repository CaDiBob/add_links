import sqlite3
import csv

from environs import Env


columns = [
    "id",
    "name",
    "active",
    "user_id",
    "interval",
    "url",
    "type",
    "weight",
    "hostname",
    "port",
    "created_date",
    "keyword",
    "maxretries",
]


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if not any(row.values()):
                continue
            filtered_row = {key: row[key] for key in columns if key in row}
            data.append(filtered_row)
        return data


def insert_to_db(proxies, table_name, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if not proxies:
        print(f"Нет данных для вставки в {table_name}")
        return

    columns = list(proxies[0].keys())
    placeholders = ", ".join(["?"] * len(columns))
    column_names = ", ".join(columns)
    query = (f"INSERT INTO {table_name} "
             f"({column_names}) VALUES ({placeholders})")

    values = [tuple(row[col] for col in columns) for row in proxies]
    cursor.executemany(query, values)
    conn.commit()
    print(f"Добавлено {len(values)} записей в таблицу {table_name}")


def main():
    env = Env()
    env.read_env()
    csv_file_path = env("FILE_PATH")
    db_path = env("DATABASE_PATH")
    result = read_csv(csv_file_path)
    table_name = "monitor"
    insert_to_db(result, table_name, db_path)


if __name__ == "__main__":
    main()
