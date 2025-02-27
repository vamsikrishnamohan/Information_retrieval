from util import *

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

		

		#Fill in code here

		segmentedText=sent_tokenize(text)   # internally calls Punkt Tokenizer 
		
		return segmentedText
