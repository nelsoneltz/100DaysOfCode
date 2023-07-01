from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item['text']
    question_answer = item['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz! Congrats")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
print("\n")