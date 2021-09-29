# Ryan Lugo: RJL 9/28/21

card_one = input("What is your first cards points?: ")
card_two = input("What is your second card points?: ")

card_value = int(card_one) + int(card_two)

if card_value < 21:
    print("You are safe!")
else:
    print("You are not safe.")