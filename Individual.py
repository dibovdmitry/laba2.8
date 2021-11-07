#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_airplane():
    path = input("Название пункта назначения ")
    number = input("Номер рейса ")
    model = float(input("Тип самолёта "))

    return {
        'path': path,
        'number': number,
        'model': model,
    }


def display_airplanes(race):
    """
    """
    if race:
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

        for idx, worker in enumerate(airplanes, 1):
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
        print("Нет таких рейсов.")


def select_airplanes(race, info):
    result = []
    for employee in race:
        if employee.get('path') == info:
            print('Пункт назначения', airplane.get('path', ''))
            print('Номер рейса', airplane.get('number', ''))
            print('Тип самолёта:', airplane.get('model', ''))

        return result


def main():
    airplanes = []

    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            airplane = get_airplane()

            airplanes.append(airplane)
            if len(airplanes) > 1:
                airplanes.sort(key=lambda item: item.get('path', ''))

        elif command == 'list':
            display_airplanes(airplanes)

        elif command.startswith('select '):
            parts = command.split('', maxsplit=3)
            info = str(parts[1])

            selected = select_airplanes(airplanes, info)
            display_airplanes(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <рейс> - запросить информацию о рейсе;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
