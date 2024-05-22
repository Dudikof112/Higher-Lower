import art
import functions

print(art.logo)

score = 0
flag = True

index_A = functions.index()

while flag:

    if score > 0:
        print(f"You're right! Current score: {score}")

    functions.compare(index_A, def_i='A')

    print(art.vs)

    index_B = functions.index()
    functions.compare(index_B, def_i='B')

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if answer == 'A':
        flag = functions.compare_followers(index_A, index_B)

        if flag:
            score += 1

    elif answer == 'B':
        flag = functions.compare_followers(index_B, index_A)

        if flag:
            score += 1

    print("\n")

    index_A = index_B

print(F"Sorry, that's wrong. Your score is {score}")
