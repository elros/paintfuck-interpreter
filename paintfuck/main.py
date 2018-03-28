from paintfuck.interpreter import Interpreter


def interpreter(code, iterations, width, height):
    return Interpreter(width, height).run_program(code, iterations)
