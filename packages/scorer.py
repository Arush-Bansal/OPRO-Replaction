from packages.geminiGenerate import geminiGenerate
def scorePromptQBegin(prompt, dataset):
    correct = 0
    for example in dataset:
        generation = geminiGenerate(f"{prompt}\n{example["target"]}")
        # print(f"|{example["target"]}|   ::::   |{generation}|", end="")
        if generation == example["target"]: 
            correct += 1
            print(".")
        else:
            pass
            print(f"|{example["target"]}|   ::::   |{generation}|","     : INCORRECT")



    score = correct/len(dataset)
    return score

# print(f"score :::: {scorePromptQBegin("Solve the following boolean expresion. Reply with only True or False")}")
