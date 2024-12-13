import os

# Функція для запису логів у файл
def log_action(action, details):
    log_file = os.path.join("TP-KB-231-Olexandr-Koretskiy/topic_06/log.txt") 
    with open(log_file, "a") as file:
        file.write(f"{action}: {details}\n")