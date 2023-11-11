from random import randint, choice

def function_Integer(min, max):
    """
    Random integer.
    """
    return randint(min, max)

# Random number Generator for function A

def function_Operator():
    return choice(['+', '-', '*'])

# Random Math operation selection for function B

def function_Execution(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

# Operation performing

def math_quiz():
    s = 0
    t_q = 3

# Quiz result storing parameters
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_Integer(1, 10)
        n2 = function_Integer(1, 5)
        o = function_Operator()

        PROBLEM, ANSWER = function_Execution(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()