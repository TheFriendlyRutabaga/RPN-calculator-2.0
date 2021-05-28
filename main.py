# author: name here
# date: date here
#
# description: rpn calculator
​
operators = ['+', '-', '*', '/', '^']
​
​
def add(x, y):
    return x + y
​
# Make a helper function for each operation
​
# parameters
#   expression | list | the expression to be calculated
def calculate(expression):
    # while there are tokens to be read
    #   read a token
    stack = []
​
    print(expression)
    for token in expression:
        # if token is an operator, then:
        if token in operators:
            print(f'operator: {token}')
            # pop the top item in the stack and store in variable y
            y = stack.pop()
            # pop the top item in the stack and store in variable x
            x = stack.pop()
​
            print(f'x: {x}')
            print(f'y: {y}')
​
            # evaluate the expression: x token y, and then append the result to the stack
            # x operator y
            # if the _ is an addition sign
            if token == '+':
                result = add(x, y)
                stack.append(result)
            elif token == '-':
                result = x - y
                stack.append(result)
            elif token == '*':
                result = x * y
                stack.append(result)
            # elif token is division
            elif token == '/':
              result = x / y
              stack.append(result)
            # elif token is exponent
            elif token == '^':
              result = x ^ y
              stack.append(result)
​
        # otherwise, its an operand
        else:
            print(f'operand: {token}')
            # append the operand to the stack
            stack.append(float(token))
​
        print(f'stack: {stack}')
​
    # if there is only one item in the stack, then:
        # print the item, this is the result of the expression
​
​
# conversion functions
# str(element) --> returns a copy of the element as a string
# int(element) --> returns a copy of the element as an integer
# float(element) --> returns a copy of the element as a float
# bool(element) --> returns a copy of the element as a bool
​
​
# function
#   main
#       parameters
#           none
#       return value
#           none
#   description: accepts input from the user in the form of a postfix equation
#       computes the equation and prints the result
def main():
    expression = input('>> ')
    calculate(expression.split())
​
​
if __name__ == '__main__':
    main()
