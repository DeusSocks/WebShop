from datetime import datetime

class Logger:
    def __init__(self, active: bool, path:str):
        self.active = active #активация вывода в консоль
        self.path = path #путь для логов
    def save_log(self, info: str):
        # Получаем текущее время и форматируем его
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{now}] {info}"
        # Записываем в файл с переносом строки (\n)
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(log_entry + "\n")
        if self.active:
            print(log_entry)
