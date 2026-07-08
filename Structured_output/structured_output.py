from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person=Person(name="Ganesh",age="twenty-five")
print("Using typeddict :",new_person)


