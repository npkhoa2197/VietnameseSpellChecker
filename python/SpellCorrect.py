#!/usr/bin/python
# -*- coding: utf-8 -*-

from PreProcessing import PreProcessing
from NGramLanguageModel import NGramLanguageModel
from TelexConverter import TelexConverter
from SoundEx import SoundEx

class VietnameseSpellChecker:
    """Holds edit model (telex processor and SoundEx algorithm), language model, corpus."""

    def __init__(self, lm, corpus):
        """initializes the language model, telex converter, soundEx"""
        self.languageModel = lm
        self.VietnameseDictionary = self.ReadDictionary()
        self.converter = TelexConverter(self.VietnameseDictionary)
        self.soundEx = SoundEx(self.VietnameseDictionary)

    def ReadDictionary(self):
        dictionaryPath = "../data/Viet74K.txt"
        f = open(dictionaryPath)
        dictionary = []
        for line in f:
            line = line.replace('\n', '')
            dictionary.append(line)
        
        return dictionary

    def evaluate(self, corpus):  
        """Tests this speller on a corpus, returns a SpellingResult"""
        for sentence in corpus.corpus:
            if sentence.isEmpty():
                continue
            processed_sentence = sentence.getProcessableSentence()
            listOfSuggestions = self.correctSentence(processed_sentence)
        
        return listOfSuggestions

    def correctSentence(self, sentence):
        """Takes a list of words, returns a corrected list of words."""
        if len(sentence) == 0:
            return {}
        
        listOfSuggestions = {}
        maxscore = float('-inf')
        bestCandidate = ''
        # argmax_i = 0
        # argmax_w = sentence[0]
        # maxlm = float('-inf')
        # maxedit = float('-inf')

        # skip start and end tokens
        for i in range(1, len(sentence) - 1):
            #word = sentence.get(i)
            word = sentence[i]
            candidates = []
            bestCandidate = ''
            maxscore = float('-inf')
        
            #generate candidates using TelexConverter
            candidates.append(self.converter.ToVietnamese(word))

            #generate candidates using SoundEx (extracting syllable components)
            tempCandidates = self.soundEx.extractComponent(word)
            for each in tempCandidates:
                candidates.append(each)

            #add the word itself as a candidate
            candidates.append(word.decode('utf-8'))

            # if (word == 'sinh' or word == 'tin'):
            #     for each in candidates:
            #         print each
            #     print '--------'

            for candidate in candidates:
                if candidate == '':
                    continue
                #sentence.put(i, candidate)
                sentence[i] = candidate.encode('utf-8')
                
                score = self.languageModel.score(sentence) 
                # if word == 'tin':
                #     print str(sentence) + ': ' + str(score)
                
                if score >= maxscore:
                    maxscore = score
                    bestCandidate = candidate

            # store the best alternative for the corresponding word
            listOfSuggestions[word] = bestCandidate
            # restores sentence to original state before moving on
            sentence[i] = word
            #sentence.put(i, word)
        return listOfSuggestions

def PrintInput(corpus):
    for sentence in corpus.corpus:
        print sentence

def main():
    #take the train data, which will go through preprocessing and ngramlanguagemodel
    trainPath = '../data/train/trainCorpus.dat'
    
    # PreProcessing: normalization, spliting, punctuation mark removal
    trainingCorpus = PreProcessing(trainPath)
    # NGram Language Model 
    nGramLanguageModel = NGramLanguageModel(trainingCorpus)

    #take the test data, which will go through proprocessing and VietnameseSpellChecker evaluation
    testPath = '../data/test/testCorpus.dat'
    testCorpus = PreProcessing(testPath)
    PrintInput(testCorpus)

    # Vietnamese Spell Checker
    spellCorrect = VietnameseSpellChecker(nGramLanguageModel, trainingCorpus)
    print ' ####### List of suggestions ####### '
    suggestions = spellCorrect.evaluate(testCorpus)
    for key in suggestions.keys():
        print key + ' -----> ' + suggestions.get(key).encode('utf-8')

if __name__ == '__main__':
    main()