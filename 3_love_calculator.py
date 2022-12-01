# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
l_name1 = name1.lower()
l_name2 = name2.lower()

true_count = (l_name1.count("t") + l_name2.count("t")) + (l_name1.count("r") + l_name2.count("r")) + (l_name1.count("u") + l_name2.count("u")) + (l_name1.count("e") + l_name2.count("e"))

love_count = (l_name1.count("l") + l_name2.count("l"))+ (l_name1.count("o") + l_name2.count("o")) + (l_name1.count("v") + l_name2.count("v")) + (l_name1.count("e") + l_name2.count("e"))

s_score = str(true_count) + str(love_count)
love_score = int(s_score)

if love_score < 10:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")





