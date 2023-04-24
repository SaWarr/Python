# multiple choice quiz
question_prompts = [
    "What colour is Nelly's favourite? \n(a) Red \n(b) Yellow \n(c) Blue\n\n",
    "What is her favourite food? \n(a) Noodles \n(b) Pizza \n(c) Pasta\n\n",
    "What does she like to watch? \n(a) Football \n(b) Star Wars \n(c) Gabby's Dollhouse"
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_quiz(questions):
    correct = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            correct += 1
    print("You got " + str(correct) + "/" + str(len(questions)) + " right!")

run_quiz(questions)