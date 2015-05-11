from chapter01.person import Person

class Manager(Person):
    def giveRaise(self,percent,bonus=01.):
        self.pay*=(1.0+percent+bonus)


if __name__=='__main__':
    tom=Manager(name='Tom Doe',age=42,pay=10000)
    tom.giveRaise(0.2)
    print(tom.pay)