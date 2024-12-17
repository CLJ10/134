from collections import Counter
color_roots = ['червон', 'син', 'зелен', 'жовт', 'чорн', 'біло', 'сір', 'оранж', 'фіолет', 'коричн']
text = """
Тут можете вставити ваш текст, що описує кольори.
Наприклад: червоний, синій, зелений, жовтий, червоний, білий, сірий, оранжевий, фіолетовий, коричневий.
"""
words = text.lower().split()
def has_color_root(word, roots):
    for root in roots:
        if root in word:
            return True
    return False
color_words = [word for word in words if has_color_root(word, color_roots)]
color_counts = Counter(color_words)
most_common_color = color_counts.most_common(1)

print("Слова, що характеризують колір:", color_words)
print("Кількість слів, що характеризують колір:", len(color_words))
print("Переважний колір:", most_common_color)