bob=['Bob Simth',42,30000,'software']
sue=['Sue Jones',45,40000,'hardware']
people=[bob,sue]
for person in people:
    print(person)

pays=[person[2] for person in people]
print(pays)

total=sum(person[2] for person in people)
print(total)

people.append(['Tom',50,0,None])
print(len(people))