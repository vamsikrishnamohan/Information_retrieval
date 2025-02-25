from util import *
import nltk
nltk.download("punkt_tab")

# Add your import statements here
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize 



class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		segmentedText=text.replace("?",".").replace("!",".") # replacing the delimiters like ("?","!" ) to "." 
		segmentedText=segmentedText.split(".")
		segmentedText=[s.strip() for s in segmentedText if s.strip()] # stripping the extra spaces 


		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		# segmentedText = None

		#Fill in code here
		# Tokenizer=PunktSentenceTokenizer()
		# segmentedText=Tokenizer.tokenize(text)
		segmentedText=sent_tokenize(text)
		
		return segmentedText

ckeck=SentenceSegmentation()
text="hey man , whats up. , iam Dr. vk well know gastrologist. i have a girlfriend who is a dentist. nice to meet to man."
naive_sentences=ckeck.naive(text)
punkt_sentences=ckeck.punkt(text)
print(f"naive : {naive_sentences}")
print(f"punkt : {punkt_sentences}")