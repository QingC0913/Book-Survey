import json

lofAnswers = []
previous = []

questions=["What is your name?", "How old are you?", "What is your favorite book genre?", "Who is your favorite author?", "Do you like books that have female protagonist?",
"Do you read books outside of school?" ]
keys = ['name', 'age', 'genre', 'author', 'fprotagonist', 'outofschool']

start = input("Do you want to take this survey?")
while start == "yes" or start == "Yes":
    survey = {}
    for i in range(len(questions)):
        answer = input(questions[i])
        survey[keys[i]] = answer
    lofAnswers.append(survey)
    start = input("Do you want to take this survey?")

print ("Thanks for your time! Bye!")

with open("saveSurvey.json") as storageFile:
    previous = json.load(storageFile)
lofAnswers = previous + lofAnswers;
with open("saveSurvey.json", "w") as outFile:
    json.dump(lofAnswers, outFile)
