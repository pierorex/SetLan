# To set indentation automatically
def indent(level):
    return "    " * level


class Program:
    """A program consists of running a statement"""
    def __init__(self, statement):
        self.statement = statement

    def __str__(self):
        return "Program\n" + self.statement.print_tree(1)


# For inheritance
class Statement: pass


class Assign(Statement):
    """The assign statement"""
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def print_tree(self, level):
        string = indent(level) + "ASSIGN\n" + indent(level + 1)
        string += "variable: " + str(self.variable)
        string += "\n" + indent(level + 1)
        string += "value:\n" + self.expression.print_tree(level + 2)
        return string


class Block(Statement):
    """Block statement, it's just a sequence of statements"""
    def __init__(self, statements):
        self.statements = statements

    def print_tree(self, level):
        string = indent(level) + "BEGIN\n"
        for stat in self.statements:
            string += stat.print_tree(level + 1) + '\n'
            string += indent(level + 1) + "SEPARATOR\n"
        string = string[:(-10 - len(indent(1)))]
        string += "END"
        return string


class Read(Statement):
    """Read statement, for user input"""
    def __init__(self, variable):
        self.variable = variable

    def print_tree(self, level):
        string = indent(level) + "READ\n"
        string += indent(level + 1) + "variable: " + str(self.variable)
        return string


class Print(Statement):
    """Write statement, for printing in standard output"""
    def __init__(self, elements):
        self.elements = elements

    def print_tree(self, level):
        string = indent(level) + "WRITE\n"
        for elem in self.elements:
            string += indent(level + 1) + "element:\n"
            string += elem.print_tree(level + 2) + '\n'
        return string[:-1]


class If(Statement):
    """If statement"""
    def __init__(self, condition, then_st, else_st=None):
        self.condition = condition
        self.then_st = then_st
        self.else_st = else_st

    def print_tree(self, level):
        string = indent(level) + "IF\n"
        string += indent(level + 1) + "condition:\n"
        string += self.condition.print_tree(level + 2) + '\n'
        string += indent(level + 1) + "then:\n"
        string += self.then_st.print_tree(level + 2)
        if self.else_st:
            string += '\n' + indent(level + 1) + "else:\n"
            string += self.else_st.print_tree(level + 2)
        return string


class For(Statement):
    """For statement, works in ranges"""
    def __init__(self, variable, in_range, statement):
        self.variable = variable
        self.in_range = in_range
        self.statement = statement

    def print_tree(self, level):
        string = indent(level) + "FOR\n"
        string += indent(level + 1) + "variable: " + str(self.variable) + '\n'
        string += indent(level + 1) + "IN:\n"
        string += self.in_range.print_tree(level + 2) + '\n'
        string += indent(level + 1) + "DO statement:\n"
        string += self.statement.print_tree(level + 2)
        return string


class Repeat(Statement):
    """While statement, takes a condition"""
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement

    def print_tree(self, level):
        string = indent(level) + "Repeat\n"
        string += indent(level + 1) + "condition:\n"
        string += self.condition.print_tree(level + 2) + '\n'
        string += indent(level + 1) + "DO statement:\n"
        string += self.statement.print_tree(level + 2)
        return string


# For inheritance
class Expression: pass


class Variable(Expression):
    """Class to define a variable"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def print_tree(self, level):
        return indent(level) + "VARIABLE: " + str(self.name)


class Int(Expression):
    """Class to define an expression of int"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def print_tree(self, level):
        return indent(level) + "INT: " + str(self.value)


class Bool(Expression):
    """Class to define an expression of bool"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def print_tree(self, level):
        return indent(level) + "BOOL: " + str(self.value)


class String(Expression):
    """Class to define an expression of a printable string"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def print_tree(self, level):
        return indent(level) + "STRING: " + str(self.value)


class Binary(Expression):
    """Binary expressions"""
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def print_tree(self, level):
        string = indent(level) + "BINARY:\n" + indent(level + 1)
        string += "operator: " + self.operator + '\n'
        string += indent(level + 1) + "left operand:\n"
        string += self.left.print_tree(level + 2) + '\n'
        string += indent(level + 1) + "right operand:\n"
        string += self.right.print_tree(level + 2)
        return string


class Unary(Expression):
    """Unary expressions"""
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def print_tree(self, level):
        string = indent(level) + "UNARY:\n" + indent(level + 1) + "operator: "
        string += str(self.operator) + '\n'
        string += indent(level + 1) + "operand:\n"
        string += self.operand.print_tree(level + 2)
        return string
