from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    q_dic = Question(q_text=question["question"], q_answer=question["correct_answer"])
    question_bank.append(q_dic)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()
print("you completed the quiz yeeehoooooo")
print(f"your score was {quiz.score}/{quiz.questions_number}")