

val = list(range(1,10))
win_version = [(1,2,3),(4,5,6),(3,6,9),(7,8,9),(1,4,7),(2,5,8),(1,5,9),(3,5,7)]

def game_field():
    for i in range(3):
        print("|", val[0+i*3],"|", val[1+i*3],"|", val[2+i*3],"|")


def symbols_take(player_symbol):
 while True:
        x = input('Choose number to place you symbol: ' + player_symbol )
        if not (x in '123456789'):
            print('You chose something wrong\nTry again')
            continue
        x = int(x)
        if str(val[x - 1]) in "XO":
            print('There is number already\nTry again')
            continue
        val[x - 1] = player_symbol
        break

def check_win():
    for each in win_version:
        if (val[each[0] - 1]) == (val[each[1] - 1]) == (val[each[2] - 1]):
            return val[each[1] - 1]
    else:
        return False

def gameplay():
    counter = 0
    while True:
        game_field()
        if counter % 2 == 0:
            symbols_take('X')
        else:
            symbols_take('O')
        if counter > 3:
            winner = check_win()
            if winner:
                game_field()
                print(winner, "You won!")
                break
        counter += 1
        if counter > 8:
            game_field()
            print('Draw')
            break
    
gameplay()



