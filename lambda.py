people = [{"name":"Harry", "house":"Griffindor"},{"name":"Cho","house":"Ravenclaw"},{"name":"Draco","house":"Slytherin"}]

def f(person):
    return(person["name"])

people.sort(key=f)   #function returns what to sort by

print(people)

people.sort(key = lambda person:person["house"])   #can use lambda function to define a quick one line function

print(people)