import json

def compare_json_files(file1_path, file2_path, ignored_keys=[]):
    # Открываем и читаем JSON файлы
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        json1 = json.load(file1)
        json2 = json.load(file2)

    # Сравниваем JSON объекты
    return compare_json_objects(json1, json2, ignored_keys)

def compare_json_objects(obj1, obj2, ignored_keys):
    # Если оба объекта - это словари
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        return compare_dicts(obj1, obj2, ignored_keys)
    
    # Если оба объекта - это списки
    elif isinstance(obj1, list) and isinstance(obj2, list):
        return compare_lists(obj1, obj2, ignored_keys)
    
    # Для других типов данных (строки, числа и т.д.)
    else:
        return obj1 == obj2

def compare_dicts(dict1, dict2, ignored_keys):
    # Проверяем ключи, игнорируя указанные ключи
    dict1_keys = set(dict1.keys()) - set(ignored_keys)
    dict2_keys = set(dict2.keys()) - set(ignored_keys)
    
    if dict1_keys != dict2_keys:
        return False
    
    # Сравниваем значения для каждого ключа
    for key in dict1_keys:
        if not compare_json_objects(dict1[key], dict2[key], ignored_keys):
            return False
    return True

def compare_lists(list1, list2, ignored_keys):
    # Проверяем длину списков
    if len(list1) != len(list2):
        return False
    
    # Сравниваем каждый элемент списка
    for item1, item2 in zip(list1, list2):
        if not compare_json_objects(item1, item2, ignored_keys):
            return False
    return True

# Пример использования:
'''

file1_path = "file1.json"
file2_path = "file2.json"
ignored_keys = ["id"]  # ключи, которые нужно игнорировать
result = compare_json_files(file1_path, file2_path, ignored_keys)
print("JSON файлы одинаковы" if result else "JSON файлы различаются")

'''
