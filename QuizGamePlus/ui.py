from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="#FFFFFF")
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="hello world",
            font=("Arial", 20, "italic"))

        correct_button_image = PhotoImage(file="images/true.png")
        incorrect_button_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=correct_button_image, padx=20, pady=20, command=self.check_correct)
        self.incorrect_button = Button(image=incorrect_button_image, padx=20, pady=20, command=self.check_incorrect)

        self.correct_button.grid(column=0, row=2)
        self.incorrect_button.grid(column=1, row=2)

        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, highlightthickness=0, bg=THEME_COLOR)

        self.load_question()

        self.window.mainloop()

    def load_question(self):
        self.score_text.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        if not self.quiz.still_has_questions():
            self.correct_button.config(command=NONE)
            self.incorrect_button.config(command=NONE)

    def check_correct(self):
        self.quiz.check_answer("True")
        self.load_question()

    def check_incorrect(self):
        self.quiz.check_answer("False")
        self.load_question()