#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from train_system import add_train, list_trains, select_trains, display_help


def main():
    """Основная функция управления программой."""
    trains = []

    while True:
        command = input(">>> ").lower()

        match command:
            case 'exit':
                break
            case 'add':
                add_train(trains)
            case 'list':
                list_trains(trains)
            case 'select':
                selected = select_trains(trains, input("Введите время для поиска поездов (в формате ЧЧ:ММ): "))
                if isinstance(selected, list):
                    list_trains(selected)
                else:
                    print(selected)
            case 'help':
                display_help()
            case _:
                print(f"Неизвестная команда {command}")


if __name__ == '__main__':
    main()
