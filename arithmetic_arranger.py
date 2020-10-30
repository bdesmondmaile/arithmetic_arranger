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
    problem_pattern = re.compile(r'(?P<first_operand>[\w\W]+) (?P<sign>[+-/*]) (?P<last_operand>[\w\W]+)')
    first_operands = ""     # Stores the first operands of the problems in the required format.
    second_operands ="\n"
    dash = "\n"
    sum = "\n"

    #if there are too many problems (>5) return an error
    if len(problems) > 5:
        return "Error: Too many problems."

    for i in range(len(problems)):
        problem = problem_pattern.match(problems[i])
        if problem.group() == None:
            pass
        #The appropriate operators the function will accept are **addition** and **subtraction** only. Otherwise return an error
        elif problem.group('sign') not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        # Each number (operand) should only contain digits. Otherwise, the function will return an error.
        elif not problem.group('first_operand').isdecimal() or not problem.group('last_operand').isdecimal() :
            return "Error: Numbers must only contain digits."
        # Each operand (aka number on each side of the operator) has a max of four digits in width.
        elif len(problem.group("first_operand")) > 4 or len(problem.group("last_operand")) > 4:
            return "Error: Numbers cannot be more than four digits."

        else: # Code below is responsible for rearranging the problem into the required format.
            if i < len(problems)-1: # Problems are separated by 4 spaces, exclude the last item of the list as no trailing white space is required.
                if len(problem.group('first_operand')) == len(problem.group('last_operand')):
                    # ln stores width of the longest operand plus length 2 (for operator and space)
                    #  right justify the operands of the problem at ln.
                    ln = len(problem.group('first_operand')) + 2
                    first_operands += problem.group('first_operand').rjust(ln) + '    '
                    second_operands += (problem.group('sign') +' '+ problem.group('last_operand')).rjust(ln) + '    '
                    dash += ('-' * len(problem.group('first_operand')) + 2*'-').rjust(ln) +'    '
                    if problem.group('sign') == "+":
                        sum += (str(int(problem.group('first_operand')) + int(problem.group('last_operand')))).rjust(ln) +'    '
                    else:
                        sum += (str(int(problem.group('first_operand')) - int(problem.group('last_operand')))).rjust(ln) +'    '

                elif len(problem.group('first_operand')) > len(problem.group('last_operand')):
                    ln = len(problem.group('first_operand')) + 2
                    diff_len = len(problem.group('first_operand')) - len(problem.group('last_operand'))
                    first_operands += problem.group('first_operand').rjust(ln) + '    '
                    second_operands += (problem.group('sign') + ' ' + ' '*(diff_len)+ problem.group('last_operand')).rjust(ln) + '    '
                    dash += ('-' * len(problem.group('first_operand')) + 2*'-').rjust(ln) + '    '
                    if problem.group('sign') == "+":
                        sum += (str(int(problem.group('first_operand')) + int(problem.group('last_operand')))).rjust(ln) +'    '
                    else:
                        sum += (str(int(problem.group('first_operand')) - int(problem.group('last_operand')))).rjust(ln) +'    '

                elif len(problem.group('first_operand')) < len(problem.group('last_operand')):
                    ln = len(problem.group('last_operand')) + 2
                    first_operands += (problem.group('first_operand')).rjust(ln) + '    '
                    second_operands += (problem.group('sign') + ' ' + problem.group('last_operand')).rjust(ln) + '    '
                    dash += ('-' * len(problem.group('last_operand')) + 2*'-').rjust(ln) + '    '
                    if problem.group('sign') == "+":
                        sum += (str(int(problem.group('first_operand')) + int(problem.group('last_operand')))).rjust(ln) +'    '
                    else:
                        sum += (str(int(problem.group('first_operand')) - int(problem.group('last_operand')))).rjust(ln) +'    '

            else: # Remove trailing white space for the last item of the list
                if len(problem.group('first_operand')) == len(problem.group('last_operand')):
                    ln = len(problem.group('first_operand')) + 2
                    first_operands += (problem.group('first_operand')).rjust(ln)
                    second_operands += (problem.group('sign')+' '+problem.group('last_operand')).rjust(ln)
                    dash += ('-' * len(problem.group('first_operand')) + 2*'-').rjust(ln)
                    if problem.group('sign') == "+":
                        sum += (str(int(problem.group('first_operand')) + int(problem.group('last_operand')))).rjust(ln)
                    else:
                        sum += (str(int(problem.group('first_operand')) - int(problem.group('last_operand')))).rjust(ln)

                elif len(problem.group('first_operand')) > len(problem.group('last_operand')):
                    ln = len(problem.group('first_operand')) + 2
                    diff_len = len(problem.group('first_operand')) - len(problem.group('last_operand'))
                    first_operands += (problem.group('first_operand')).rjust(ln)
                    second_operands += (problem.group(2)+ ' ' + ' '*(diff_len)+ problem.group('last_operand')).rjust(ln)
                    dash += ('-' * len(problem.group('first_operand')) + 2*'-').rjust(ln)
                    if problem.group('sign') == "+":
                        sum += (str(int(problem.group('first_operand')) + int(problem.group('last_operand')))).rjust(ln)
                    else:
                        sum += (str(int(problem.group('first_operand')) - int(problem.group('last_operand')))).rjust(ln)

                elif len(problem.group('first_operand')) < len(problem.group('last_operand')):
                    ln = len(problem.group('last_operand')) + 2
                    first_operands += (problem.group('first_operand')).rjust(ln)
                    second_operands += (problem.group(2)+ ' ' + problem.group('last_operand')).rjust(ln)
                    dash += ('-' * len(problem.group('last_operand')) + 2*'-').rjust(ln)
                    if problem.group(2) == "+":
                        sum += (str(int(problem.group('first_operand')) + int(problem.group('last_operand')))).rjust(ln)
                    else:
                        sum += (str(int(problem.group('first_operand')) - int(problem.group('last_operand')))).rjust(ln)

    if totals == True:
        arranged_problems = first_operands + second_operands + dash + sum
    else:
        arranged_problems = first_operands + second_operands + dash

    return arranged_problems
