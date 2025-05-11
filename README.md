### Как пользоваться

Python должен быть установлен\
Клонировать репозиторий и перейти в папку со скриптом
```bash
cd add_links
```

Создать виртуальное окружение и активировать его

```bash
python -m venv venv && source venv/bin/activate
```
Установить зависимости
```bash
python -m pip install -r requirements.txt
```

Переименовать файл  `.env_Example` в `.env` и прописать пути к переиенным окружения\
- `DATABASE_PATH` путь до базы данных
- `FILE_PATH` путь до файла CSV

Запустить скрипт
```bash
python db_fill.py
```
