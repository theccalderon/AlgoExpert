from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk import sent_tokenize, download
from nltk.corpus import stopwords


def tldr(text_to_summarize, threshold=3):
    # creates a list of documents, in this case sentences.
    sentences = np.array(sent_tokenize(text_to_summarize))

    # matrix with document id, again in this case sentence, and in the columns it has all the tokens (words)
    # so the result is basically { (doc_id: [tf_idf per word] for doc_id in documents }
    vectorized = TfidfVectorizer(stop_words=stopwords.words("english")).\
        fit_transform(sentences).toarray()

    # sum for every sentence and transforming matrix to an array???
    tf_idf_per_sentence = np.sum(vectorized, axis=1)

    # taking the indices for sentences that have an appropriate TF-IDF and join them together
    indices = np.where(tf_idf_per_sentence > threshold)[0]
    return "".join(sentences[indices])


if __name__ == '__main__':
    # download('punkt')
    # download('stopwords')
    print(tldr(
        "The territory that is now Cuba was inhabited as early as the 4th millennium BC, with the Guanahatabey and "
        "Taíno peoples inhabiting the area at the time of Spanish colonization in the 15th century.[15] It was then a "
        "colony of Spain, and slavery was abolished in 1886, remaining a colony until the Spanish–American War of "
        "1898, when Cuba was occupied by the United States and gained independence in 1902. In 1940, Cuba implemented "
        "a new constitution, but mounting political unrest culminated in the 1952 Cuban coup d'état and the "
        "subsequent dictatorship of Fulgencio Batista. The Batista government was overthrown in January 1959 by "
        "the 26th of July Movement during the Cuban Revolution. That revolution established communist rule under the "
        "leadership of Fidel Castro. The country was a point of contention during the Cold War between the "
        "Soviet Union and the United States, and nuclear war nearly broke out during the Cuban Missile Crisis of "
        "1962. Following the dissolution of the Soviet Union, Cuba faced severe economic downturn in the 1990s, "
        "known as the Special Period. In 2008, Fidel Castro retired after 49 years; Raúl Castro was elected his "
        "successor. Raúl Castro retired as president in 2018 and Miguel Díaz-Canel was elected president by the "
        "National Assembly following parliamentary elections. Raúl Castro retired as First Secretary of the Communist "
        "Party in 2021 and Díaz-Canel was elected.", 0))
