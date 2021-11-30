class Base:
    def get(self):
        print(123)


class Dog(Base):
    cat = 1

    def get(self):
        if self.cat == 1:
            return 2
        else:
            # print(self.cat)
            return 'cat' + str(self.cat)


res = Dog().get()
print(res)

print(Dog.cat)
