#!/usr/bin/python
# -*- coding: utf-8 -*-

class SoundEx:
    #b, c, ch, d, đ, g, gh, h, k, kh, l, m, n, ng, ngh, nh, p, ph, q, r, s, t, th, tr, v, x, none
    initialConsonants = {u'r', u'd', u'gi', u'v', u'ch', u'tr', u's', u'x', u'l', u'n', u'qu', u'b', u'c', u'k', u'đ', u'g', u'gh', u'h', u'kh', u'm', u'ng', u'ngh', u'nh', u'p', u'ph', u't', u'th'}

    #c, ch, m, n, ng, nh, p, t, none
    endConsonants = {u't',u'p',u'ng',u'nh',u'c',u'n',u'm', u'ch'}

    #error set based pronunciation
    initialConsonantErrorSet = {
        u'c': [u'k'], u'k': [u'c'], 
        u'g': [u'gh'], u'gh': [u'g'], 
        u'ng': [u'ngh'], u'ngh': [u'ng'], 
        u'ch': [u'tr'], u'tr': [u'ch'], 
        u's': [u'x'], u'x': [u's'], 
        u'v': [u'd', u'gi', u'r'], u'd': [u'v', u'gi', u'r'], u'gi': [u'd', u'v', u'r'], u'r': [u'd', u'gi', u'v']}

    middleConsonantCombinationErrorSet = {
        u'ai': [u'ay', u'ây'], u'ay': [u'ai', u'ây'], u'ây': [u'ay', u'ai'], 
        u'ao': [u'au', u'âu'], u'au': [u'ao', u'âu'], u'âu':[u'au', u'ao'], 
        u'ă': [u'â'], u'â': [u'ă'],
        u'iu': [u'iêu', u'êu'], u'iêu': [u'iu', u'êu'], u'êu': [u'iêu', u'iu'],
        u'i': [u'iê', u'e', u'ê'], u'iê': [u'i', u'e', u'ê'], u'e': [u'iê', u'i', u'ê'], u'ê': [u'iê', u'e', u'i'],
        u'oi': [u'ôi', u'ơi'], u'ôi': [u'oi', u'ơi'], u'ơi': [u'ôi', u'oi'],
        u'o': [u'ô', u'ơ'], u'ô': [u'o', u'ơ'], u'ơ': [u'ô', u'o'], 
        u'ui': [u'uôi'], u'uôi': [u'ui'], 
        u'u': [u'uô'], u'uô': [u'u'],
        u'ưi': [u'ươi'], u'ươi': [u'ưi'],
        u'ưu': [u'ươu'], u'ươu': [u'ưu']}

    endConsonantsErrorSet = {
        u'n': [u'ng', u'nh'], u'ng': [u'n', u'nh'], u'nh':[u'ng', u'n'],
        u't': [u'c', u'ch'], u'c': [u't', u'ch'], u'ch': [u'c', u't']}

    def __init__(self, dictionary):
        self.initialConsonant = ''
        self.endConsonant = ''
        self.middleConsonantCombination = ''
        self.containsError = False
        self.VietnameseDictionary = dictionary


    def extractComponent(self, input):
        self.initialConsonant = ''
        self.endConsonant = ''
        self.middleConsonantCombination = ''
        self.containsError = False

        #a word will be extract into 3 components: initial component (initial consonant), middle component (middle consonant combination), end 
        #component (end consonant)
        if input[:1] in self.initialConsonants:
            if (len(input) == 1 
                or (len(input) == 2 and (input[-1] in self.endConsonants or input[-1] in self.initialConsonants))
                or (len(input) == 3 and (input[-2:] in self.endConsonants or input[-2:] in self.initialConsonants))):
                self.containsError = True
            elif input[:2] in self.initialConsonants:
                if (len(input) == 2 
                    or (len(input) == 3 and (input[-1] in self.endConsonants or input[-1] in self.initialConsonants))
                    or (len(input) == 4 and (input[-2:] in self.endConsonants or input[-2:] in self.initialConsonants))):
                    self.containsError = True
                elif input[:3] in self.initialConsonants:
                    if (len(input) == 3 
                        or (len(input) == 4 and (input[-1] in self.endConsonants or input[-1] in self.initialConsonants))
                        or (len(input) == 5 and (input[-2:] in self.endConsonants or input[-2:] in self.initialConsonants))):
                        self.containsError = True
                    else:
                        self.initialConsonant = input[:3]
                        if (input[-2:] in self.endConsonants):
                            self.endConsonant = input[-2:]
                            self.middleConsonantCombination = input[3:-2]
                        elif (input[-1] in self.endConsonants):
                            self.endConsonant = input[-1]
                            self.middleConsonantCombination = input[3:-1]
                        else:
                            self.middleConsonantCombination = input[3:]
                else:
                    self.initialConsonant = input[:2]
                    if (input[-2:] in self.endConsonants):
                        self.endConsonant = input[-2:]
                        self.middleConsonantCombination = input[2:-2]
                    elif (input[-1] in self.endConsonants):
                        self.endConsonant = input[-1]
                        self.middleConsonantCombination = input[2:-1]
                    else:
                        self.middleConsonantCombination = input[2:]
            else:
                self.initialConsonant = input[:1]
                if (input[-2:] in self.endConsonants):
                    self.endConsonant = input[-2:]
                    self.middleConsonantCombination = input[1:-2]
                elif (input[-1] in self.endConsonants):
                    self.endConsonant = input[-1]
                    self.middleConsonantCombination = input[1:-1]
                else:
                    self.middleConsonantCombination = input[1:]
        
        self.initialConsonant = self.initialConsonant.decode('utf-8')
        self.middleConsonantCombination = self.middleConsonantCombination.decode('utf-8')
        self.endConsonant = self.endConsonant.decode('utf-8')
        return self.generateCandidates()

    def generateCandidates(self):
        if self.containsError:
            return []
        else:
            candidates = []

            #There will be 8 cases: Y indicates error, N indicates no error
            # Y Y Y -----> there is no error
            # Y Y N
            # Y N Y
            # N Y Y
            # Y N N
            # N Y N
            # N N Y
            # N N N -----> error in all components

            #error in initialConsonant
            if (self.initialConsonant in self.initialConsonantErrorSet):
                for consonant in self.initialConsonantErrorSet[self.initialConsonant]:
                    item = consonant + self.middleConsonantCombination + self.endConsonant
                    # for itemDict in self.VietnameseDictionary:
                    #     if item.encode('utf-8') == itemDict:
                    #         candidates.append(item)
                    #         break
                    if item.encode('utf-8') in self.VietnameseDictionary:
                        candidates.append(item)
            
            #error in endConsonant
            if (self.endConsonant in self.endConsonantsErrorSet):
                for consonant in self.endConsonantsErrorSet[self.endConsonant]:
                    item = self.initialConsonant + self.middleConsonantCombination + consonant
                    # for itemDict in self.VietnameseDictionary:
                    #     if item.encode('utf-8') == itemDict:
                    #         candidates.append(item)
                    #         break
                    if item.encode('utf-8') in self.VietnameseDictionary:
                        candidates.append(item)

            #error in middleConsonant
            if (self.middleConsonantCombination in self.middleConsonantCombinationErrorSet):
                for consonant in self.middleConsonantCombinationErrorSet[self.middleConsonantCombination]:
                    item = self.initialConsonant + consonant + self.endConsonant
                    # for itemDict in self.VietnameseDictionary:
                    #     if item.encode('utf-8') == itemDict:
                    #         candidates.append(item)
                    #         break
                    if item.encode('utf-8') in self.VietnameseDictionary:
                        candidates.append(item)


            #error in initialConsonant and endConsonant
            if (self.initialConsonant in self.initialConsonantErrorSet 
                and self.endConsonant in self.endConsonantsErrorSet):
                for consonant1 in self.initialConsonantErrorSet[self.initialConsonant]:
                    for consonant2 in self.endConsonantsErrorSet[self.endConsonant]:
                        item = consonant1 + self.middleConsonantCombination + consonant2
                        # for itemDict in self.VietnameseDictionary:
                        #     if item.encode('utf-8') == itemDict:
                        #         candidates.append(item)
                        #         break
                        if item.encode('utf-8') in self.VietnameseDictionary:
                            candidates.append(item)

            #error in initialConsonant and middleConsonant
            if (self.initialConsonant in self.initialConsonantErrorSet 
                and self.middleConsonantCombination in self.middleConsonantCombinationErrorSet):
                for consonant1 in self.initialConsonantErrorSet[self.initialConsonant]:
                    for consonant2 in self.middleConsonantCombinationErrorSet[self.middleConsonantCombination]:
                        item = consonant1 + consonant2 + self.endConsonant
                        # for itemDict in self.VietnameseDictionary:
                        #     if item.encode('utf-8') == itemDict:
                        #         candidates.append(item)
                        #         break
                        if item.encode('utf-8') in self.VietnameseDictionary:
                            candidates.append(item)

            #error in middleConsonant and endConsonant
            if (self.middleConsonantCombination in self.middleConsonantCombinationErrorSet 
                and self.endConsonant in self.endConsonantsErrorSet):
                for consonant1 in self.middleConsonantCombinationErrorSet[self.middleConsonantCombination]:
                    for consonant2 in self.endConsonantsErrorSet[self.endConsonant]:
                        item = self.initialConsonant + consonant1 + consonant2
                        # for itemDict in self.VietnameseDictionary:
                        #     if item.encode('utf-8') == itemDict:
                        #         candidates.append(item)
                        #         break
                        if item.encode('utf-8') in self.VietnameseDictionary:
                            candidates.append(item)

            #error in all components
            if (self.initialConsonant in self.initialConsonantErrorSet 
                and self.middleConsonantCombination in self.middleConsonantCombinationErrorSet
                and self.endConsonant in self.endConsonantsErrorSet):
                for consonant1 in self.initialConsonantErrorSet[self.initialConsonant]:
                    for consonant2 in self.middleConsonantCombinationErrorSet[self.middleConsonantCombination]:
                        for consonant3 in self.endConsonantsErrorSet[self.endConsonant]:
                            item = consonant1 + consonant2 + consonant3
                            # for itemDict in self.VietnameseDictionary:
                            #     if item.encode('utf-8') == itemDict:
                            #         candidates.append(item)
                            #         break
                            if item.encode('utf-8') in self.VietnameseDictionary:
                                candidates.append(item)

            # for item in candidates:
            #     print item
            if (len(candidates) > 0):
                return candidates
            return ['']
