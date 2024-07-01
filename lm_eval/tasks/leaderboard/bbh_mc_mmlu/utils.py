def doc_to_target(doc):
    text = doc["target"]
    for i in range(26):
        text = text.replace(f'({chr(ord("A") + i)})', f'{chr(ord("A") + i)}')
    return text