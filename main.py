# Run using command line: "python main.py hm1_dir"

import os
import sys
from nltk import \
	word_tokenize, \
	FreqDist
from nltk.corpus import stopwords
import re


def main():
	cwd = os.getcwd()
	try:
		# Gets the users system argument
		parameter = sys.argv[1]
		# Returns a message if users argument is not in the directory
		if not os.path.isdir(parameter):
			print("Invalid argument given.")
			return
		# Path points to the new directory
		text_files_path = os.path.join(cwd, parameter)
		# Stores the name of the files in a list
		list_files = os.listdir(text_files_path)
		# list to hold text for all 10 files
		list_text = read_files(text_files_path)
		dict_freq_all = {}
		cumulative_freq_dist = FreqDist()
		for i, v in enumerate(list_text):
			# Removes symbols from the text
			list_text[i] = re.sub(r"[.?!,:;'`\"()\-\n\d]", "", v)
			# Replaces new lines with space
			list_text[i].replace("\n", " ")
			# lower cases the text
			list_text[i] = list_text[i].lower()
			# Tokenize the text into a list of words
			tokens = word_tokenize(list_text[i])
			# Removes stop words from the tokenize list
			stop_words = set(stopwords.words("english"))
			tokens = [t for t in tokens if t not in stop_words]
			# Creates a FreqDist object with the text as arguments
			freq_dist = FreqDist(tokens)
			# Cumulative FreqDist to store top 50 words
			cumulative_freq_dist += freq_dist
			# returns the 5 most common (highest frequency) words
			print(list_files[i], (freq_dist.most_common(5)))
		# Creates a plot chart with top 50 most frequent words across all 10 text files
		cumulative_freq_dist.plot(50, cumulative = True)
	# Returns a message if user did not submit an argument in the console
	except IndexError:
		print("No argument given.")


def read_files(text_files_path):
	list_text = []
	file_dir = os.listdir(text_files_path)
	for file in file_dir:
		file_text = open(os.path.join(text_files_path, file), "r")
		contents = file_text.read()
		list_text.append(contents)
	return list_text


if __name__ == "__main__":
	main()

