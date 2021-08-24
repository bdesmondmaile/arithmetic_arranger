import re
def arithmetic_arranger(problems, totals=False):
    """
    function receives a list of strings that are arithmetic problems and
    returns the problems arranged vertically and side-by-side. The function
    optionally take a second argument. When the second argument is set
    to `True`, the answers are displayed.
    """
    # Use regex to capture different parts of the problem in groups.
    # Grouping parts of the problem will enable easier rearrangement of the problem.
    extractor = re.compile(r'(?P<first_operand>[\w\W]+) (?P<sign>[+-/*]) (?P<last_operand>[\w\W]+)')

    first_operands = []
    second_operands =[]
    width = []
    dash = []
    total = []
    sign = []

    #if there are too many problems (>5) return an error
    if len(problems) > 5:
        return "Error: Too many problems."

    for i in range(len(problems)):
        math_expr = extractor.match(problems[i])

        if math_expr.group() == None:
            pass

        #The appropriate operators the function will accept are **addition** and **subtraction** only. Otherwise return an error
        elif math_expr.group('sign') not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Each number (operand) should only contain digits. Otherwise, the function will return an error.
        elif not math_expr.group('first_operand').isdecimal() or not math_expr.group('last_operand').isdecimal() :
            return "Error: Numbers must only contain digits."

        # Each operand (aka number on each side of the operator) has a max of four digits in width.
        elif len(math_expr.group("first_operand")) > 4 or len(math_expr.group("last_operand")) > 4:
            return "Error: Numbers cannot be more than four digits."

        else:
            width.append(max([len(math_expr.group("first_operand")), \
                len(math_expr.group("last_operand"))]))
            sign.append(math_expr.group('sign'))
            first_operands.append(math_expr.group("first_operand").rjust(width[i] + 2))
            second_operands.append(sign[i] + ' ' + (math_expr.group("last_operand")).rjust(width[i]))

            if math_expr.group('sign') == "+":
                total.append(str(int(math_expr.group("first_operand")) \
                             + int(math_expr.group("last_operand"))).rjust(width[i]+ 2))

            if math_expr.group('sign') == "-":
                total.append(str(int(math_expr.group("first_operand")) \
                                 - int(math_expr.group("last_operand"))).rjust(width[i]+ 2))

    #create dash separators for each problem.
    for i in range(len(width)):
        dash.append('-' * (width[i] + 2))
    
    operand_one = '    '.join(first_operands) + '\n'
    operand_two = '    '.join(second_operands) + '\n'
    dashes = '    '.join(dash)
    summation = '    '.join(total)

    if totals == True:
        arr_prob = operand_one + operand_two + dashes + '\n' + summation
    else:
        arr_prob = operand_one + operand_two + dashes

    return arr_prob