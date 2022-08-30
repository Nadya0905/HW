# 0. Есть данные в формате json - сделайте файл с исходными данными.
# 1. Реализовать функцию, которая считает ваши данные в json и переделает их в формат csv,
# 2. Функция, котоая сохранит данные в csv файл. (данные должны сохраняться независимо от количества данных - если я добавлю в ваш json файл еще одного человека, работа программы не должна нарушиться, все должно работать.
# 3. Функция которая добавит новую запись в json файл - вводите пошагово сначала имя, потом дату рождения, потом еще все остальное, формируете данные для записи и записываете в дополнение к уже имеющимся в файле записям.
# 4. Такая же функция для добавления в csv
# 5. Функция которая выведет вам данные про одного человека, которого вы запросите по имени
# 6. Функция фильтра по языку - вывести всех сотрудников, у которых среди языков программирования есть тот, который вы запрашиваете. Например, вы запросили Python, вам вывелся список сотрудников, которые используют Python.
# 7. Функция фильтра по росту - среди всех сотрудников, у которых год рождения меньше заданного посчитать средний рост
# 8. Программа должна представлять собой пользовательское меню с предложением выбрать какое-то действие или выйти из программы.
# Выбрали действие - выполнилось - предложили выполнить еще какое-то действие или выйти из программы. И так до бесконечности)


import json
import csv
import os


def pars_from_json_to_csv(raw_path, process_path):
    with open(raw_path, "r", encoding="utf-8") as raw_file, open(process_path, 'w', newline='',
                                                                 encoding="utf-8") as csv_file:
        json_data = json.load(raw_file)
        csv_writer = csv.writer(csv_file)
        for row in json_data:
            print(row)
            values = row.values()
            csv_writer.writerow(values)


def input_person_info(raw_path):
    with open(raw_path, "r", encoding="utf-8") as raw_file:
        json_object = json.load(raw_file)

        name = input("name: ")
        birthday = input("birthday: ")
        height = input("height: ")
        weight = input("weight: ")
        car = input("car: ")
        languages = list(input("languages: ").split(","))

        new_object = dict(
            name=name,
            birthday=birthday,
            height=height,
            weight=weight,
            car=car,
            languages=languages
    )

        json_object.append(new_object)

        with open(raw_path, "w", encoding="utf-8") as update_file:
            json.dump(json_object, update_file)

def input_person_info_2(process_path):
    with open(process_path, "r", encoding="utf-8") as process_file:
        csv_object = csv.reader(process_file)

        csv_rows = [row for row in csv_object]

        name = input("name: ")
        birthday = input("birthday: ")
        height = input("height: ")
        weight = input("weight: ")
        car = input("car: ")
        languages = input("languages: ")

        new_object = [name, birthday, height, weight, car, languages]

        csv_rows.append(new_object)

        with open(process_path, "w", encoding="utf-8") as update_file:
            csv_file = csv.writer(update_file)

            for row in csv_rows:
                csv_file.writerow(row)

def person_info(test_path):

    with open(test_path, "r", encoding="utf-8") as raw_file:
        data = json.loads(raw_file.read())
        for i in data:
            if i["name"] == "Maria Ivanova":
                print(i["name"])

def languages_info(test_path):

    with open(test_path, "r", encoding="utf-8") as raw_file:
        data = json.loads(raw_file.read())
        input_language = input("")
        for h in data:
            languages = h.get("languages")
            name = h.get("name")
            if input_language in languages:
                print(name)


def height_info(test_path):

    with open(test_path, "r", encoding="utf-8") as raw_file:
        data = json.loads(raw_file.read())
        person_counter = 0
        sum_height = 0
        for item in data:
            birthday = item.get("birthday")
            year = int(birthday[-4:])
            height = int(item.get("height"))
            if year < 1999:
                person_counter += 1
                sum_height += height
        avg_height = sum_height/person_counter
        print(avg_height)


def main():

    menu_message = """
        Hi there, for starting an app you need to select one of available option:
 
        1 - Function to save data to csv file
        2 - Function to add data to json file
        3 - Function to add data to csv
        4 - Data about one person, whom you request by name
        5 - Languages filter function
        6 - Height filter function
        7 - Exit

        """

    application_switcher = True

    while application_switcher:

        test_path = os.path.join("data\\raw\\test_1.json")
        process_path = os.path.join("data\\process\\test_1.csv")

        print(menu_message)

        try:
            client_option = int(input("please, input number:"))

        except Exception as e:
            print("incorrect number, please, try again")
            continue

        if client_option == 1:
            pars_from_json_to_csv(raw_path=test_path, process_path=process_path)
        elif client_option == 2:
            input_person_info(raw_path=test_path)
        elif client_option == 3:
            input_person_info_2(process_path=process_path)
        elif client_option == 4:
            person_info(test_path=test_path)
        elif client_option == 5:
            languages_info(test_path=test_path)
        elif client_option == 6:
            height_info(test_path=test_path)
        elif client_option == 7:
            application_switcher = False

        else:
            print("this option isn't available")
            continue

    dirname = os.path.dirname(__file__)
    print(dirname)
    print(__file__)
    test_path = os.path.join(dirname, "data\\raw\\test_1.json")
    process_path = os.path.join(dirname, "data\\process\\test_1.csv")
    person_info(test_path)
    languages_info(test_path)
    height_info(test_path)
    pars_from_json_to_csv(raw_path=test_path, process_path=process_path)


main()
