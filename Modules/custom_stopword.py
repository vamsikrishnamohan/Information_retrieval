from collections import Counter
from nltk.corpus import stopwords

lemmatized_docs=[[["experimental", "investigation", "of", "the", "aerodynamics", "of", "a", "wing", "in", "a", "slipstream", "."], ["an", "experimental", "study", "of", "a", "wing", "in", "a", "propeller", "slipstream", "be", "make", "in", "order", "to", "determine", "the", "spanwise", "distribution", "of", "the", "lift", "increase", "due", "to", "slipstream", "at", "different", "angle", "of", "attack", "of", "the", "wing", "and", "at", "different", "free", "stream", "to", "slipstream", "velocity", "ratio", "."]]]

# Flatten the tokenized document list
all_words = [word for doc in lemmatized_docs for sentence in doc for word in sentence]

# Compute term frequency
word_freq = Counter(all_words)

# Define a threshold: Words that appear in more than 80% of the documents
threshold = len(lemmatized_docs) * 0.8  
corpus_stopwords = {word for word, freq in word_freq.items() if freq > threshold}

print("Custom Corpus Stopwords:", corpus_stopwords)

def remove_corpus_stopwords(tokenized_docs, custom_stopwords):
    return [
        [[word for word in sentence if word not in custom_stopwords] for sentence in doc]
        for doc in tokenized_docs
    ]


def nltk_stopwords(docs):
    
    stop_words=stopwords.words('english')
	
    stopwordsRemovedText=[[word for word in sentence if word not in stop_words]for sentence in docs]
    return stopwordsRemovedText

filtered_docs_custom = remove_corpus_stopwords(lemmatized_docs, corpus_stopwords)
print(f"Custom_removal: {filtered_docs_custom}")

removed_token=nltk_stopwords(lemmatized_docs)
print(f"NLTK Stopword removal:{removed_token}")
