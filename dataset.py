import json


def BooelanExpresion():
    with open(r'data/BIG-Bench-Hard-data/boolean_expressions.json') as file:
        dataset = json.load(file)
    file.close()
    exampleList = dataset['examples']
    return exampleList