import random

print("Welcome to the Quiz")
print("Please spell your words carefully as we are very good in English!!")

rows = 10

k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("        * ", end="")
    print("")

k = rows - 2

for i in range(rows, -1, -1):

    for j in range(k, 0, -1):
        print(end=" ")

    k = k + 1

    for j in range(0, i + 1):
        print("        * ", end="")
    print("")
points = 0

name = input("Enter yor name")

question = ["Who is the Current CM of Sikkim?", "Sikkim became the 22nd state of the Indian Union in the year?"]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == "Who is the Current CM of Sikkim?":

    if ans.lower() == "prem singh tamang":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:
    if ans == '1975':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")

'''................................................Round - 2.........................................................'''
question = [" Who is the Current Chief Justices of Sikkim", "Sikkim is the large exporter of"]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == " Who is the Current Chief Justices of Sikkim":

    if ans.lower() == "arup kumar goswami":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == 'cardamom':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")

'''........................................Round - 3...........................................................'''
question = ["In which year, the indo-sikkimese Treaty was signed?", "Which is the highest point in Sikkim?"]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == "In which year, the indo-sikkimese Treaty was signed?":

    if ans.lower() == "1950":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == 'kanchenjunga':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")

'''....................................Round - 4...................................................................'''
question = ["The Nathu La pass connects India with?", "Which dynasty ruled Sikkim in 1642-1975?"]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == "The Nathu La pass connects India with?":

    if ans.lower() == "china":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == 'namgyal':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")
".......................................Round 5...................................................................."
question = ["Which is the Sikkim state Animal ?", "Which is the Sikkim state Flower?"]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == "Which is the Sikkim state Animal ?":

    if ans.lower() == "red panda":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == 'noble orchid':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")

"Round 6"
question = ["Which is the Sikkim state Bird?", "Sikkim is known as ________ in the Tibetan regions"]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == "Which is the Sikkim state Bird?":

    if ans.lower() == "blood pheasant":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == 'densong':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")

"........................................Round-7.................................................................."
question = ["Upon reaching Bangladesh, the Teesta river joins with",
            "Name the one and only National Park in Sikkim."]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == "Upon reaching Bangladesh, the Teesta river joins with":

    if ans.lower() == "brahmaputra river":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == 'khangchendzonga national park':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")
"....................................................Round-8...................................................."
question = ["The major festival of Sikkim is?", "Name a Bio-diversity hotspot in Sikkim."]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == "The major festival of Sikkim is?":

    if ans.lower() == "Saga Dawa Festival":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == 'eastern himalayas':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")
".....................................................Round-9........................................................"
question = ["The dance form, performed by Buddhists during the Losar (New year) festival is?",
            "How many districts are there in Sikkim?     (write in characters please)"]
z = random.choice(question)
print(z)

ans = input("Enter the Answer :- ")
if z == "The dance form, performed by Buddhists during the Losar (New year) festival is?":

    if ans.lower() == "gumpa":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == 'four':
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")
"..............................................Round 10..........................................................."
question = ["The earliest inhabitants of Sikkim was ____. ", "The fastest flowing river in India."]
z = random.choice(question)
print(z)
ans = input("Enter the Answer :- ")
if z == "The earliest inhabitants of Sikkim was ____. ":

    if ans.lower() == "lepchas":
        print("Correct Answer")
        points += 10
    else:

        print("wrong answer")

else:

    if ans.lower() == "tista":
        print("Correct Answer")
        points += 10
    else:
        print("Wrong Answer")

print("Total points is :- ", points)

Author = "Pranshu Raj"

file = open("highscore.txt", "a")
data = [name, points]
a = file.write(str(data))
file.close()
while True:
    continue
