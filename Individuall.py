#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys

# Список работников.
airplanes = []


def get_airplane():
    """
    Запросить данные о работнике.
    """
    path = input("Название пункта назначения рейса ")
    number = input("Номер рейса ")
    model = float(input("Тип самолёта "))

    # Создать словарь.
    return {
        'path': path,
        'number': number,
        'model': model,
    }


def display_airplanes(race):
    """
    Отобразить список работников.
    """
    # Проверить, что список работников не пуст.
    if race:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Пункт назначения",
                "Номер рейса",
                "Тип самолёта"
            )
        )
        print(line)

        for airplane in race:
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    airplane.get('path', ''),
                    airplane.get('number', ''),
                    airplane.get('model', 0)
                )
            )
        print(line)

    else:
        print("Таких рейсов нет.")


def select_airplanes(race, sel):
    """
    Выбрать работников с заданным стажем.
    """
    result = []
    for airplane in race:
        if airplane.get('path') <= sel:
            result.append(airplane)

    return result


def main():
    """
    Главная функция программы.
    """

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            airplane = get_airplane()

            airplanes.append(airplane)
            if len(airplanes) > 1:
                airplanes.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            display_airplanes(airplanes)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = str(parts[1])

            selected = select_airplanes(airplanes, sel)
            display_airplanes(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
