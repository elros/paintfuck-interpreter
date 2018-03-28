from paintfuck.interpreter import Interpreter
from paintfuck.utils import bitfield_to_str


def interpreter(code, iterations, width, height):
    program_output = Interpreter(width, height).run_program(code, iterations)
    return bitfield_to_str(program_output)
