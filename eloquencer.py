
import nltk
import urllib2
from bs4 import BeautifulSoup

def tokensToString(tokens):
	string = ""
	first = True
	for word in tokens:
		if first:
			string += word
		else:
			string = string + " " + word
	return string


print "Hello, and welcome to the eloquencer."
print "I try to make you sound smarter."

sentence = raw_input("What would you like to say? \n")

tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

i = 0
change_list = []
for word, tag in tagged:
	if tag == "JJ":
		change_list.append((word, "adjective", i))
	elif tag == "NN":
		change_list.append((word, "noun", i))
	elif tag == "VB":
		change_list.append((word, "verb", i))
	i += 1


print tagged

for word_tuple in change_list:
	word = word_tuple[0]
	wclass = word_tuple[1]
	place = word_tuple[2]
	page_url = "https://www.powerthesaurus.org/"+ word +"/synonyms/"+ wclass
	page = urllib2.urlopen(page_url)

	soup = BeautifulSoup(page, 'html.parser')
	# print "Got soup"
	synonym_box = soup.find('a', attrs={'class': 'topic-link'})
	if synonym_box:
		synonym = synonym_box.text.strip()
	else: 
		synonym = word
	print word + " => " +synonym

	tokens[place] = str(synonym)
print " ".join([x for x in tokens])




#tree = html.fromstring(page.content)

#synonyms = tree.xpath('//div[@id="TB_overlay"]/text()')

