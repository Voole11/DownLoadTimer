import glob
import json

# Шаблон для поиска файлов с нужным расширением (например, .txt)
file_pattern = '*.acf'
data = {}

def thieve(steam_folders):
    for steam_folder in steam_folders:
        steam_folder = steam_folder[:-12]
        # Полный путь с шаблоном
        search_pattern = f'{steam_folder}/{file_pattern}'
        
        # Список всех файлов с нужным расширением в папке
        files = glob.glob(search_pattern)
        print(f'Найдено файлов: {len(files)}')

    for t, file_path in enumerate(files):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            app_id = content.split('\n')[2]
            app_id = app_id.split('"')[3]
            name = content.split('\n')[5]
            name = name.split('"')[3]
            steam_id = content.split('\n')[13]
            steam_id = steam_id.split('"')[3]
            data[t] = {'app_id': app_id, 'name': name, 'steam_id': steam_id}

    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)