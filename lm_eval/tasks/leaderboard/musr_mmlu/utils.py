import ast

def doc_to_choice(doc):
    """
    Convert a doc to a choice.
    """
    choices = ast.literal_eval(doc["choices"])
    n_choices = len(choices)
    choice_labels = [chr(65+i) for i in range(n_choices)]
    return choice_labels

DOC_TO_TEXT = (
    "{narrative}\n\n"
    "Question: {question}\n"
    "{choices}\n"
    "Answer:"
)

def doc_to_text(doc):
    """
    Convert a doc to text.
    """
    choices = ""
    for i, choice in enumerate(ast.literal_eval(doc["choices"])):
        choices += f"{chr(65+i)}. {choice}\n"

    text = DOC_TO_TEXT.format(narrative=doc["narrative"], question=doc["question"], choices=choices)

    return text

def doc_to_answer(doc):
    """
    Convert a doc to an answer.
    """
    return chr(65 + doc["answer_index"])