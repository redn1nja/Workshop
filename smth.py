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
            return 'There is not a such coordinate. Maybe You already shot that cell!')
            

print(move(create_field(), []))
    
