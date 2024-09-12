class Question:

    def __init__(self, q_text, q_answer):
        """
        Initialize a Question object with a question text and answer.

        Parameters
        ----------
        q_text : str
            The question text.
        q_answer : str
            The answer to the question.
        """
        
        self.text = q_text
        self.answer = q_answer

