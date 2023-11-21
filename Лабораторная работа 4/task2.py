# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считать содержимое CSV файла
    with open(INPUT_FILENAME, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Преобразовать в список словарей
        data = [row for row in csv_reader]

    # Сериализовать в файл JSON с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    # Вызвать функцию для выполнения задачи
    task()

    # Вывести содержимое созданного JSON файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")