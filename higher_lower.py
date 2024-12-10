import random
from art import logo,vs
from game_data import data
score = 0
def formate_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


print(logo)
account_b = random.choice(data)

flags = True
while flags:
    def check_answer(user_guess, a_followers, b_followers):
        if a_followers >b_followers:
            return user_guess == "a"
        else:
            return user_guess == "b"

    account_a = account_b
    account_b = random.choice(data)


    if account_a == account_b:
        account_a = random.choice(data)


    print(f"Compare A : {formate_data(account_a)}")

    print(vs)

    print(f"Campare B : {formate_data(account_b)}")


    guess =  input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = (check_answer(guess, a_followers_count, b_followers_count))
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        flags = False




