import random
plw = 0
cpw = 0
dr = 0
def main():
    #global variables for the score plw = players wins , cpw = cpu wins , dr = draw
    global plw
    global cpw
    global dr
    print "Welcome to your demise!"
    #3 list for 3 rows and 3 cells for 3 collums
    a=[' ',' ',' ']
    b=[' ',' ',' ']
    c=[' ',' ',' ']
    print a
    print b
    print c
    #while the are no winning combinations
    while not (a[0] == a[1] == a[2] == "O" or a[0] == b[0] == c[0] == "O" or a[1] == b[1] == c[1] == "O" or a[2] == b[2] == c[2] == "O" or b[0] == b[1] == b[2] == "O" or c[0] == c[1] == c[2] == "O" or a[0] == b[1] == c[2] =="O" or a[2] == b[1] == c[0] == "O"  or a[0] == a[1] == a[2] == "X" or a[0] == b[0] == c[0] == "X" or a[1] == b[1] == c[1] == "X" or a[2] == b[2] == c[2] == "X" or b[0] == b[1] == b[2] == "X" or c[0] == c[1] == c[2] == "X" or a[0] == b[1] == c[2] =="X" or a[2] == b[1] == c[0] == "X"):
        #players turn
        print "Player's Turn"
        #player choose row and collum
        player_row = input("Write 'a' , 'b' or 'c' for the row: ")
        player_collum = input("Write 0,1 or 2 for the collum: ")
        while not (player_collum == 0 or player_collum == 1 or player_collum == 2):
            player_collum = input("Please Write 0 , 1 or 2 only!! ")
        while player_row[player_collum] == "O" or player_row[player_collum] == "X":
            player_row = input("You have to place it in a empty cell! Write a,b or c for the row: ")
            player_collum = input("You have to place it in a empty cell! Write 1,2 or 3 for the collum: ")
            while not (player_collum == 0 or player_collum == 1 or player_collum == 2):
                player_collum = input("Please Write 0 , 1 or 2 only!! ")
        player_row[player_collum] = "O"
        #show results
        print a
        print b
        print c
        if a[0] == a[1] == a[2] == "O" or a[0] == b[0] == c[0] == "O" or a[1] == b[1] == c[1] == "O" or a[2] == b[2] == c[2] == "O" or b[0] == b[1] == b[2] == "O" or c[0] == c[1] == c[2] == "O" or a[0] == b[1] == c[2] =="O" or a[2] == b[1] == c[0] == "O":
            print "End of this happy game"
            print "Unexpected but you won!"
            plw = plw + 1
            repeat = raw_input("Press 'Y' to play again or 'N' to quit! ")
            while not (repeat == "y" or repeat == "Y" or repeat == "n" or repeat == "N"):
                repeat = raw_input("Please press 'Y' or 'N' only!! ")
            if repeat == "y" or repeat == "Y":
                main()
            else:
                return
        elif a[0] != " " and a[1] != " " and a[2] != " " and b[1] != " " and b[2] != " " and  b[0] != " " and c[0] != " "  and c[1] != " " and c[2] != " ":
            print "End of this happy game"
            print "At least you tried...Draw!"
            dr = dr + 1
            repeat = raw_input("Press 'Y' to play again or 'N' to quit! ")
            while not (repeat == "y" or repeat == "Y" or repeat == "n" or repeat == "N"):
                repeat = raw_input("Please press 'Y' or 'N' only!! ")
            if repeat == "y" or repeat == "Y" :
                main()
            else:
                return
        #cpu's turn
        print "Cpu's Turn"
        cpu_row = random.choice([a,b,c])
        cpu_collum = random.choice([0,1,2])
        while cpu_row[cpu_collum] == "O" or cpu_row[cpu_collum] == "X":
            cpu_row=random.choice([a,b,c])
            cpu_collum=random.choice([0,1,2])
        cpu_row[cpu_collum] = "X"
        #show results
        print a
        print b
        print c
        if a[0] == a[1] == a[2] == "X" or a[0] == b[0] == c[0] == "X" or a[1] == b[1] == c[1] == "X" or a[2] == b[2] == c[2] == "X" or b[0] == b[1] == b[2] == "X" or c[0] == c[1] == c[2] == "X" or a[0] == b[1] == c[2] =="X" or a[2] == b[1] == c[0] == "X":
            print "End of this happy game"
            print "You lost from a MACHINE!You should be embarashed!!Cpu Won!"
            cpw = cpw + 1
            repeat = raw_input("Press 'Y' to play again or 'N' to quit! ")
            while not (repeat == "y" or repeat == "Y" or repeat == "n" or repeat == "N"):
                repeat = raw_input("Please press 'Y' or 'N' only!! ")
            if repeat == "y" or repeat == "Y" :
                main()
            else:
                return
        elif a[0] == a[1] == a[2] == b[1] == b[2] == b[0] == c[0] == c[1] == c[2] != " ":
            print "End of this happy game"
            print "At least you tried...Draw!"
            dr = dr + 1
            repeat = raw_input("Press 'Y' to play again or 'N' to quit! ")
            while not (repeat == "y" or repeat == "Y" or repeat == "n" or repeat == "N"):
                repeat = raw_input("Please press 'Y' or 'N' only!! ")
            if repeat == "y" or repeat == "Y" :
                main()
            else:
                return


st = raw_input("Press 'Y' to start the game or 'N' to quit!! ")
while not (st == "y" or st == "Y" or st == "n" or st == "N"):
    st = raw_input("Please press 'Y' or 'N' only!! ")
if st == "y" or st == "Y":
    score = main()
    print "The score is: Player:", plw + dr ,"- Cpu:", cpw + dr
elif st == "n" or st == "N":
    print "Chip-chip-chip you are too afraid!"
    quit = raw_input("Press 'Y' to quit or 'N' if you dare to try! ")
    while not (quit == "Y" or quit == "y" or quit == "n" or quit == "Y"):
        quit = raw_input("Please press 'Y' or 'N' only!! ")
    if quit == "N" or quit == "n":
        score = main()
        print "The score is: Player:", plw + dr ,"- Cpu:", cpw + dr
