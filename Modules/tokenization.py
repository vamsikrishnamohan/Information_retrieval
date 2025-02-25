from util import *

# Add your import statements here
from nltk.tokenize import TreebankWordTokenizer

class Tokenization():

    def naive(self, text):
        """
        Tokenization using a Naive Approach

        Parameters
        ----------
        arg1 : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """

        tokenizedText = []

        for sentence in text:
            words = sentence.split()  # Split by whitespace
            clean_words = [word.strip('.,!?;:"()[]{}') for word in words if word.strip()]
            tokenizedText.append(clean_words)

        return tokenizedText


    def pennTreeBank(self, text):
        """
        Tokenization using the Penn Tree Bank Tokenizer

        Parameters
        ----------
        arg1 : list
            A list of strings where each string is a single sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
        """

        tokenizer = TreebankWordTokenizer()
        tokenizedText = [tokenizer.tokenize(sentence) for sentence in text]

        return tokenizedText


#checking the code
text = [
    "Hey man, what's up?",
    "I am Dr. VK, a well-known gastroenterologist!",
    "I have a girlfriend who is a dentist.",
    "Nice to meet you, man."
]

tokenizer = Tokenization()

# Naïve Tokenization
naive_tokens = tokenizer.naive(text)
print("Naïve Tokenization:", naive_tokens.size)

# Penn Treebank Tokenization
ptb_tokens = tokenizer.pennTreeBank(text)
print("Penn Treebank Tokenization:", ptb_tokens)
