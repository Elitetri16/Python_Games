q1 = """ Q1) Who is the ramen lover ninja to later became the 7th Hoakge?
a.Naruto
b.Kakashi
c.Tsunade
d.Hinata
"""
q2 = """ Q2) Who am I? - "After discovering the Death Note, I decided to use it to rid the world of criminals.
 My killings are eventually labelled by the people living in Japan as the work of "Kira.

 a.Kira
 b.Light Yagami
 c.L
 d.Misa
"""
q3 = """Q3) I am Studio Ghibli’s well-known mascot - Who am I?
 a.Kiki
 b.Bakura
 c.Ponyo
 d.Totoro
"""

q4 = """ Q4) Yubaba is a witch in which animated film written and directed by Hayao Miyazaki?
 a.Castle in the Sky
 b.Ocean Waves
 c.Pom Poko
 d.Spirited Away
"""

q5 = """ Q5) Which anime series is set in the dark underworld of Victorian London?
 a.Phantomhive
 b.Black Butler
 c.Valkyria Chronicles
 d.Blue Exorcist
"""
questions = {q1: "a", q2: "b", q3: "d", q4: "d", q5: "b"}

name = input("Enter Your Name:")
print("Hi!!", name, "Welcome to Anime Quiz!")
print(
    "Before we start here are some rules - For each correct answer +1 Point will be awarded and for each Incorrect answer -1 will be awarded")
print("Lets Start!")
score = 0
for i in questions:
    print(i)
    flag1 = input("Wanna skip this question? (yes/no)")
    if flag1 == "yes":
        continue
    ans = input("Enter the answer (a/b/c/d):")
    if ans == questions[i]:
        print("Correct! +1 Point")
        score = score + 1
    else:
        print("Incorrect Answer -1 Point")
        score = score - 1

    flag2 = input("Wanna quit the quiz? (yes/no)")
    if flag2 == "yes":
        break

print("Well Done! You scored:", score)
