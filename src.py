import re
import os
import nltk
import PyPDF2
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
from sentence_transformers import SentenceTransformer



class text_preprocessing:
	def __init__(self):
		self.text = text

	def remove_extra_space(text):
		return re.sub("\s+", " ", text)

	def lower_case(text):
		return text.lower()

	def remove_urls(text):
		pattern = re.compile(r'https?://\S+|www.\.\S+')
		return pattern.sub(r'', text)

	def remove_punctuations(text):
		punctuations = r'''!\"#$%&'()*+,-/:;<=>?@[\]•^_`{|}~'''
		for char in punctuations:
			if char in text:
				text = text.replace(char, ' ')
		return re.sub("\s+", " ", text)

	def remove_stopwords(text):
		for word in stopwords.words('english'):
			w = f" {word} "
			print(w)
			if w in text:
				text = text.replace(w, ' ')
		return re.sub("\s+", " ", text)

	def stemming(text):
		porter_stemmer = PorterStemmer()
		words = text.split()
		return ' '.join([porter_stemmer.stem(word) for word in words])


class file_processing:
	def save_data(path, file, type='wb'):
		if os.path.exists(path):
			os.remove(path)
			with open(path, type) as f:
				f.write(file)
		else:
			with open(path, type) as f:
				f.write(file)

	def pdf_loader(file):
		reader = PyPDF2.PdfReader(file)
		num_pages = len(reader.pages)
		text = ""
		for page_num in range(num_pages):
			page = reader.pages[page_num]
			text += page.extract_text()
		return text

	def remove_all_files(path):
		if os.path.exists(path):
			os.remove(path)
		else:
			pass

class similarity:
	def text_embedding(text):
		model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
		return model.encode(text, normalize_embeddings=True)

	def find_similarity(embedding1, embedding2):
		return embedding1 @ embedding2.T
