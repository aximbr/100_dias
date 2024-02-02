#Sum of even numbers between 1 100

total = 0
for n in range(1, 101):
    if n%2 == 0:
        total += n
    #end of if
#end of for
        
print(f"The sum of first 100 even number is {total}")
