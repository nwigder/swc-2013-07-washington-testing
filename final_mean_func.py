def mean(numlist):
    '''this is the docstring'''
    try:
        length = len(numlist)
    except:
        raise TypeError("numlist does not support method 'len'")
        
    try:
        total = sum(numlist)
    except TypeError:
        raise TypeError("The number list was not a list of numbers.")

    try:
        answer = float(total)/length
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
          
 
    return answer

def main():
    assert mean([1, 2, 3]) == 2

if __name__ == "__main__":
    main()

