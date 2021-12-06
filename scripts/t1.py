class A:
    a =2


    def get(self):
        print(self.a)



a = A()
a.a =3
A.a =4
a.get()
print(A().a)

b = A()
b.get()
print(b.a)
