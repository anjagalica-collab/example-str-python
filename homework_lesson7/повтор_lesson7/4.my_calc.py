#Робимо функцію, яка буде реалізовувати калькулятор
def myCalc():
    a=input("Вкажіть значення а: ")
    b= input("вкажіть значення b: ")
    intA=int(a)
    intB= int(b)
    print(f"{a}+{b}={intA+intB}")
    print(f"{a}-{b}={intA-intB}")
    print(f"{a}*{b}={intA*intB}")
    if intB!= 0:
        print(f"{a}/{b}={intA/intB}")
    else:
        print("Не ділимо на 0!")
myCalc()