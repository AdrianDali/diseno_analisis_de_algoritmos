class Hash:
    def __init__(self, age, name, size):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        save =  hash((self.age, self.name))




person = Hash(415, 'fresa')
person2 = Hash(520,'manzana')
person3 = Hash(40,'platano')
person4 = Hash(123,"coco")
person5 = Hash(215,"mora")
person6 = Hash(23,"elote")


print(hash(person))
print(hash(person2))
print(hash(person3))
print(hash(person4))
print(hash(person5))