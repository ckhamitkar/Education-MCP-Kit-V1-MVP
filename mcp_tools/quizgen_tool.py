import random
from mcp_tools.logging_tool import log_action

def generate_quiz(user: str, text: str, num_questions: int = 5):
    """Generates a multiple-choice quiz from a given text."""
    log_action(user, 'generate_quiz', {'num_questions': num_questions})

    sentences = [s.strip() for s in text.split('.') if len(s.strip().split()) >= 5]
    if not sentences:
        return {"error": "Text is too short to generate a quiz."}

    words = list(set(text.split()))

    quiz = []

    # Ensure we don't try to create more questions than we have sentences
    num_questions = min(num_questions, len(sentences))

    # Get random sentences for questions
    if len(sentences) < num_questions:
        return {"error": f"Not enough sentences to generate {num_questions} questions."}

    question_sentences = random.sample(sentences, num_questions)

    for sentence in question_sentences:
        sentence_words = sentence.split()
        answer = sentence_words[-1]
        question_text = " ".join(sentence_words[:-1]) + " ____."

        # Generate three incorrect options
        options = {answer}
        while len(options) < 4:
            # make sure the random word is not the answer
            random_word = random.choice(words)
            if random_word != answer:
                options.add(random_word)

        # Shuffle options
        shuffled_options = list(options)
        random.shuffle(shuffled_options)

        quiz.append({
            'question': question_text,
            'options': shuffled_options,
            'answer': answer
        })

    return quiz
