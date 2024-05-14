def Addition(x,y):
    '''
    input: x(float), y(float)
    this funtion performs addition 
    
    '''
    ans = x+y 
    return ans 

def Subtraction(x,y):
    '''
    input: x(float), y(float)
    this function performs Subtration 
    '''
    ans = x-y
    return ans

def Multiplication(x,y):
    '''
    input: x(float), y(float)
    this funcction performs Multiplication
    '''
    ans = x*y
    return ans 

def Division(x,y):
    '''
    input: x(float), y(float)
    this function performs Division
    '''
    ans = x/y
    return ans


def Power(x,y):
    '''
    input: x(float), y(float)
    this function calculates the power.
    '''
    y = int(y)
    if len(str(y)) > 3:
        return "error to calculate"
    ans = x**y
    return ans 

def roots(x,y):
    '''
    input: x(float), y(float)
    this function calculates the rooth of a value 
    this is using the newton rapsons method with bisection search 
    '''
    y = int(y)
    if x < 0  :
        return "plesase enter an non-negative number, no complex values possible "
    if y < 0  :
        return "plesase enter an non-negative number, no complex values possible "
    if len(str(y)) != 1:
        return "please select a one digit root"
   
    epsilon = 0.01
    low = 0
    high = max(1.0,x)
    ans = (high + low) /2
    while abs(ans**y-x) >= epsilon:
        if ans**y < x:
            low = ans 
        else:
            high = ans 
        ans = (high + low)/ 2.0

    return ans  


def input_error_checker(data):
    '''
    input: user data : list 

    this functions checks for input error 
    this function also structutures the data 
    '''
    data_list = data
    value1 = ""
    value2 = ""
    oparator = ""
    value_1_list = []
    value_2_list = []
    oparator_list = []
    temp = ""
    count = 0
    error = False
    for i in data_list:
        if i != " ":
            if i in "0123456789.":
                temp += i
                
            else:
                count +=1
                oparator_list.append(i)
                value_1_list.append(temp)
                temp = ""
    value_2_list.append(temp)

    if len(oparator_list)>1:
        while oparator_list.count("-") >= 1:
            if oparator_list[0] == "-":
                value1=oparator_list[0]
                oparator_list.pop(0)
            
            if oparator_list[len(oparator_list)-1] == "-":
                value2 = oparator_list[len(oparator_list)-1]
                oparator_list.pop(len(oparator_list)-1)
        
    for d in oparator_list:
        oparator += d 
    for b in value_1_list:
        value1 += b
    for c in value_2_list:
        value2 += c
    
    oparator= oparator.lower()
    if oparator not in["root","+","-","/","^","*"]:
        error = True 
         
    return(value1,oparator,value2,error)


def calculator(user_input):
    '''
    input : user data :list
    
    this funtion is the calculator 
    '''
   
    value1,operator,value2,error=input_error_checker(user_input)
    if error:
        return "please give only numerical values and given oparators  "
    
    value1 = float(value1)
    value2 = float(value2)
    if operator == "+":
        ans = Addition(value1,value2)
    if operator == "-":
        ans = Subtraction(value1,value2)
    if operator == "*":
        ans = Multiplication(value1,value2)
    if operator == "/":
        ans = Division(value1,value2)
    if operator == "^":
        ans = Power(value1,value2)
    if operator == "root":
        ans = roots(value1,value2)

    
    return ans 



def run():
    '''
    this function runs the calculator 
    it also adjusts when a previous answer is used 
    '''
    print("welcom to the two value calculator")
    print("_________________________________")
    print("avalible functions: + , - , * , / , ^ , root ")
    count = 0
    while True:
        
        previous_ans=""
        
        user_input = str(input(' plese enter a arthimetic sum :'))
        if count > 0 and user_input.count("ans") == 1 :
            
            previous_ans=str(ans) # storing previous ans 
            user_input = previous_ans + user_input 
            user_input = user_input.replace("ans","") # removing the text "ans"
        ans = calculator(user_input)
        print(ans)
        if type(ans) != str: # checking for errors returned by functions 
            want_to_reapeat = str(input(" do you want to solve more questons? yes/no : "))
            if want_to_reapeat.lower() == "no":
                print("thank you for using the calculator")
                break
            else:
                print(" use 'ans' to use the previous answer.")
        count += 1
        

run()
