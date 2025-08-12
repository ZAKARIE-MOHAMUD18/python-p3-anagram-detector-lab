# your code goes here!

class Anagram:
    def  __init__(self,word):
        self.word = word.lower()
        
    
    def match(self,candidates):
        matches=[]
        sorted_word = sorted(self.word)

        for candidate in candidates:
            if candidate.lower() == self.word:
                continue
            if sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches
            

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])

