from util import *
import nltk
# nltk.download('averaged_perceptron_tagger_eng')

# Add your import statements here
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet

#Note:
'''For lemmatization Pos_tagging is important because using pos_tagging we can use the base word of the word or elase every word is treated as noun running will be running rather than run. Therefore we we'll use post tagging from nltk  '''
class InflectionReduction:
    
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

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

        reducedText = [[self.lemmatizer.lemmatize(word, self.get_wordnet_pos(word)) for word in sentence] for sentence in text]
        
        return reducedText
	

text = [["running", "quickly"], ["cats", "are", "playing"], ["better", "solutions", "were", "found"]]
lemma=InflectionReduction()
reduced_text=lemma.reduce(text)
print(reduced_text)
