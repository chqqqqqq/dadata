from api import get_data
from db import create_table, select_all, update_all


#Обновление настроек и вывод в консоль
def update_settings(settings):
    print('----------------------------------------------------------------------------------------------')
    print(f'Текущие настройки:\n'
          f'url: {settings[0]}\n'
          f'api-key: {settings[1]}\n'
          f'язык: {settings[2]}')
    print('----------------------------------------------------------------------------------------------')
    print('Введите новые настройки:')
    settings = (input('url:'), input('api-key:'), input('язык:'))
    update_all(settings)
    print('----------------------------------------------------------------------------------------------')
    print('Настройки обновлены.')

#Поиск запроса пользователя и вывод результатов в консоль
def search(settings, query):
    print('----------------------------------------------------------------------------------------------')
    data = get_data(settings, query, count=10)
    if data == None:
        print("Что-то пошло не так, проверьте настройки!")
        update_settings(settings)
    else:
        if len(data) != 0 :
            print(f'Найдено {len(data)} вариантов: ')
            for i, j in enumerate(data):
                print(f'{i + 1}. {j["value"]}')
            while True:
                print('----------------------------------------------------------------------------------------------')
                user_message = int(input(f"Введите вариант от 1 до {len(data)}:"))
                if user_message in range(1, len(data) + 1):
                    break
                else:
                    continue
            query = data[user_message - 1]["value"]
            data = get_data(settings, query=query, count=1)[0]
            geo_lat = data["data"]["geo_lat"]
            geo_lon = data["data"]["geo_lon"]
            print('----------------------------------------------------------------------------------------------')
            print(f'Адрес: "{data["value"]}" | Координаты {geo_lat},{geo_lon}')
        else:
            print('Ничего не удалось найти. Попробуйте еще раз!')

#Основной алгоритм выполнения программы
def main():
    create_table()
    print('----------------------------------------------------------------------------------------------')
    print('Для поиска координат введите адрес! \n'
          'Для перехода в меню настроек введите "настройки", для завершения работы - "выход".')
    update_settings(settings=select_all())
    while True:
        print('----------------------------------------------------------------------------------------------')
        settings = select_all()
        user_message = input("Введите запрос:")
        if user_message == "выход":
            print('----------------------------------------------------------------------------------------------')
            print('Всего доброго!')
            print('----------------------------------------------------------------------------------------------')
            break
        elif user_message == 'настройки':
            update_settings(settings)
            continue
        else:
            search(settings, query=user_message)
            continue


if __name__ == "__main__":
    main()


