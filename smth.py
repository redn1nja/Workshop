import random

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
    #Функція для генерування повного списку позицій, зайнятих кораблями.
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

    #Перевірка на правильність вводу.
    checklist=[]
    for i in user_input :
        if i[0] in "ABCDEFGHIJ" and int(i[1]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            checklist.append(True)
    #Головна частина функції - менеджить її поведінку вцілому.
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
    
