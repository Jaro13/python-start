def factorial(n):
    if n>=1:
         print "wykonano operacje",n
         return n * factorial(n-1)
    else:
         return 1


# jak znajezc koncowy element oraz wtedy wydrukowac napis wynik koncowy
# print "wynik koncowy", factorial(2)
print factorial(23)
