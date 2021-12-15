import random

def intro():
    rules = "МОРСЬКИЙ БІЙ\n\nПравила гри:\n 1)Гравець 1 обирає розсташування своїх кораблів\n\
 2)Гравець 2 обирає розсташування своїх кораблів\n 3)Гравці по-черзі здйснюють хід:\n\
    >>> Якщо у суперника на місці вашого вистрілу знаходиться корабель\n\
        то корабель або його частина 'тоне, а той хто влучив здобуває'\n\
        право зробити ще один хід\n\
Мета гравця — першим потопити всі кораблі супротивника.\n\n\
Правила розміщення:\n    >>> 1 корабель — ряд із 4 клітин («лінкор», або «чотирипалубний»)\n\
    >>> 2 кораблі — ряд із 3 клітин («крейсери», або «трипалубні»)\n\
    >>> 3 кораблі — ряд із 2 клітин («есмінці», або «двопалубні»)\n\
    >>> 4 кораблі — 1 клітина («підводні човни», або «однопалубні»)\n\n\
При розміщенні кораблі не можуть торкатися один одного кутам\n\n\
Для ЗАВЕРШЕННЯ гри введіть\n    >>> 'Здатися'\n\
Введіть координати корабля у вигляді:\n    >>> A1 A2 A3 A4"
    return rules

def create_field():
    return [['' for i in range(10)] for j in range(10)]


def first_player_selection():
    return random.randint(1,2)

def table():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    set_of_moves=set()
    for i in range(len(letters)):
        for j in range(len(numbers)):
            set_of_moves.add(letters[i]+numbers[j])
    return set_of_moves

def move(ships, table):
    step=input('Select a coordinate where to shoot')
    for i in ships:
        if step in i:
            return 'You hit a ship!'
        elif step not in i and step in table:
            return 'You have missed!'
        else:
            return 'There is not a such coordinate. Maybe You already shot that cell!'
            
def set_ships(output_list, user_input):
    def check_proper(list_of) :
        if list_of[0][0]==list_of[1][0] :
            for i in range(abs(int(list_of[0][1])-int(list_of[1][1]))-1):
                list_of.append(list_of[0][0]+str(abs(int(list_of[0][1])-int(list_of[1][1]))-i))
            return list_of
        if list_of[0][1]==list_of[1][1] :
            for i in range(abs(ord(list_of[0][0])-ord(list_of[1][0]))-1):
                list_of.append(str(chr(abs(max([ord(list_of[0][0]), ord(list_of[1][0])])-i-1)))+list_of[0][1])
            return list_of
        print("One of your coordinates is not proper. Insert something like 'B1 D1'")
        return set_ships(output_list, input("Type your ship`s beggining and ending point : ").split())
    checklist=[]
    for i in user_input :
        if i[0] in "ABCDEFGHIJ" and int(i[1]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            checklist.append(True)
    if False not in checklist :
        output_list.append([user_input[0], user_input[1]])
        if len(output_list)==10:
            output_list[len(output_list)-1]=check_proper(output_list[len(output_list)-1])
            return output_list
        else :
            output_list[len(output_list)-1]=check_proper(output_list[len(output_list)-1])
            return set_ships(output_list, input("Type your ship`s beggining and ending point : ").split())
    else :
        print("One of your coordinates is not proper. Insert something like 'B1'")
        return set_ships(output_list, input("Type your ship`s beggining and ending point : ").split())

print(move(create_field(), []))
    
