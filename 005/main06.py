#FizzBuzz game
#if the number is divisible by 3 print fizz
#if the number is divisible by 5 print buzz
#if number is divisibe by 5 and 3 print FizzBuzz

for n in range(1,101):
    if (n % 5 == 0) and (n % 3 == 0):
        print("FizzBuzz")
    elif (n % 3 == 0):
        print("Fizz")
    elif (n % 5 == 0):
        print("Buzz")
    else:
        print(n)
    #end if
#end for