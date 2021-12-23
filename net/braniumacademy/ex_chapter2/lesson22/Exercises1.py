a_str, op, b_str = input().split()
a = float(a_str)
b = float(b_str)

match op:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} =  {a * b}")
    case "/":
        if b == 0.0:
            print("ERROR")
        else:
            print(f"{a} / {b} = {a / b}")
