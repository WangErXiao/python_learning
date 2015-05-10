bob=['Bob Simth',42,30000,'software']
sue=['Sue Jones',45,40000,'hardware']
NAME,AGE,PAY=range(3)
print bob[NAME]," , ",sue[NAME]

bob=[['name','Bob Smith'],['age',10],['pay',10000]]
sue=[['name','Sue Jones'],['age',12],['pay',20000]]

people=[bob,sue]
for person in people:
    print person[0][1] , " : ", person[2][1]


for person in people:
    for (name,value) in person:
        if name == 'name': print(value)


def field(record,label):
    for(fname,fvalue) in record:
        if fname==label:
            return fvalue

for rec in people:
    print(field(rec,'name'),field(rec,'age'),field(rec,'pay'))







