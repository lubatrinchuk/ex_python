class Mother:
    def __str__(self):
        return "mother"

class Daughter(Mother):
    def __str__(self):
        return "daugther"

a = Mother()
b = Daughter()

print(a)
print(b)