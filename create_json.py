import json  # импорт json

crops = []

for crop in species:  #
    dict_crop = {}
    for i in range(len(keys)):
        dict_crop[keys[i]] = crop[i]
    crop.append(dict_crop)

with open('data.json', 'w') as fp:  # открытие json-ого файла
    json.dump(crops, fp, indent=4)