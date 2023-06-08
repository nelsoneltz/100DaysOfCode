row1 = ['⬜','⬜','⬜']
row2 = ['⬜','⬜','⬜']
row3 = ['⬜','⬜','⬜']
map = [row1,row2,row3]

print(f'{row1}\n{row2}\n{row3}')

position = input("Where do you want to hide your treasure? ")
x = int(position[0]) - 1 
y = int(position[1]) - 1

map[x][y] = 'X'
print(f'{row1}\n{row2}\n{row3}')