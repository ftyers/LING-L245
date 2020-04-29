import sys

vocab = {} # dict to store frequency list
fd = open ("freq.txt", "r")
# for each of the lines of input
for line in fd.readlines(): 
    # the form is the line without spacing
    form = line.strip( '\n').lower()
    # if we haven't seen it yet, set the frequency count to 0
    if form not in vocab:
        vocab[form] = 0
    vocab[form] = vocab[form] + 1
words=sys.stdin.read()
text=words.split(' ')

# print out the frequency list
for word in text:	
        if word.lower() not in vocab: 
                print('*'+word)
        else:
                print(word)
