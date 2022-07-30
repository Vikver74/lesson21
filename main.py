from shop import Shop
from store import Store
from request import Request


if __name__ == '__main__':
    store = Store()
    shop = Shop()


    while True:
        action = input('Забрать товар со склада или добавить на склад? (введите "забрать" или "добавить",'
                       ' для выхода введите "выход")')
        if action.lower() == 'выход':
            break
        product = input('Введите наименование товара: ')
        quantity = int(input('Введите количество товара: '))

        if action.lower() == 'забрать':
            request = Request('магазин', 'склад', quantity, product)
            if not store.check_remove(request.product, request.amount):
                print('Такого товара нет на складе или количество меньше запрошенного')
                continue
            if not  shop.check_add(request.product, request.amount):
                print('В магазин недостаточно места, попробуйте что-то другое')
                continue

            store.remove(request.product, request.amount)
            shop.add(request.product, request.amount)
            print('Нужное количество есть на складе')
            print('На складе хранится:')
            for item in store.get_items().items():
                print(f'{item[1]}: {item[0]}')

            print('В магазине хранится:')
            for item in shop.get_items().items():
                print(f'{item[1]}: {item[0]}')

        elif action.lower() == 'добавить':
            request = Request('склад', 'магазин', quantity, product)
            if store.check_add(request.amount):
                store.add(request.product, request.amount)
            else:
                print('Не хватает на складе, попробуйте заказать меньше')
        else:
            print('Вы ввели неверное действие')
