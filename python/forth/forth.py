class StackUnderflowError(Exception):
    pass


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def evaluate(input_data):
    defines = {}
    if not input_data:
        return []
    while input_data[0][:1] == ':':
        values = input_data.pop(0).split()[1:-1]
        key = values.pop(0).lower()
        if is_integer(key):
            raise ValueError('cannot redefine numbers')
        defines[key] = values
    stack = []
    input_data = input_data[-1].split()
    while any(input_data):
        word = input_data.pop(0).lower()
        try:
            if is_integer(word):
                stack.append(int(word))
            elif word in defines:
                input_data = defines[word] + input_data
            elif word == '+':
                stack.append(stack.pop() + stack.pop())
            elif word == '-':
                stack.append(-stack.pop() + stack.pop())
            elif word == '*':
                stack.append(stack.pop() * stack.pop())
            elif word == '/':
                divider = stack.pop()
                if divider == 0:
                    raise ZeroDivisionError('cannot divide by zero')
                stack.append(int(stack.pop() / divider))
            elif word == 'dup':
                stack.append(stack[-1])
            elif word == 'drop':
                stack.pop()
            elif word == 'swap':
                stack.append(stack[-2])
                del stack[-3]
            elif word == 'over':
                stack.append(stack[-2])
            else:
                raise ValueError('unknown word ' + word)
        except ZeroDivisionError:
            raise
        except IndexError:
            raise StackUnderflowError('not enough values for ' + word)
    return stack
