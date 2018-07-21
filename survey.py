import os

file1 = open("radishsurvey.txt", "r")

content = file1.readlines()

file1.close()

rad_survey = {}

for line in content:
    name,variety = line.split(" - ")
    variety = variety.strip()
    if variety not in rad_survey:
        rad_survey[variety] = 1
    else:
        rad_survey[variety] += 1
print(rad_survey)

popular = []

maxvote = 0

for variety,count in rad_survey.items():
    if count > maxvote:
        maxvote = count
        popular = []
        popular.append(variety)
    elif count == maxvote:
        popular.append(variety)

print("most popular variety is %s" % (str(popular)))

minv = max(rad_survey.values())

unpopular = []

for variety,count in rad_survey.items():
    if count < minv:
        minv = count
        unpopular = []
        unpopular.append(variety)
    elif count == minv:
        unpopular.append(variety)

print("The least popular variety is %s" % (unpopular))

voter_list ={}

for line in content:
    name,variety = line.split(" - ")
    name = name.strip()
    if name not in voter_list:
        voter_list[name] = 1
    else:
        voter_list[name] += 1

print(voter_list)

if max(voter_list.values()) > 1:
    print("Someone has voted twice!")
else:
    print("Everyone has voted once!")


