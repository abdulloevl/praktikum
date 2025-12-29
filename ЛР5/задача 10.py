import json
import os

DB_FILE = "database.json"

def _ensure_db_exists():
    """Создать файл БД, если он не существует"""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def _read_db():
    """Безопасное чтение данных"""
    _ensure_db_exists()
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def _write_db(data):
    """Безопасная запись данных"""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add(record):
    """Добавить запись в БД"""
    if not isinstance(record, dict):
        raise ValueError("record должен быть словарём")
    data = _read_db()
    data.append(record)
    _write_db(data)

def find(key, value):
    """Найти записи по ключу и значению"""
    data = _read_db()
    return [record for record in data if record.get(key) == value]



if __name__ == "__main__":
 
    add({"name": "Umar", "age": 20})
    add({"name": "Alice", "age": 25})
    add({"name": "Umar", "age": 30})


    results = find("name", "Umar")
    print("Найденные записи:", results)

    results_age = find("age", 25)
    print("Найденные записи с возрастом 25:", results_age)
