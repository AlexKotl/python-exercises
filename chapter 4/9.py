def get_odds(last=10):
    number = 0
    while number < last:
        if number % 2 == 0:
            yield number
        number += 1

print(get_odds(10))

n = 1
for number in get_odds(10):
    print("Number", number)
    if n == 3:
        print("Third number is ", number)
    n += 1
