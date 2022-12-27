print("Welcome to the computer quiz! There are 10 question. You have to complete it in 2 minutes.")

play = input('Do you want to play? ').lower()
if play == "yes":
    print("Alright. Let the quiz begin :)")
else:
    print("Okay :(")
    quit()

score = 0

answer1 = input("1. What does CPU stand for?\n Type in your answer: ").lower()
if answer1 == "central processing unit":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer2 = input("2. What does RAM stand for?\n Type in your answer: ").lower()
if answer2 == "random access memory":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer3 = input("3. What does ROM stand for?\n Type in your answer: ").lower()
if answer3 == "read only memory":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer4 = input("4. What does GPU stand for?\n Type in your answer: ").lower()
if answer4 == "graphics processing unit":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer5 = input("5. Who was the first computer programmer?\n Type in your answer: ").lower()
if answer5 == "ada lovelace":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer6 = input("6. Who was the first computer scientist?\n Type in your answer: ").lower()
if answer6 == "charles babbage":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer7 = input("7. Who decoded the encrption of the German Enigma machine during world war II?\n Type in your answer: ").lower()
if answer7 == "alan turing":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer8 = input("8. What stands for specs?\n Type in your answer: ").lower()
if answer8 == "specifications":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer9 = input("9. What stands for lan?\n Type in your answer: ").lower()
if answer9 == "local area network":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

answer10 = input("10. What stands for wan? ").lower()
if answer10 == "wide area network":
    print(" Correct!")
    score += 1
else:
    print(" Incorrect.")

print ("You got " + str(score) + " out of 10 questions correct!")
print ("You got " + str(int(score/10*100)) + "% " "out of 100%.")

if score >= 8:
    print("Excellent Job! :)")
elif score >= 6:
    print("Good Job!")
else:
    print("Try again.")