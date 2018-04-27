import math, collections
class NGramLanguageModel:
    def __init__(self, corpus):
        """Initialize your data structures in the constructor."""
        
        #self.bigramCounts = collections.defaultdict(int)
        #self.unigramCounts = collections.defaultdict(int)
        self.trigramCounts1 = collections.defaultdict(lambda: 0)
        self.trigramCounts2 = collections.defaultdict(lambda: 0)
        self.trigramCounts3 = collections.defaultdict(lambda: 0)
        #self.fivegramCounts = collections.defaultdict(lambda: 0)
        
        #self.total = 0
        self.train(corpus)

    def train(self, corpus):
        """ Takes a corpus and trains your language model. 
            Compute any counts or other corpus statistics in this function.
        """
        wi_2 = '<s>'
        wi_1 = ''
        for sentence in corpus.corpus:
            datums = sentence.data 
            for i in range(1, len(datums)-2):
                if i == 1:
                    wi_1 = datums[i].word
                if i > 1:
                    wi = datums[i].word
                    wi1 = datums[i+1].word
                    wi2 = datums[i+2].word
                    trigram1 = (wi_2, wi_1, wi)
                    trigram2 = (wi_1, wi, wi1)
                    trigram3 = (wi, wi1, wi2)
                    self.trigramCounts1[trigram1] += 1
                    self.trigramCounts2[trigram2] += 1
                    self.trigramCounts3[trigram3] += 1
                    
                    # fivegram = (wi_2, wi_1, wi, wi1, wi2)
                    # self.fivegramCounts[fivegram] += 1

                    #update 
                    wi_2 = datums[i-1].word
                    wi_1 = datums[i].word

                    # what is self.total
                    # self.total += 1
        # print self.trigramCounts1
        # print self.trigramCounts2
        # print self.trigramCounts3