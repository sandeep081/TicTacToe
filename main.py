def tic_tac(p1, s1, p2, s2):
    li = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print(p1 + ", " + p2 + " Welcome to Playground!!...Let's Play")
    print(' ' + li[0][0] + ' | ' + li[0][1] + ' | ' + li[0][2])
    print('__________')
    print(' ' + li[1][0] + ' | ' + li[1][1] + ' | ' + li[1][2])
    print('__________')
    print(' ' + li[2][0] + ' | ' + li[2][1] + ' | ' + li[2][2])
    count = 0
    com_li = list(map(str, range(1, 10)))
    quit_list = ['exit', 'bye', 'exit()']
    while True:
        if count % 2 == 0:
            p = p1
            s = s1
        else:
            p = p2
            s = s2
        while True:
            while True:
                x = input(p + " Enter your choice: ").lower()
                if x in quit_list:
                    exit()
                if x not in com_li:
                    print("Enter Valid no. b/w 1-9 or for exit type exit")
                else:
                    x = int(x)
                    break
            if x >= 7:
                i = 0
                j = x - 7
            elif x >= 4:
                i = 1
                j = x - 4
            else:
                i = 2
                j = x - 1
            if li[i][j] == " ":
                li[i][j] = s
                break
            else:
                print("Warning! This is a fare game you can't override someone else's position.")
        print(' ' + li[0][0] + ' | ' + li[0][1] + ' | ' + li[0][2])
        print('__________')
        print(' ' + li[1][0] + ' | ' + li[1][1] + ' | ' + li[1][2])
        print('__________')
        print(' ' + li[2][0] + ' | ' + li[2][1] + ' | ' + li[2][2])
        for i in range(3):
            s_com = s + s + s
            st1 = ""
            st2 = ""
            st3 = ""
            st4 = ""
            for j in range(3):
                st1 += li[i][j]
                st2 += li[j][i]
                st3 += li[j][j]
                st4 += li[j][2 - j]
            if s_com == st1 or s_com == st2 or s_com == st3 or s_com == st4:
                print(p + ", You won the match congratulations!")
                return

        if count < 8:
            count += 1
        else:
            print('OOPSY!, Match is drawn')
            return


def main(player1, sign1, player2, sign2):
    x = 'YES'
    while x == 'YES':
        tic_tac(player1, sign1, player2, sign2)
        while True:
            q = input('Wanna Play again??...(Y/N) ').upper()
            if q == 'Y' or q == 'N':
                break
            else:
                print("Please, enter correct choice Dude!!")

        if q == 'N':
            print(player1 + ', ' + player2 + ' Thanks for playing...Bye!')
            exit()


if __name__ == "__main__":
    pla1 = input("Enter player 1 name: ")
    while True:
        sig1 = input(pla1 + " Choose X or O : ").upper()
        if sig1 == 'X' or sig1 == 'O':
            break
        else:
            print("Error : Enter correct choice.")
    pla2 = input("Enter player 2 name: ")
    if sig1 == 'X':
        sig2 = 'O'
    else:
        sig2 = 'X'
    main(pla1, sig1, pla2, sig2)
