#Calculate number of cans to pint an wall give the height and width
import math
def paint_calc(height, width, cover):
    can = math.ceil(height*width/cover)
    print(f"The number of can to this wall is {can}")


test_h = int(input("Enter the height of wall : "))
test_w = int(input("Enter the width of wall : "))
coverage = 5
test_c = int(input("Enter the coverage of each can : "))
paint_calc(height = test_h, width = test_w, cover = coverage)

