def add(a, b):
    return a+b
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: 0 division in denominator is not possible"
    return a/b
def floor_division(a,b):
    if b==0:
        return "Error: 0 floor division in denominator is not possible"
    return a//b
def exponent(a,b):
    return a**b
def Modulo_remainder(a,b):
    return a%b

def App_calculator():
    print("Welcome to this Simple Calculator")
    print("select Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor_division (//)")
    print("6. Exponent (**)")
    print("7. Modulo_remainder (%)")
    
    choice = input("enter your choice: ")
    if choice in ['1','2','3','4','5','6','7']:
        try:
            number_1 =float(input("Enter first Number: "))
            number_2 = float(input("Enter second number: "))
        except:
            print("Invalid input. Please enter numeric values.")
            return
        if choice == '1':
            print(f"{number_1} + {number_2} = {add(number_1, number_2)}")
        elif choice == '2':
            print(f"{number_1} - {number_2} = {sub(number_1, number_2)}")
        elif choice == '3':
            print(f"{number_1} * {number_2} = {mul(number_1, number_2)}")
        elif choice == '4':
            result = divide(number_1, number_2)
            print(f"{number_1} / {number_2} = {result}")  
        elif choice == '5':
            result = floor_division(number_1, number_2)
            print(f"{number_1} // {number_2} = {result}")      
        elif choice == '6':
            result = exponent(number_1, number_2)
            print(f"{number_1} ** {number_2} = {result}")          
        elif choice == '7':
            result = Modulo_remainder(number_1, number_2)
            print(f"{number_1} % {number_2} = {result}")      
    else:
        print("Invalid Choice.")
if __name__=="__main__":
    App_calculator()