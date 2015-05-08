#!/usr/bin/python
'''
this script reads a file containing text of one tweet per line
Filters out stop-words, stems words, etc, writes words to outfile (again, one tweet per line)
'''


#datafile = 'normal_tweets_text.txt'
#outfile = 'normal.tweetext'

datafile = 'sarcastic_tweets_text.txt'
outfile = 'sarcastic.tweetext'


stopwordfile = 'stop_words.txt'
twslangwordfile = 'twitter_slang.txt'
slangwordfile = 'internet_slang.txt'

stoplist = []
twslanglist = []
slanglist = []

def createStopwordList(f):
	words = open(f, 'r').read().split()
	for w in words:
		w = w.lower()
		stoplist.append(w)
	# end for
# end createStopwordList()

def createSlangwordList(f):
        words = open(f, 'r').read().split()
        for w in words:
                w = w.lower()
                slanglist.append(w)
        # end for
# end createSlangwordList()


def createTweetSlangwordList(f):
        words = open(f, 'r').read().split()
        for w in words:
                w = w.lower()
                twslanglist.append(w)
        # end for
# end createTweetSlangwordList()



def processText(text):
	
	#Removing Punctuation Marks
	text = text.strip()
	#text = text.replace('"',' ').replace('\'',' ')
	#text = text.replace('/',' ')
        text = text.replace(',',' , ')
        text = text.replace('.','').replace('?',' ? ').replace('!',' ! ')
	text = text.replace("\\t",' ').replace("\\u",' ').replace("\\r",' ').replace("\\n",' ').replace("\\x",' ')
	text = text.replace('#sarcasm', '')		# considering hashtags as any other word
	text = text.replace('#', 'HASHTAG ')		# considering hashtags as any other word
	text = text.lower()			#Casefolding is done
	original_text = text
	#I have to Remove Date

	words = text.split()
	words = map( lambda x: 'USER' if '@' in x else x, words ) #removing names
	#removing urls
	words = map( lambda x: 'URL' if 'http' in x else x, words )
	words = map( lambda x: 'URL' if 'https' in x else x, words )
	#wordx = words

	#mid_original_text = ""

	#for elem in wordx:
	#	mid_original_text = mid_original_text + " " +  elem
		
	words = map( lambda x: 'STOP' if x in stoplist else x, words )
	words = map( lambda x: 'TSLANG' if x in twslanglist else x, words )
	words = map( lambda x: 'SLANG' if x in slanglist else x, words )
	#words = map( lambda x: 'ALNUM' if x.isalnum() else x, words )

	words = map( lambda x: 'NUM' if x.isdigit() else x, words )		# replace numbers by 'NUM'

	#if not wordx:
	#	final = original_text
	#	print 'Tweet becomes blank after LESS filtering:', original_text
	
	#elif not words:
	if not words:
		final = original_text
		print 'Tweet becomes blank after MORE filtering:', original_text
	else:
		final = ' '.join(words)
	# end if

	return final
# end processText()


#### main process ####

createStopwordList(stopwordfile)
createSlangwordList(slangwordfile)
createTweetSlangwordList(twslangwordfile)

fin = open(datafile, 'r')
fout = open(outfile, 'w')

for line in fin:
	line = line.strip()
	p = processText(line)
	fout.write(p + '\n')
# end for

fin.close()
fout.close()

