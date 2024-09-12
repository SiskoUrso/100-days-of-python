class QuizBrain:

    def __init__(self, q_list):
        """
        Initialize the QuizBrain with a list of questions.

        Parameters
        ----------
        q_list : list
            A list of Question objects.
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        """
        Ask the user the next question and check their answer.

        This method will advance the question number and ask the user the next
        question. It will then check the user's answer using the check_answer
        method.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """
        Check if there are still more questions in the question list.

        Returns
        -------
        bool
            True if there are still more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
        Check if the user's answer matches the correct answer.

        Parameters
        ----------
        user_answer : str
            The user's answer.
        correct_answer : str
            The correct answer.

        Notes
        -----
        Updates the score if the user's answer is correct.
        Prints a message indicating whether the user's answer is correct or not.
        Prints the correct answer.
        Prints the user's current score.
        """
        
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's incorrect.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{len(self.question_list)}")
        print("\n")