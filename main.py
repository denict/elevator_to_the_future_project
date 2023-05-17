import json  # импорта json
from cropcalc import *  # импортируется файл "cropcalc"

with open('data.json', 'r') as f:  # открытие файла json
    crop_dict = json.load(f)

crop_objects = []  # создание пустого списка

for crop in crop_dict:
    crop_objects.append(Crop(list(crop.values())))  # добавление объектов в список "crop"

contin = 'да'
while contin == 'да':
    calculate_field(crop_objects)
    answer = list(input('Как хотите отсортировать(1-прибыль 2-доход от продажи 3-затраты на посевы и выращивание 4-затраты на хранение):'))
    print_sorted(crop_objects, answer)

    output = generate_output(crop_objects)
    save = input('Сохранить данные?(да/нет)').lower()  # сохранение файлов
    if save == 'да':
        file_name = input('Введите имя файла:')
        with open(file_name + '.json', 'w') as fp:  # рестартинг программы
            json.dump(output, fp, indent=4)
    contin = input('Хотите продолжить?(да/нет)').lower()