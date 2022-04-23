import random
deck = [["AD",5],["KD",10],["QD",15],["JD",20],["AH",25],
        ["KH",30],["QH",35],["JH",40],["AC",45],["KC",50],
        ["QC",55],["JC",60],["AS",65],["KS",70],["QS",75],["JS",80]]
print(deck)
random.shuffle(deck)
print(deck)
pl_1 = []
pl_2 = []
pl_3 = []
pl_4 = []
for i in range(0,4):
    pl_1.append(deck[i])
for j in range(4,8):
    pl_2.append(deck[j])
for k in range(8,12):
    pl_3.append(deck[k])
for l in range(12,16):
    pl_4.append(deck[i])
print("Player 1 :",pl_1)
print("Player 2 :",pl_2)
print("Player 3 :",pl_3)
print("Player 4 :",pl_4)
while True:
#     count+=1
    print("Round No # 1")
    ope = input("Please select operation: \n1.) Play game \n2.) Exit game")
    if ope == '1':
#         player 1 turn
        print("*************Player 1! Please Select Card *************")
        num = 0
        for i in pl_1:
            num+=1
            print(f"{num}.) {i[0]}")
        select_card = input("Enter Card Number: ")
        if select_card == '1':
            print(f"You Select {pl_1[0][0]} Card")
        elif select_card == '2':
            print(f"You Select {pl_1[1][0]} Card")
        elif select_card == '3':
            print(f"You Select {pl_1[2][0]} Card")
        elif select_card == '4':
            print(f"You Select {pl_1[3][0]} Card")
        else:
            print("Invalid Enter!")
#         player 2 turn
        print("*************Player 2! Please Select Card *************")
        num = 0
        for j in pl_2:
            num+=1
            print(f"{num}.) {j[0]}")
        select_card_2 = input("Enter Card Number: ")
        if select_card_2 == '1':
            print(f"You Select {pl_2[0][0]} Card")
        elif select_card_2 == '2':
            print(f"You Select {pl_2[1][0]} Card")
        elif select_card_2 == '3':
            print(f"You Select {pl_2[2][0]} Card")
        elif select_card_2 == '4':
            print(f"You Select {pl_2[3][0]} Card")
        else:
            print("Invalid Enter!")
#         Condition for checking who player win the match
#         1 card to multiple card
        if select_card == '1' and select_card_2 == '1':
            if pl_1[0][1] > pl_2[0][1]:
                print("player 1 is won the game")
                print(f"{pl_1[0][1]} > {pl_2[0][1]}")
                print(f"{pl_1[0][0]} is value {pl_1[0][1]} > {pl_2[0][0]} is value {pl_2[0][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[0][0]} is value {pl_1[0][1]} > {pl_2[0][0]} is value {pl_2[0][1]}")
                print("out!")
        elif select_card == '1' and select_card_2 == '2':
            if pl_1[0][1] > pl_2[1][1]:
                print("player 1 is won the game")
                print(f"{pl_1[0][1]} > {pl_2[1][1]}")
                print(f"{pl_1[0][0]} is value {pl_1[0][1]} > {pl_2[1][0]} is value {pl_2[1][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[0][0]} is value {pl_1[0][1]} > {pl_2[1][0]} is value {pl_2[1][1]}")
                print("out!")
        elif select_card == '1' and select_card_2 == '3':
            if pl_1[0][1] > pl_2[2][1]:
                print("player 1 is won the game")
                print(f"{pl_1[0][1]} > {pl_2[2][1]}")
                print(f"{pl_1[0][0]} is value {pl_1[0][1]} > {pl_2[2][0]} is value {pl_2[2][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[0][0]} is value {pl_1[0][1]} > {pl_2[2][0]} is value {pl_2[2][1]}")
                print("out!")
        elif select_card == '1' and select_card_2 == '4':
            if pl_1[0][1] > pl_2[3][1]:
                print("player 1 is won the game")
                print(f"{pl_1[0][1]} > {pl_2[3][1]}")
                print(f"{pl_1[0][0]} is value {pl_1[0][1]} > {pl_2[3][0]} is value {pl_2[3][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[0][0]} is value {pl_1[0][1]} > {pl_2[3][0]} is value {pl_2[3][1]}")
                print("out!")
