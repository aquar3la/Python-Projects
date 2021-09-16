coordinate = ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3"]
entry, state, turn, player, keep = [" ", " ", " ", " ", " ", " ", " ", " ", " "], 0, 0, "", 0


def game():
    print("---------")
    print("|", entry[0], entry[1], entry[2], "|")
    print("|", entry[3], entry[4], entry[5], "|")
    print("|", entry[6], entry[7], entry[8], "|")
    print("---------")


game()
while keep == 0:
    coordinates = input("Enter the coordinates:")
    mini = coordinates.split()
    if mini[0].isalpha() or mini[1].isalpha():
        state = 2
    else:
        mini = [int(x) for x in mini]
        if (mini[0] or mini[1]) not in range(1, 4):
            state = 1

    for idx, item in enumerate(coordinate):
        if item == coordinates:
            if entry[idx] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                if turn % 2 == 0:
                    player = "X"
                elif turn % 2 == 1:
                    player = "O"
                entry[idx] = entry[idx].replace(" ", player)
                turn += 1
                a, b, c, d = entry[:3], entry[3:6], entry[6:9], entry[0:7:3]
                e, f, g, h = entry[0:9:4], entry[2:9:3], entry[2:7:2], entry[1:8:3]
                game()
                if ['X', 'X', 'X'] in (a, b, c, d, e, f, g, h):
                    print("X wins")
                    keep = 1
                elif ['O', 'O', 'O'] in (a, b, c, d, e, f, g, h):
                    print("O wins")
                    keep = 1
                elif abs(entry.count('X') - entry.count('O')) == (1 or 0) and entry.count(' ') == 0:
                    print("Draw")
                    keep = 1

        elif state == 1:
            print("Coordinates should be from 1 to 3!")
            state = 0
            break
        elif coordinates not in coordinate or state == 2:
            print("You should enter numbers!")
            state = 0
            break
