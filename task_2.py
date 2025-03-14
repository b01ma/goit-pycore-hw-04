''' 
    У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить 
    унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:
        60b90c1c13067a15887e1ae1,Tayson,3
    Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та 
    повертає список словників з інформацією про кожного кота.




    Рекомендації для виконання:

    Використовуйте with для безпечного читання файлу.
    Пам'ятайте про встановлення кодування при відкриті файлів
    Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
    Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
    Опрацьовуйте можливі винятки, пов'язані з читанням файлу.
'''
# creat cats info file
def create_cats_info_file(path: str) -> int:
    '''
        Function to create cats info file
        
        :param path: str: path to the file
        :return: int: 0 if success
    '''
    cats = [
        '60b90c1c13067a15887e1ae1,Tayson,3',
        '60b90c2413067a15887e1ae2,Vika,1',
        '60b90c2e13067a15887e1ae3,Barsik,2',
        '60b90c3b13067a15887e1ae4,Simon,12',
        '60b90c4613067a15887e1ae5,Tessi,5',
        '60b90c5213067a15887e1ae6,Tommy,8',
        '60b90c6113067a15887e1ae7,Lucy,4',
        '60b90c7013067a15887e1ae8,Charlie,10',
        '60b90c7913067a15887e1ae9,Sasha,7',
        '60b90c8813067a15887e1aea,Max,9',
        '60b90c9613067a15887e1aeb,Nina,6',
        '60b90ca013067a15887e1aec,Leo,15',
        '60b90cb013067a15887e1aed,Oliver,4',
        '60b90cc013067a15887e1aee,Luna,11',
        '60b90cd013067a15887e1aef,Rocky,2',
        '60b90ce013067a15887e1af0,Izzy,3',
        '60b90cf013067a15887e1af1,Jack,13',
        '60b90d0013067a15887e1af2,Chloe,6',
        '60b90d1013067a15887e1af3,Kona,9',
        '60b90d2013067a15887e1af4,Felix,1',
        '60b90d3013067a15887e1af5,Harley,8',
        '60b90d4013067a15887e1af6,Bella,14',
        '60b90d5013067a15887e1af7,Theo,5',
        '60b90d6013067a15887e1af8,Henry,7',
        '60b90d7013067a15887e1af9,Remy,10',
        '60b90d8013067a15887e1afa,Peanut,6',
        '60b90d9013067a15887e1afb,Willow,12',
        '60b90da013067a15887e1afc,George,3',
        '60b90db013067a15887e1afd,Rocky,11',
        '60b90dc013067a15887e1afe,Milo,6',
        '60b90dd013067a15887e1aff,Rex,10',
        '60b90de013067a15887e1b00,Spooky,2',
        '60b90df013067a15887e1b01,Otis,8',
        '60b90e0013067a15887e1b02,Lola,4',
        '60b90e1013067a15887e1b03,Piper,9',
        '60b90e2013067a15887e1b04,Ruby,6',
        '60b90e3013067a15887e1b05,Simba,10',
        '60b90e4013067a15887e1b06,Fluffy,3',
        '60b90e5013067a15887e1b07,Zoe,14',
        '60b90e6013067a15887e1b08,Rocky,5',
        '60b90e7013067a15887e1b09,Juno,8',
        '60b90e8013067a15887e1b0a,Tinkerbell,6',
        '60b90e9013067a15887e1b0b,Lucy,4',
        '60b90ea013067a15887e1b0c,Max,7',
        '60b90eb013067a15887e1b0d,Peanut,2',
        '60b90ec013067a15887e1b0e,Bella,5',
        '60b90ed013067a15887e1b0f,Oscar,6',
        '60b90ee013067a15887e1b10,Jasper,9',
        '60b90ef013067a15887e1b11,Charlie,8',
        '60b90f0013067a15887e1b12,Izzy,4',
        '60b90f1013067a15887e1b13,Sasha,2',
        '60b90f2013067a15887e1b14,Luna,7',
        '60b90f3013067a15887e1b15,Tommy,10',
        '60b90f4013067a15887e1b16,Theo,3',
        '60b90f5013067a15887e1b17,Harley,9',
        '60b90f6013067a15887e1b18,Luna,5',
    ]
    
    with open(path, 'w', encoding="utf-8") as file:
        for cat in cats:
            file.write(f'{cat}\n')
    return 0

create_cats_info_file('./cats.txt')

# get cats info
def get_cats_info(path: str) -> list:
    '''
        Function to get cats info from the file
        
        :param path: str: path to the file
        :return: list: list of dictionaries with cats info
    '''
    cats = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()

            for line in data:
                if (line.strip() == ''):
                    continue
                id, name, age = line.strip().split(',')
                cats.append({'id': id, 'name': name, 'age': age})
    except FileNotFoundError:
        print(f'File not found: {path}')
    except Exception as e:
        print(f'Error: {e}')
    return cats
    
cats_info = get_cats_info('./cats.txt')
for cat in cats_info:
    print(f"id: {cat['id']:<20}\t name: {cat['name']:<10}\t age: {cat['age']:<5}")