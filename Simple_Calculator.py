print("-------------------- CALCULATOR --------------------")

def operation():
    while(True):
        operator = input("Enter a operator (+,-,*,/) = ")
        if operator in ['+','-','*','/']:
            return operator 
        else: 
            print("Invalid!, Please enter valid Operator.\n")
        
def calculate(num1,operator,num2):
    if   operator == '+': return (num1+num2)
    elif operator == '-': return (num1-num2)
    elif operator == '*': return (num1*num2)
    elif operator == '/': 
        if num2==0:
            raise ZeroDivisionError
        else : return (num1/num2)
        
while (True):
    print("\nAddition       (+) \nSubtraction    (-) \nMultiplication (*) \nDivision       (/) \n")
    first_var = eval(input("Enter First Number = "))
    operator = operation()
    second_var = eval(input("Enter Second Number = "))
    
    try:
        answer = calculate(first_var,operator,second_var)
        print(f"\nThe Result of {first_var} {operator} {second_var} = {answer}\n")
    except ZeroDivisionError:
        print("\nSorry!, Cannot Divide by Zero.\n")
    except Exception:
        print("\nSorry!, An Error Occured.\n")
    
    ask = input("Do you want to Perform another Caculation? (yes/no):").strip().lower()
    if (ask!="yes"): 
        print("Thank You!.") 
        break
