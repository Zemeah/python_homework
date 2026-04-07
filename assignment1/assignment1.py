# Task 1
def hello():
    return("Hello!")

# print(greeting())

# Task 2
def greet(name):
    return f"Hello, {name}!"

# print(greet("Meah"))

# Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
            
    except ZeroDivisionError:
        return "You can't divide by 0!"
    
    except TypeError:
        return "You can't multiply those values!"
            
# print(calc(5,8, "power"))

# Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return "Invalid data type"
            
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

# print(data_type_conversion(123.5, "int"))

# Task 5
def grade(*args):
    try:
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
        
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
    
# print(grade(80,90,10))
    
# Task 6
def repeat(str, count):
    result = ""

    for i in range(count):
        result += str

    return result

# print(repeat("Hello",15))

# Task 7
def student_scores(mode, **kwargs):
    try:
        if mode == "best":
            best_student = None
            highest_score = -1

            for name, score in kwargs.items():
                if score > highest_score:
                    highest_score = score
                    best_student = name

            return best_student
        
        elif mode == "mean":
            total = sum(kwargs.values())
            count = len(kwargs)
            return total / count
        
        else:
         return "Invalid mode"
    
    except (TypeError, ZeroDivisionError):
        return "Invalid data"
    
# print(student_scores("best", Amy=70, Ina=93, Ben=88))
# print(student_scores("mean", Amy=70, Ina=93, Ben=88))
    
# Task 8
def titleize(str):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    words = str.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            words [i] = word.capitalize()

        elif word.lower() in little_words:
            words[i] = word.lower()

        else:
            words[i] = word.capitalize()

    return " ".join(words)

# print(titleize("Johnny had a apple"))

# Task 9
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

# print(hangman("python", "pt"))

# Task 10
def pig_latin(str):
    vowels = "aeiou"
    words = str.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0

            while i < len(word):
                if word[i] in vowels:
                    break
                if word[i:i+2] == "qu":
                    i += 2
                else:
                    i += 1

            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)

# print(pig_latin("quick hello"))

        


        
            