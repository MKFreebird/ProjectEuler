# Project Euler

#1 Multiples of 3 and 5
def euler1():
    total = 0
    for i in range(1, 1000):
        if (i%3) == 0 or (i%5) == 0:
            total += i
    return total


#2 Even fibonacci numbers
def euler2():
    a = 1
    b = 2
    c = 0
    totalEvenNumbers = 0
    while c < 4000000:
        if (b % 2) == 0:
            totalEvenNumbers += b
        c = a + b
        a = b
        b = c
    return totalEvenNumbers


#6 Sum square difference
def euler6():
    sumSquares = 0
    squareSum = 0
    for i in range(1,101):
        sumSquares += i**2
    for x in range(1,101):
        squareSum += x
    squareSum = squareSum**2
    return squareSum-sumSquares


#8 Largest product in a series
def euler8():
    digit = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    pointer = 0
    highest = 0
    seriesLength = 13
    for x in range(len(digit) - seriesLength):
        serie = []
        for i in range(seriesLength):
            serie.append(int(digit[pointer]))
            pointer += 1
        product = 1
        for number in serie:
            product = product * number
        if product > highest:
            highest = product
        pointer -= (seriesLength - 1)
    return highest


#9 Special Pythagorean triplet
def euler9():
    a = 331
    b = 333
    c = 336
    notFound = True
    while notFound:
        if a + b + c == 1000:
            if (a**2) + (b**2) == c**2:
                print("yolo", a*b*c)
                notFound = False
            else:
                print("helaas", a, b, c)
    return a*b*c

print(euler9())
