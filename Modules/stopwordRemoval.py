# Add your import statements here
from util import *
from nltk.corpus import stopwords

class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list

			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		#Fill in code here
		stop_words=stopwords.words('english')
		stopwordsRemovedText=[[word for word in sentence if word.lower() not in stop_words]for sentence in text]

		return stopwordsRemovedText
