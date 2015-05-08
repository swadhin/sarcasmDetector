#!/usr/bin/python

'''
Reads a set of text files, and assigns numeric ids to each distinct word in the files
'''

textfiles = ['normal.tweetext','sarcastic.tweetext']
outfile_dict = 'dictionary.tweetext'

#textfiles = ['training.tweetext.raw', 'validation.tweetext.raw']
#outfile_dict = 'dictionary.tweetext.raw'


distinct_words = set()

for tfile in textfiles:
	print 'Processing text file', tfile
	fp = open(tfile, 'r')
	for line in fp:
		words = line.strip().split()
		for w in words:	distinct_words.add(w)
	# end for
	fp.close()
# end for


temp = list(distinct_words)
temp.sort()

fp = open(outfile_dict, 'w')
count = 0
for w in temp:
	count += 1
	fp.write(w + '\t' + str(count) + '\n')
# end for

fp.close()


