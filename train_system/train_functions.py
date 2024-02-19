from datetime import time


def add_train(trains):
    """Добавляет информацию о поезде."""
    destination = input("Название пункта назначения: ")
    train_number = input("Номер поезда: ")
    departure_time_str = input("Время отправления (в формате ЧЧ:ММ): ")

    hours, minutes = map(int, departure_time_str.split(':'))

    departure_time = time(hours, minutes)

    train = {
        'название пункта назначения': destination,
        'номер поезда': train_number,
        'время отправления': departure_time,
    }

    trains.append(train)
    trains.sort(key=lambda x: x['название пункта назначения'])


def list_trains(trains):
    """Выводит список всех поездов."""
    line = f'+-{"-" * 35}-+-{"-" * 15}-+-{"-" * 25}-+'
    print(line)
    print(f"| {'Название пункта назначения':^35} | {'Номер поезда':^15} | {'Время отправления':^25} |")

    for train in trains:
        print(line)
        departure_time = train['время отправления'].strftime('%H:%M')
        print(
            f"| {train['название пункта назначения']:^35} | {train['номер поезда']:^15} | {departure_time:^25} |")
    print(line)


def select_trains(trains, search_time_str):
    """Выводит поезда, отправляющиеся после указанного времени."""
    found = False
    result = []

    hours, minutes = map(int, search_time_str.split(':'))

    search_time = time(hours, minutes)

    print(f"Поезда, отправляющиеся после {search_time}:")
    for train in trains:
        train_time = train['время отправления']
        if train_time > search_time:
            result.append(train)
            found = True

    if found:
        return result

    if not found:
        return "Нет поездов, отправляющихся после указанного времени."


def display_help():
    """Выводит справку о доступных командах."""
    print("Список команд:\n")
    print("add - добавить информацию о поезде;")
    print("list - вывести список всех поездов;")
    print("select <время> - вывести поезда, отправляющиеся после указанного времени;")
    print("exit - завершить работу с программой.")
