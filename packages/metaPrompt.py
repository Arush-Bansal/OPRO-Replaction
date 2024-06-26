def InsScoreDictToSortedList(data_list):
    data_list.sort(key=lambda x: x[1], reverse=True)
    return [{"Ins": ins, "Score" : score} for ins, score in data_list]


def InsListToPrompt(InsScoreList):
    textList = []
    for InsScorePair in InsScoreList:
        newText = f"text:\n{InsScorePair["Ins"]}\nscore: {InsScorePair["Score"]}\n"
        textList.append(newText)
    InsScorePrompt = "\n".join(textList)
    return InsScorePrompt

def TrainingDatasetToPrompt_QBegin(TrainingDataset):
    textList = []
    for item in TrainingDataset:
        newText = f"<INS>\n{item["input"]}\noutput:\n{item["target"]}\n"
        textList.append(newText)
    TrainingDatasetPrompt = "\n".join(textList)
    return TrainingDatasetPrompt


def generateMetaPrompt_QBegin(InsScoreDict, TrainingDataset):

    InsScoreSortedList = InsScoreDictToSortedList(InsScoreDict)
    # print(f"InsScoreSortedList : {InsScoreSortedList}")
    initialContext = "I have some texts along with their corresponding scores. The texts are arranged in ascending order based on their scores, where higher scores indicate better quality."
    InsScorePrompt = InsListToPrompt(InsScoreSortedList)
    # print(f"InsScorePrompt : {InsScorePrompt}")
    BestInsContext = "The following exemplars show how to apply your text: you replace <INS> in each input with your text, then read the input and give an output. We say your output is wrong if your output is different from the given output, and we say your output is correct if they are the same."
    TrainingDatasetPrompt = TrainingDatasetToPrompt_QBegin(TrainingDataset)
    # print(f"TrainingDatasetPrompt : {TrainingDatasetPrompt}")
    callToAction = "Write your new text that is different from the old ones and has a score as high as possible. Write the text in square brackets."
    
    metaPrompt = f'{initialContext}\n{InsScorePrompt}\n{BestInsContext}\n{TrainingDatasetPrompt}\n{callToAction}'
    
    return metaPrompt