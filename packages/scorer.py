from geminiGenerate import geminiGenerate
import dataset

def scorePromptQBegin(prompt):
    Dataset = dataset.BooelanExpresion()
    correct = 0
    for example in Dataset:
        generation = geminiGenerate(f"{prompt}\n{example["target"]}")
        # print(f"|{example["target"]}|   ::::   |{generation}|", end="")
        if generation == example["target"]: 
            correct += 1
            print(".")
        else:
            print(f"|{example["target"]}|   ::::   |{generation}|","     : INCORRECT")



    score = correct/len(Dataset)
    return score

print(f"score :::: {scorePromptQBegin("Solve the following boolean expresion. Reply with only True or False")}")
