import re
from string import punctuation
import spacy
from gensim.models import LdaModel
from gensim.corpora import Dictionary


def prepare_text(text):
    # Удаление ссылок
    text_no_links = re.sub(r"http\S+", "", text)

    # Удаление знаков пунктуации
    text_no_punctuation = "".join(
        char for char in text_no_links if char not in punctuation
    )

    return text_no_punctuation


def lemmatize_texts(texts):
    nlp = spacy.load("ru_core_news_sm")
    lemmatized_texts = []

    for text in texts:
        doc = nlp(" ".join(text))
        lemmatized_text = [
            token.lemma_ for token in doc if not token.is_stop and token.is_alpha
        ]
        lemmatized_texts.append(lemmatized_text)

    return lemmatized_texts


def lda_topics_from_texts(texts):
    # Создание словаря и корпуса для модели LDA
    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # Обучение модели LDA
    lda_model = LdaModel(corpus, num_topics=3, id2word=dictionary, passes=10)

    # Вывод тематик и их слов
    topics = lda_model.print_topics(num_words=5)

    return topics


# Пример использования функции
texts = [
    ["я", "читать", "книга"],
    ["это", "интересно"],
    ["анализ", "текст", "и", "тематика"],
    # Добавьте свои тексты или загрузите реальные данные
]

result_topics = lda_topics_from_texts(lemmatize_texts(texts))
for topic in result_topics:
    print(topic)
