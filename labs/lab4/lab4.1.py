import string

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    total_chars_with_spaces = len(text)

    total_chars_without_spaces = len(text.replace(" ", "").replace("\n", ""))

    words = text.split()

    total_words = len(words)

    cleaned_words = [word.strip(string.punctuation).lower() for word in words]

    unique_words = set(cleaned_words)
    total_unique_words = len(unique_words)

    word_counts = {}
    for word in cleaned_words:
        word_counts[word] = word_counts.get(word, 0) + 1

    words_with_single_occurrence = sum(1 for count in word_counts.values() if count == 1)

    return {
        "total_chars_with_spaces": total_chars_with_spaces,
        "total_chars_without_spaces": total_chars_without_spaces,
        "total_words": total_words,
        "total_unique_words": total_unique_words,
        "words_with_single_occurrence": words_with_single_occurrence
    }


file_path = "book.txt"

if __name__ == "__main__":
    results = analyze_text(file_path)
    print("Результати аналізу тексту:")
    print(f"Кількість символів із пробілами: {results['total_chars_with_spaces']}")
    print(f"Кількість символів без пробілів: {results['total_chars_without_spaces']}")
    print(f"Кількість слів: {results['total_words']}")
    print(f"Кількість різних слів (без повторів): {results['total_unique_words']}")
    print(f"Кількість унікальних слів, що зустрічаються тільки один раз: {results['words_with_single_occurrence']}")