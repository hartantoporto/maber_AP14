import operator
import random


def generate_question(level):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    shapes = ["◼", "▲", "●", "◆", "○"]
    shape1, shape2, shape3, shape4 = random.sample(shapes, 4)
    ops = [random.choice(list(operations.keys())) for _ in range(3)]
    op1, op2, op3 = ops[0], ops[1], ops[2]

    
    def make_hint(shape, op, value):
        expr = f"{value}{op}{value}{op}{value}"
        result = round(eval(expr), 2)
        return f"{shape} {op} {shape} {op} {shape} = {result}"

    if level <= 15:
        if level == 1:
            v1, v2 = random.randint(1, 10), random.randint(1, 10)
            question = f"{shape1} + {shape2} = ?"
            hint1 = f"{shape1} + {shape1} = {v1 + v1}"
            hint2 = f"{shape2} + {shape2} = {v2 + v2}"
            answer = v1 + v2
        elif 1 < level <= 3:
            op = random.choice(["+", "-"])
            v1, v2 = random.randint(5, 25), random.randint(5, 25)
            question = f"{shape1} {op} {shape2} = ?"
            hint1 = make_hint(shape1, op, v1)
            hint2 = make_hint(shape2, op, v2)
            answer = round(eval(f"{v1}{op}{v2}"), 2)
        elif 3 < level <= 9:
            v = [random.randint(10, 30) for _ in range(3)]
            v1, v2, v3 = v[0], v[1], v[2]
            expr = f"{v1} {op1} {v2} {op2} {v3}"
            question = f"{shape1} {op1} {shape2} {op2} {shape3} = ?"
            answer = round(eval(expr), 2)
            hint1 = make_hint(shape1, op1, v1)
            hint2 = make_hint(shape2, op2, v2)
            hint3 = make_hint(shape3, op3, v3)
        else:
            ops = [random.choice(list(operations.keys())) for _ in range(3)]
            v = [random.randint(30, 50) for _ in range(4)]
            expr = f"{v[0]} {ops[0]} {v[1]} {ops[1]} {v[2]} {ops[2]} {v[3]}"
            question = f"{shape1} {ops[0]} {shape2} {ops[1]} {shape3} {ops[2]} {shape4} = ?"
            answer = round(eval(expr), 2)
            hint1 = make_hint(shape1, op1, v[0])
            hint2 = make_hint(shape2, op2, v[1])
            hint3 = make_hint(shape3, op2, v[2])
            hint4 = make_hint(shape4, op3, v[3])
    elif 15 < level <= 19:
        ops1, ops2 = "*", "/"        
        ops = [random.choice(["+", "-", "*"]) for _ in range(2)]
        v = [random.randint(50, 200) for _ in range(4)]
        expr = f"{v[0]} {ops1} {v[1]} {ops2} {v[2]} {ops[1]} {v[3]}"
        question = f"{shape1} {ops1} {shape2} {ops2} {shape3} {ops[1]} {shape4} = ?"
        answer = round(eval(expr), 2)
        hint1_expr = f"{v[0]} {ops1} {v[1]} {ops1} {v[2]} {ops1} {v[3]}"
        hint1_result = round(eval(hint1_expr), 2)
        hint2_expr = f"{v[0]} {ops[1]} {v[1]} {ops[1]} {v[2]} {ops[1]} {v[3]}"
        hint2_result = round(eval(hint2_expr), 2)
        hint1 = f"{shape1} {ops1} {shape2} {ops1} {shape3} {ops1} {shape4} = {hint1_result}"
        hint2 = f"{shape1} {ops[1]} {shape2} {ops[1]} {shape3} {ops[1]} {shape4} = {hint2_result}"
        hint3 = make_hint(shape1, ops[0], v[0])
        hint4 = make_hint(shape4, ops[1], v[3])
    else:
        question = "Terdapat pola ABCDABCDABCD... Apa huruf ke-2018?"
        hint1 = "Pola berulang setiap 4 huruf."
        answer = "B"    
    
    print(f"Level {level}: \n{question}")
    print("\nPetunjuk:")
    for hint in [locals().get(f"hint{i}") for i in range(1, 5)]:
        if hint:
            print(hint)    
    return answer