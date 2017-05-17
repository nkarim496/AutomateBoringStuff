# The Collatz Sequence
def collatz(number):
    return number // 2 if number % 2 == 0 else 3 * number + 1

while True:
    try:
        UserNumber = int(input('Give me an integer number: '))
        break
    except ValueError:
        print('There must be an integer')

while UserNumber != 1:
    UserNumber = collatz(UserNumber)
    print(UserNumber, end=' ')
