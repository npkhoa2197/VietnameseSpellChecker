import re
import string

class PreProcessing:
    corpus = []

    #patterns for regex matching
    email_pat = '([\w\.-]+@)((?:\w|\.|-)+(?:-?[eE]-?[dD]-?[uU]|com|vn|com\.vn))(?!\w+)'
    number_pat = '([0-9]+)'
    #pattern adapted from regex101.com
    url_pat = '((?<=[^a-zA-Z0-9])(?:https?\:\/\/|[a-zA-Z0-9]{1,}\.{1}|\b)(?:\w{1,}\.{1}){1,5}(?:com|org|edu|gov|uk|net|ca|de|jp|fr|au|us|ru|ch|it|nl|se|no|es|mil|iq|io|ac|ly|sm){1}(?:\/[a-zA-Z0-9]{1,})*)'
    url_test = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url_test2 = '((?:[\w]+\.)+(?:com|org|edu|gov|uk|net|ca|de|jp|fr|au|us|ru|ch|it|nl|se|no|es|mil|iq|io|vn|ly|sm){1})'
    
    EMAIL_STRING_REPLACE = "EMAIL"
    NUMBER_STRING_REPLACE = "NUMBER"
    URL_STRING_REPLACE = "WEBSITE"

    def __init__(self, filename=None):
        if filename:
            self.read_file(filename)
        else:
            self.corpus = []

    #process the input file
    def read_file(self, filename):
        f = open(filename)
        self.corpus = []
        for line in f:
            #process each line: line processing includes normalization, sentence splitting, punctuation mark removal
            sentence = self.processLine(line)
            if sentence:
                self.corpus.append(sentence)
    
    def processLine(self, line):
        #normalization: replace 5 -> NUMBER, URL -> WEBSITE, email address -> EMAIL
        line = self.normalize(line)
        return line
        
        # #remove white space
        # line = line.strip()
        # #to lower case
        # line = line.lower()

        # #remove unnecessary punctuation marks that clearly do not affect the meaning of a sentence
        # line = line.replace('"','') 
        # line = line.replace(',', '')
        # line = line.replace('.','') 
        # line = line.replace('!','') 
        # line = line.replace("'",'') 
        # line = line.replace(":",'') 
        # line = line.replace(";",'') 
        # line = line.replace("?",'')

        # if line == '':
        #     return None
        # processed_tokens = Sentence() 
        # processed_tokens.append(Datum("<s>")) #start symbol
        # tokens = line.split()
        # i = 0
        # while i < len(tokens):
        #     token = tokens[i]
        #     if token == '<err':
        #     targ = tokens[i+1]
        #     targ_splits = targ.split('=')
        #     correct_token = targ_splits[1][:-1] # chop off the trailing '>'
        #     correct_token_splits = correct_token.split()
        #     if len(correct_token_splits) > 2: # targ with multiple words
        #         #print 'targ with multiple words: "%s"' % targ
        #         for correct_word in correct_token_splits:
        #         processed_tokens.append(Datum(correct_word))
        #     elif tokens[i+3] != '</err>':
        #         processed_tokens.append(Datum(correct_token))
        #     else:
        #         incorrect_token = tokens[i+2]
        #         processed_tokens.append(Datum(correct_token, incorrect_token))    
        #     i += tokens[i:].index('</err>') + 1 # update index
        #     else: # regular word
        #     processed_tokens.append(Datum(token))
        #     i += 1
        # processed_tokens.append(Datum("</s>"))
        # return processed_tokens

    def normalize(self, line):
        print line
        #match email 1
        matches = re.findall(self.email_pat, line)
        for m in matches:
            email = '%s%s' % m
            line = line.replace(email, self.EMAIL_STRING_REPLACE)

        # match number
        matches = re.findall(self.number_pat, line)
        for m in matches:
            number = '%s' % m 
            line = line.replace(number, self.NUMBER_STRING_REPLACE)

        #match urls
        matches = re.findall(self.url_test, line)
        for m in matches:
            url = '%s' % m 
            line = line.replace(url, self.URL_STRING_REPLACE)
    
        #match urls
        matches = re.findall(self.url_test2, line)
        for m in matches:
            url = '%s' % m 
            line = line.replace(url, self.URL_STRING_REPLACE)
    
        return line




    