#         else:
#             print("Out of game")
#         2 card to multiple card
        elif select_card == '2' and select_card_2 == '1':
            if pl_1[1][1] > pl_2[0][1]:
                print("player 1 is won the game")
                print(f"{pl_1[1][1]} > {pl_2[0][1]}")
                print(f"{pl_1[1][0]} is value {pl_1[1][1]} > {pl_2[0][0]} is value {pl_2[0][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[1][0]} is value {pl_1[1][1]} > {pl_2[0][0]} is value {pl_2[0][1]}")
                print("out!")
        elif select_card == '2' and select_card_2 == '2':
            if pl_1[1][1] > pl_2[1][1]:
                print("player 1 is won the game")
                print(f"{pl_1[1][1]} > {pl_2[1][1]}")
                print(f"{pl_1[1][0]} is value {pl_1[1][1]} > {pl_2[1][0]} is value {pl_2[1][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[1][0]} is value {pl_1[1][1]} > {pl_2[1][0]} is value {pl_2[1][1]}")
                print("out!")
        elif select_card == '2' and select_card_2 == '3':
            if pl_1[1][1] > pl_2[2][1]:
                print("player 1 is won the game")
                print(f"{pl_1[1][1]} > {pl_2[2][1]}")
                print(f"{pl_1[1][0]} is value {pl_1[1][1]} > {pl_2[2][0]} is value {pl_2[2][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[1][0]} is value {pl_1[1][1]} > {pl_2[2][0]} is value {pl_2[2][1]}")
                print("out!")
        elif select_card == '2' and select_card_2 == '4':
            if pl_1[1][1] > pl_2[3][1]:
                print("player 1 is won the game")
                print(f"{pl_1[1][1]} > {pl_2[3][1]}")
                print(f"{pl_1[1][0]} is value {pl_1[1][1]} > {pl_2[3][0]} is value {pl_2[3][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[1][0]} is value {pl_1[1][1]} > {pl_2[3][0]} is value {pl_2[3][1]}")
                print("out!")
#             print("Out of game")
#         2 card to multiple card
        elif select_card == '3' and select_card_2 == '1':
            if pl_1[2][1] > pl_2[0][1]:
                print("player 1 is won the game")
                print(f"{pl_1[2][1]} > {pl_2[0][1]}")
                print(f"{pl_1[2][0]} is value {pl_1[2][1]} > {pl_2[0][0]} is value {pl_2[0][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[2][0]} is value {pl_1[2][1]} > {pl_2[0][0]} is value {pl_2[0][1]}")
                print("out!")
        elif select_card == '3' and select_card_2 == '2':
            if pl_1[2][1] > pl_2[1][1]:
                print("player 1 is won the game")
                print(f"{pl_1[2][1]} > {pl_2[1][1]}")
                print(f"{pl_1[2][0]} is value {pl_1[2][1]} > {pl_2[1][0]} is value {pl_2[1][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[2][0]} is value {pl_1[2][1]} > {pl_2[1][0]} is value {pl_2[1][1]}")
                print("out!")
        elif select_card == '3' and select_card_2 == '3':
            if pl_1[2][1] > pl_2[2][1]:
                print("player 1 is won the game")
                print(f"{pl_1[2][1]} > {pl_2[2][1]}")
                print(f"{pl_1[2][0]} is value {pl_1[2][1]} > {pl_2[2][0]} is value {pl_2[2][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[2][0]} is value {pl_1[2][1]} > {pl_2[2][0]} is value {pl_2[2][1]}")
                print("out!")
        elif select_card == '3' and select_card_2 == '4':
            if pl_1[2][1] > pl_2[3][1]:
                print("player 1 is won the game")
                print(f"{pl_1[2][1]} > {pl_2[3][1]}")
                print(f"{pl_1[2][0]} is value {pl_1[2][1]} > {pl_2[3][0]} is value {pl_2[3][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[2][0]} is value {pl_1[2][1]} > {pl_2[3][0]} is value {pl_2[3][1]}")
                print("out!")
#             print("Out of game")
#         2 card to multiple card
        elif select_card == '4' and select_card_2 == '1':
            if pl_1[3][1] > pl_2[0][1]:
                print("player 1 is won the game")
                print(f"{pl_1[3][1]} > {pl_2[0][1]}")
                print(f"{pl_1[3][0]} is value {pl_1[3][1]} > {pl_2[0][0]} is value {pl_2[0][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[3][0]} is value {pl_1[3][1]} > {pl_2[0][0]} is value {pl_2[0][1]}")
                print("out!")
        elif select_card == '4' and select_card_2 == '2':
            if pl_1[3][1] > pl_2[1][1]:
                print("player 1 is won the game")
                print(f"{pl_1[3][1]} > {pl_2[1][1]}")
                print(f"{pl_1[3][0]} is value {pl_1[3][1]} > {pl_2[1][0]} is value {pl_2[1][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[3][0]} is value {pl_1[3][1]} > {pl_2[1][0]} is value {pl_2[1][1]}")
                print("out!")
        elif select_card == '4' and select_card_2 == '3':
            if pl_1[3][1] > pl_2[2][1]:
                print("player 1 is won the game")
                print(f"{pl_1[3][1]} > {pl_2[2][1]}")
                print(f"{pl_1[3][0]} is value {pl_1[3][1]} > {pl_2[2][0]} is value {pl_2[2][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[3][0]} is value {pl_1[3][1]} > {pl_2[2][0]} is value {pl_2[2][1]}")
                print("out!")
        elif select_card == '4' and select_card_2 == '4':
            if pl_1[3][1] > pl_2[3][1]:
                print("player 1 is won the game")
                print(f"{pl_1[3][1]} > {pl_2[3][1]}")
                print(f"{pl_1[3][0]} is value {pl_1[3][1]} > {pl_2[3][0]} is value {pl_2[3][1]}")
            else:
                print("player 2 is won the match")
                print(f"{pl_1[3][0]} is value {pl_1[3][1]} > {pl_2[3][0]} is value {pl_2[3][1]}")
                print("out!")

        else:
            print("Out of game")
 

        
        break
    elif ope == '2':
        print("Quit Game!")
        break
    else:
        print("Invalid Enter!")

        break
