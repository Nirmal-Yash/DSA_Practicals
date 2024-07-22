precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
operator_stack = []
def infix_to_postfix(infix_expression):
    postfix_expression = []


    for i in infix_expression.split():
        if i.isalnum():
            postfix_expression.append(i)
        elif i == '(':
            operator_stack.append(i)
        elif i == ')':
            while operator_stack[-1] != '(':
                postfix_expression.append(operator_stack.pop())
            operator_stack.pop()  # Remove the '('
        else:
            while (operator_stack and
                   operator_stack[-1] != '(' and
                   precedence[operator_stack[-1]] >= precedence[i]):
                postfix_expression.append(operator_stack.pop())
            operator_stack.append(i)

    while operator_stack:
        postfix_expression.append(operator_stack.pop())

    return ' '.join(postfix_expression)

infix_expression = "A + B * C - D"
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix: {infix_expression}")
print(f"Postfix: {postfix_expression}")
