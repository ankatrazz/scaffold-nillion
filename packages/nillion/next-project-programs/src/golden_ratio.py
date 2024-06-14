from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")

    # Initialize the first two Fibonacci numbers as secret integers
    fib1 = SecretInteger(Input(name="fib1", party=party1))
    fib2 = SecretInteger(Input(name="fib2", party=party1))
    
    # Number of iterations to approximate the golden ratio
    iterations = 10

    for _ in range(iterations):
        next_fib = fib1 + fib2
        fib1 = fib2
        fib2 = next_fib

    # Compute the ratio of the last two Fibonacci numbers
    golden_ratio = fib2 / fib1

    # Return the golden ratio as the output
    return [Output(golden_ratio, "golden_ratio", party1)]
