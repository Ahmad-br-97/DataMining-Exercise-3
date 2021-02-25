import re
from os import listdir
from math import log
from wordcloud import WordCloud, ImageColorGenerator
from nltk.stem import PorterStemmer, WordNetLemmatizer
from matplotlib import pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
from nltk.corpus import stopwords

#-----------------------------------------------------------------------------------------
	
def textPreprocesser(value): # A Function For "Text preprocessing" (Exercise 1)

    token = sent_tokenize(value)
	
    token = token.lower()
	
	# Cleaning Text : ------------------------
    cleaned_text = re.sub(r'[<^+>]', ' ', token)
    cleaned_text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%|-)*\b', '', cleaned_text)
    cleaned_text = re.sub(r'[^a-zA-Z]', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s+[a-zA-Z]\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
	#-----------------------------------------
	
    filte = list(map(cleaned_text, sent_token))
    word_token = []
	
    for sen in filtered:
        word_token.extend(word_tokenize(sen))
		
    stop_words = set(stopwords.words('english'))
    word_list = [word for word in word_token if not word in stop_words]
    stemed = list(map(PorterStemmer().stem, word_list))
	
    lem = WordNetLemmatizer()
	
    lem_word = list(map(lem.lemmatize, stemed))
	
    return lem_word

#-----------------------------------------------------------------------------------------
	
def entropy(value): # A Function For Calculate "Entropy" (Exercise 3)

    probably = [float(value.count(c)) / len(value) for c in dict.fromkeys(list(value))]
    entropy = sum([p * log(p) / log(2.0) for p in probably])
	
    return (0 - entropy)

#-----------------------------------------------------------------------------------------
	
def wordCloudChart(text, title): # A Function For Drawing "WordCloud" Chart (Exercise 4)

    wird_cloud = WordCloud(max_font_size=50, max_words=100, background_color='white').generate(text)
	
	print('\n\nwordCloud Chart:\n')
	
    plt.figure()
    plt.imshow(wird_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

#-----------------------------------------------------------------------------------------
	
def frequencyMatrix(word_list): # A Function For Calculate "Word-Attribute Frequency" Matrix (Exercise 5)
 
    repeat_word = []	
    for text in word_list:
        for word in text:
		
            if word not in repeat_word:
			
                repeat_word.append(word)
				
            else: continue
				
    first_row = ' '.join(repeat_word)
	
    rows = ''
    for text in word_list:
	
        for word in repeat_word:
		
            rows += ' ' + str(text.count(word))
			
        rows += '\n'
		
    return first_row + '\n' + rows

#-----------------------------------------------------------------------------------------
	
if name == 'main': # Calculate "Term Frequency" (Exercise 2)

    input_list = listdir('data')
    input_list.sort()
    words = []
	
    for title in input_list:
	
        file = open(file'data/{title}', 'r')
        text = f.read()
        file.close()
				
        word_list = textPreprocesser(text) # Text preprocessing (Exercise 1)
		print('Word List:')
		print(word_list)
		
		print('\n\nEntropy:')
		print(entropy(word_list)) # Calculate Entropy (Exercise 3)
		
		wordCloudChart(text, title) # Drawing WordCloud Chart (Exercise 4)
		
        count = Counter(word_list)
		print('\n\nWord List Count:')
		print(count)
		
        words.append(word_list)
				
    frequency_matrix = frequencyMatrix(words) # Calculate Word-Attribute Frequency Matrix (Exercise 5)
	print(\n\n'Frequency Matrix:')
	print(frequency_matrix)