import math, collections
class NGramLanguageModel:

    def __init__(self, corpus):
        """Initialize your data structures in the constructor."""
        
        self.unigramCounts = collections.defaultdict(int)
        self.bigramCounts = collections.defaultdict(int)
        self.trigramCounts = collections.defaultdict(int)
        self.total = 0
        self.train(corpus)

    def train(self, corpus):
        """ Takes a corpus and trains your language model. 
            Compute any counts or other corpus statistics in this function.
        """  
        
        for sentence in corpus.corpus:
            temp1 = '@NaN'
            temp2 = '<s>'
            temp3 = '@NaN'
            self.unigramCounts[temp2] = self.unigramCounts[temp2] + 1
            self.total += 1
            for each in sentence.data:
                temp3 = each.word
                self.unigramCounts[temp3] = self.unigramCounts[temp3] + 1
                
                self.bigramCounts[(temp2,temp3)] = self.bigramCounts[(temp2,temp3)] + 1
                
                if temp1 != '@NaN':
                    self.trigramCounts[(temp1,temp2,temp3)] += 1
                
                temp1 = temp2
                temp2 = temp3

                self.total = self.total + 1
        
            temp1 = temp2
            temp2 = temp3
            temp3 = '</s>' 
        
            self.unigramCounts[temp3] = self.unigramCounts[temp3] + 1
            self.bigramCounts[(temp2,temp3)] = self.bigramCounts[(temp2,temp3)] + 1
            self.trigramCounts[(temp1,temp2,temp3)] = self.trigramCounts[(temp1,temp2,temp3)] + 1

            self.total = self.total + 1

    def score(self, sentence):
        """ Takes a list of strings as argument and returns the log-probability of the 
            sentence using your language model. Use whatever data you computed in train() here.
        """
        score = 0
        temp1 = '@NaN'
        temp2 = '<s>'
        temp3 = '@NaN'
        unigramCounts = self.unigramCounts[temp2]
        for word in sentence:
            temp3 = word
            bigramCounts = self.bigramCounts[(temp2,temp3)]
            trigramCounts = self.trigramCounts[(temp1,temp2,temp3)]

            #there will be 3 cases
            #1. there is trigram
            #2. there no trigram
            #3. there is no trigram and bigram
            if trigramCounts > 0:
                score = score + math.log(trigramCounts)
                score = score - (math.log(self.bigramCounts[(temp1,temp2)]))
            elif bigramCounts > 0:
                score = score + math.log(0.4) + math.log(bigramCounts)
                score = score - (math.log(self.unigramCounts[temp2]))
            else:
                score = score + math.log(0.4) + math.log(self.unigramCounts[temp3]+1)
                score = score - (math.log(self.total + (len(self.unigramCounts))))
            
            temp1 = temp2
            temp2 = temp3

        temp1 = temp2
        temp2 = temp3
        temp3 = '</s>' 
        
        unigramCounts = self.unigramCounts[temp3]
        bigramCounts = self.bigramCounts[(temp2,temp3)]
        trigramCounts = self.trigramCounts[(temp1,temp2,temp3)]

        #similar to the above situation, there will also be 3 cases
        #1. there is trigram
        #2. there no trigram
        #3. there is no trigram and bigram
        if trigramCounts > 0:
            score = score + math.log(trigramCounts)
            score = score - (math.log(self.bigramCounts[(temp2,temp3)]))
        elif bigramCounts > 0:
            score = score + math.log(0.4) + math.log(bigramCounts)
            score = score - (math.log(self.unigramCounts[temp2]))
        else: 
            score = score + math.log(0.4) + math.log(unigramCounts+1)
            score = score - (math.log(self.total + (len(self.unigramCounts))))

        return score