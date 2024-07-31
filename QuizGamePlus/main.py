from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

quiz_db_response = requests.get(url="https://opentdb.com/api.php", params=parameters)
questions = quiz_db_response.json()["results"]

question_bank = [Question(item["question"], item["correct_answer"]) for item in questions]

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)


