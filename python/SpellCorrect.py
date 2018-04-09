from PreProcessing import PreProcessing
#from NGramLanguageModel import NGramLanguageModel

def main():
    trainPath = '../data/train/trainCorpus.dat'
    # TODO: implement PreProcessing: normalization, spliting, punctuation mark removal
    # PreProcessing may also contain other functions of HolbrookCorpus
    trainingCorpus = PreProcessing(trainPath)
    
    for sentence in trainingCorpus.corpus:
        #_data = sentence.data 
        #for i in range(len(datums)):
        print sentence

    ########
    #print trainingCorpus.corpus
    # testPath = '../data/test/testCorpus.dat'
    # # TODO: implement PreProcessing: normalization, spliting, punctuation mark removal
    # # PreProcessing may also contain other functions of HolbrookCorpus
    # testCorpus = PreProcessing(testPath) 
    
    # # TODO: implemnt NGramLanguageModel in which the training corpus will be train (lam theo cach trong paper)
    # nGramLanguageModel = NGramLanguageModel(trainingCorpus)
    # # TODO: implemnt a spell checker which uses the nGramLanguageModel and an edit model | error model
    # #spellCorrect = VietnameseSpellChecker(nGramLanguageModel, trainingCorpus)

    # # TODO: use Laban Key approach for input data
    # # ...
if __name__ == '__main__':
    main()