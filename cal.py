"""
This module provides a function for calcuating the sum of two numbers.
using click for command line interface.
It also provides functions for subtraction, multiplication, division,
and exponentiation.
"""
import click

def add(a, b):
    """
    Returns the sum of a and b.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b
def subtract(a, b):
    """
    Returns the difference of a and b.
    """
    return a - b
def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b
def divide(a, b):
    """
    Returns the quotient of a and b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def power(a, b):
    """
    Returns a raised to the power of b.
    """
    return a ** b

# build  a command line interface using click

@click.command()
@click.option('--a', prompt='Enter first number', type=float, help='The first number')
@click.option('--b', prompt='Enter second number', type=float, help='The second number')
@click.option('--operation', prompt='Enter operation (add, subtract, multiply, divide, power)', type=click.Choice(['add', 'subtract', 'multiply', 'divide', 'power']), help='The operation to perform')
def cli(a, b, operation):
    """
    Command line interface for the calculator.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    operation (str): The operation to perform.
    """
    if operation == 'add':
        result = add(a, b)
    elif operation == 'subtract':
        result = subtract(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    elif operation == 'divide':
        result = divide(a, b)
    elif operation == 'power':
        result = power(a, b)
    
    click.echo(f'The result of {operation}ing {a} and {b} is {result}')
if __name__ == '__main__':
    cli()
# test the code using pytest    