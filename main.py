import json


with open ("question.json", "r") as file:
    content=file.read()


data= json.loads(content)


score=0
for index,que in enumerate(data):
    print(index+1, ".", que["question_text"])
    for index,option in enumerate(que["options"]):
        print (index+1, ".", option)
    user_choice=int(input("your option: "))
    que["your answer"]= user_choice
    if que["your answer"]==que["correct_option"]:
        score=score+1


print("Your Score is: ", score, "/", len(data))
