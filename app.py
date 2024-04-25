import streamlit as st
import time
from src import text_preprocessing, file_processing, similarity
import time
import os

st.title("Job-skills & profile match app!")

def preprocessing(job_details):
	lower_case_text = text_preprocessing.lower_case(job_details)
	remove_extra_space_text = text_preprocessing.remove_extra_space(lower_case_text)
	remove_url_text = text_preprocessing.remove_urls(remove_extra_space_text)
	remove_punctuation_text = text_preprocessing.remove_punctuations(remove_url_text)
	remove_stopwords_text = text_preprocessing.remove_stopwords(remove_punctuation_text)
	stemmed_text = text_preprocessing.stemming(remove_stopwords_text)
	return stemmed_text

with st.sidebar:
	st.subheader('Upload your CV, in pdf format here:')
	file = st.file_uploader(label = '',
							 type = 'pdf',
							 accept_multiple_files = False,
							)


	if file:
		file_name = file.name
		outputs = "/workspaces/job_profile_match/.files/CVs"
		path = os.path.join(outputs, f"{file_name}.pdf")
		file_processing.save_data(path, file.getvalue(), type = 'wb')
		data = file_processing.pdf_loader(path)
		cv = preprocessing(data)
		st.write(cv)


job_details = st.text_area(label = '',
						   placeholder = "write skills required for job here:",
						   height = 250)
submit_job_details = st.button("submit")


if job_details and submit_job_details:
	preprocessed_text = preprocessing(job_details)

try:
	if cv and preprocessed_text:
		embeddig_1 = similarity.text_embedding(preprocessed_text)
		embeddig_2 = similarity.text_embedding(cv)
		similarity_score = similarity.find_similarity(embedding1 = embeddig_1, embedding2 = embeddig_2)
		st.subheader(f'Profile match to the job is: {round(similarity_score*100,2)} %')
except:
	st.write('HERE')

try:
	if path:
		file_processing.remove_all_files(path)
except:
	pass