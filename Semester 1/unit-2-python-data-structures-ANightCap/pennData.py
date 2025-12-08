import pandas as pd
import random

#fNames = ["Mac", "Danielle", "Aiden", "Ben", "Van", "Kaden", "Lucian", "Andrew", "Benedict", "Keaton", "Joe", "Noah", "Roman", "Kyan", "Elijah", "Alexis", "Katerina", "Jill", "Jane", "Emmy", "Emma", "Eliana", "Rachel", "Marge", "Lisa" ]
fNames = ["Joe", "Kelsey", "Abby", "Azria", "Alice", "Avery", "Emm", "Gavin", "Sujay", "Vihaan", "Manny", "Josh", "Sam", "Dutch", "Cal", "Nate"]
lNames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
years = ["Freshman", "Sophomore", "Junior", "Senior"]
pathways = ["Early College", "Engineering", "Computer Science", "Business", "Marketing", "Early Childhood Education", "Culinary", "Criminal Justice", "Construction", "Bio Med"]
names = []

for i in range(20000):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.4),2) for _ in names],
    "Sports_Played": [random.randint(0, 3) for _ in names],
    "Credits_Completed": [random.randint(0, 60) for _ in names],
    "Major": [random.choice(pathways) for _ in names],
    "Year": [random.choice(years) for _ in names],
}

pennData = pd.DataFrame(data)

pennData.to_csv("pennDataB320k.csv", index=False)