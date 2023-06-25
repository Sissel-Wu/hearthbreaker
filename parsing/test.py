import ast


def top_level_functions(body):
    return [f for f in body if isinstance(f, ast.FunctionDef)]


def top_level_classes(body):
    return [f for f in body if isinstance(f, ast.ClassDef)]


def parse_ast(filename):
    with open(filename, "rt") as file:
        tree = ast.parse(file.read(), filename)

    classes = top_level_classes(tree.body)
    for cls in classes:
        print(f'Class: {cls.name}')
        methods = [f for f in cls.body if isinstance(f, ast.FunctionDef)]
        for method in methods:
            print(f'...Method: {method.name}')

    funcs = top_level_functions(tree.body)
    for func in funcs:
        print(f'Func: {func.name}')


parse_ast('../hearthbreaker/cards/base.py')
