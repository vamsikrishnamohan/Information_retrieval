from util import *

# Add your import statements here
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer

#Note:
'''For lemmatization Pos_tagging is important because using pos_tagging we can use the base word of the word or elase every word is treated as noun running will be running rather than run. Therefore we we'll use post tagging from nltk  '''
class InflectionReduction:
    
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer() # Lemmatization
        self.stemmer = PorterStemmer() #Stemmer 

    def get_wordnet_pos(self, word):
        """
        Map POS tags to first character used by WordNetLemmatizer.
        """
        tag = pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)  # Default to noun

    def reduce(self, text):
        """
        Inflection Reduction.

        Parameters
        ----------
        text : list
            A list of lists where each sub-list contains a sequence of tokens
            representing a sentence.

        Returns
        -------
        list
            A list of lists where each sub-list contains lemmatized tokens.
        """

        reducedText_lemmatize = [[self.lemmatizer.lemmatize(word, self.get_wordnet_pos(word)) for word in sentence] for sentence in text]
        reducedText_stemmer = [[self.stemmer.stem(word) for word in sentence] for sentence in text]
        
        return reducedText_lemmatize, reducedText_stemmer

#Example Test case:

# text = [["running", "quickly","studies"], ["cats", "are", "playing"], ["better", "solutions", "were", "found"]]
# inflectionReducer = InflectionReduction()

# lemmatize_tokens,Stemming_tokens=inflectionReducer.reduce(text)
# print("Steming Tokens:",Stemming_tokens)
# print("Lemmatize Tokens:",lemmatize_tokens)	
