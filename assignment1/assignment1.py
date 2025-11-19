# Write your code here.
# Task 1: Hello

def hello():
    return "Hello!"
    
hello()

# Task 2: Greet with a Formatted String

def greet(name):
    return("Hello, " + name + "!")
    
greet("Steve")

# Task 3: Calculator

def calc(a,b,operation="multiply"):  
    try:
       float(a)
       float(b)
    except ValueError:
       return "You can't multiply those values!"
    try:
        match operation:
            case "add":
                return a + b           
            case "subtract":
                return a - b         
            case "divide":
                return a / b       
            case "multiply":
                return a * b           
            case "power":
                return a ** b         
            case "int_divide":
                return a // b        
            case "modulo":
                return a % b           
            case _:
                return "error"
    except ValueError:
        return "You can't multiply those values!"
    except ZeroDivisionError:
        return "You can't divide by 0!"    

print(calc(12.6,"create","divide"))

# Task 4: Data Type Conversion

def data_type_conversion(value,type):
    try:
        match type:
            case "int":
                return int(value)
            case "str":
                return str(value)
            case "float":
                return float(value)
            case _:
                return "enter correct Data Type as in code"
    except ValueError:
        return "You can't convert " + value + " into a " + type + "."

print(data_type_conversion("banana", "int"))


# Task 5: Grading System, Using *args

def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"        
    except:
        return "Invalid data was provided."
    
print(grade(10,90,44,78,98,"mice"))

# Task 6: Use a For Loop with a Range

def repeat(string,count):
    res = ""
    for i in range(count):
        res = res + string
    return res
print(repeat("high",4))

# Task 7: Student Scores, Using **kwargs

def student_scores(*args,**kwargs):
    if "mean" in args:   
        for key, value in kwargs.items():
            return sum(kwargs.values()) / len(kwargs)
    elif "best" in args:
        best_key = ""
        best_value = ""
        for key, value in kwargs.items():
            if best_value == "" or value > best_value:
                best_value = value
                best_key = key
        return best_key
    else:
        return "define the operations"     

print(student_scores("best", Tom=75, Dick=80, Angela=97.999, Kot=97))

# Task 8: Titleize, with String and List Operations

def titleize(str):
    words = str.split()
    little_word = {"a", "on", "an", "the", "of", "and", "is", "in"}
    result = ""
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            formatted_word = word.capitalize()
        elif word in little_word:
            formatted_word = word
        else:
            formatted_word = word.capitalize()
        if i > 0:
            result += " " + formatted_word
        else:
            result += formatted_word
            

    return result
print(titleize("after on"))

# Task 9: Hangman

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
print(hangman("dashboard","ab"))

# Task 10: Pig Latin

def pig_latin(str):
    words = str.split()
    vowel = "aeiou"
    result = []
    for word in words:
        if word[0] in vowel:
            result.append(word + "ay")
            continue
        else:
            index = 0
            while index < len(word) and word[index] not in vowel:
                if index < len(word) - 1 and word[index] == "q" and word[index + 1] == "u":
                    index += 2
                    break
                index += 1
            result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)

print(pig_latin("square box"))
    
