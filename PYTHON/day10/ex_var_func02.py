persons=['hong']
year=2024

def add_person(name):
    persons.append(name)

def remove_person(name):
    persons.remove(name)

print(f'persons: {persons}')
add_person('park')
print(f'persons: {persons}')

persons=['hong']
year=2024

def add_person(name):
    persons.append(name)
    year+=1

def remove_person(name):
    persons.remove(name)

print(f'persons: {persons}')
add_person('park')
print(f'persons: {persons}')

persons=['hong']
year=2024

def add_person(name):
    global year
    persons.append(name)
    year+=1

def remove_person(name):
    persons.remove(name)

print(f'persons: {persons}')
add_person('park')
print(f'persons: {persons}')

persons=['hong']
year=2024
gender={'h':'남자'}

def add_person(name):
    global year
    persons.append(name)
    year+=1
    gender[name]='여'

def remove_person(name):
    persons.remove(name)
    gender.pop(name)

print(f'persons: {persons}')
print(f'gender:{gender}')
add_person('park')
print(f'persons: {persons}')
print(f'gender:{gender}')

remove_person('park')
print(f'persons: {persons}')
print(f'gender:{gender}')