x: float
oper: str
y: float
result: float
memory: float = 0.0
msg_0: str = "Enter an equation"
msg_1: str = "Do you even know what numbers are? Stay focused!"
msg_2: str = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3: str = "Yeah... division by zero. Smart move..."
msg_4: str = "Do you want to store the result? (y / n):"
msg_5: str = "Do you want to continue calculations? (y / n):"
msg_6: str = " ... lazy"
msg_7: str = " ... very lazy"
msg_8: str = " ... very, very lazy"
msg_9: str = "You are"
msg_10: str = "Are you sure? It is only one digit! (y / n)"
msg_11: str = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12: str = "Last chance! Do you really want to embarrass yourself? (y / n)"


def main():
    global x, oper, y, result
    operations: list = ['+', '-', '*', '/']
    calc: str = input(msg_0)
    x = calc.split()[0]
    oper = calc.split()[1]
    y = calc.split()[2]
    if x == 'M':
        x = float(memory)
    if y == 'M':
        y = float(memory)
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        main()
    else:
        if oper not in operations:
            print(msg_2)
            main()
        else:
            check(x, y, oper)
            if oper == '+':
                result = x + y
                flow_2()
            elif oper == '-':
                result = x - y
                flow_2()
            elif oper == '*':
                result = x * y
                flow_2()
            elif oper == '/' and y != 0:
                result = x / y
                flow_2()
            else:
                print(msg_3)
                main()


def flow_2():
    global memory
    print(result)
    answer: str = input(msg_4)
    if answer == 'y':
        flow_4()
        flow_3()
    elif answer == 'n':
        flow_3()
    else:
        flow_2()


def flow_3():
    answer: str = input(msg_5)
    if answer == 'y':
        main()
    elif answer != 'n':
        flow_3()


def check(v1: float, v2: float, v3: str):
    msg: str = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg:
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v: float) -> bool:
    return -10 < v < 10 and v.is_integer()


def flow_4():
    global memory
    if is_one_digit(result):
        msg_index: int = 10

        def lookup_response(id: int) -> str:
            if id == 10:
                return msg_10
            elif id == 11:
                return msg_11
            else:
                return msg_12

        def loop(msg_index):
            global memory
            answer: str = input(lookup_response(msg_index))
            if answer == 'y':
                if msg_index > 11:
                    memory = result
                else:
                    msg_index += 1
                    loop(msg_index)
            elif answer != 'n':
                loop(msg_index)

        loop(msg_index)
    else:
        memory = result


main()
