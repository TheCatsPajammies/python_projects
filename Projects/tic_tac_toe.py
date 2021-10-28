cells = str(input("Enter cells:"))

row_1 = " " + cells[0] + " " + cells[1] + " " + cells[2] + " "
row_2 = " " + cells[3] + " " + cells[4] + " " + cells[5] + " "
row_3 = " " + cells[6] + " " + cells[7] + " " + cells[8] + " "

field = "---------\n|{}|\n|{}|\n|{}|\n---------".format(row_1, row_2, row_3)

print(field)

incom = [cell for cell in cells if cell == '_' or cell == " "]
cross = [cell for cell in cells if cell == 'X']
circle = [cell for cell in cells if cell == 'O']

turns = abs((len(cross)) - len(circle))

wins = [cells[:3], cells[3:6], cells[6:9], cells[0:7:3], cells[1:8:3], cells[2:9:3], cells[2:7:2], cells[0:9:4]]

cross_win = 'XXX'
circle_win = 'OOO'

if cross_win in wins and circle_win in wins or turns >= 2:
    print('Impossible')
elif cross_win in wins:
    print('X wins')
elif circle_win in wins:
    print('O wins')
elif "_" in incom or " " in incom:
    print('Game not finished')
else:
    print('Draw')










    






# wins == cells[0] cells[1] cells[2]
#         cells[3] cells[4] cells[5]
#         cells[6] cells[7] cells[8]
#         cells[0] cells[3] cells[6]
#         cells[1] cells[4] cells[7]
#         cells[2] cells[5] cells[8]
#         cells[0] cells[4] cells[8]
#         cells[2] cells[4] cells[6]