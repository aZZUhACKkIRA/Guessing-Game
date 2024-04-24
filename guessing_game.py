print("Made by Gh05t 3Y3(aZZUhACKkIRA)")
secret_number = 4
counts = 0
limit = 3
while counts < limit:
    guess = int(input("Guess: "))
    counts += 1
    if guess == secret_number:
        print("Congratulations!!! You won!")
        break
else:
    print("Better luck next time")