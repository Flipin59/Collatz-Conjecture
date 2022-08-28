print("Collatz's Conjecture")
a = int(input("Enter a Number ")) #Input
b = a #Variable assigned for sum of all numbers that are generated
if a <= 0:
    print("Collatz's conjecture isnt applicable")
while a > 0:
    print(a)
    if a %2 ==0 :
        a = a/2
    elif a%2 != 0 :
        a = 3*a + 1
    b += a
    if a == 1:
        print(a)
        print("Sum", b)
    
        break
    
    
    
