class Calculator:
    def __init__(self,num1,num2,):
        self.num1=num1
        self.num2=num2
#hi iam 
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2

Cal=Calculator(3,5)
print(Cal.add())
print(Cal.div())
print(Cal.sub())
print(Cal.mul())
