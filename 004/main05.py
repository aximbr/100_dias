#Another treasure game
row1 = ["😀", "😃", "😄"]
row2 = ["😡", "🤬", "😠"]
row3 = ["🥶", "😰", "😎"]

map = [row1, row2, row3]

print(f"{row1} \n{row2} \n{row3}")
print(f"Where do you want put the treasure ? ")
xy = input("")

x = int(xy[0])
y = int(xy[1])

map[y-1][x-1] = " X"

print(f"{row1} \n{row2} \n{row3}")

