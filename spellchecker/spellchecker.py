words = open("spellwords.txt").readlines()
words = map(lambda x: x.strip(), words)
#print words
print len(words)
print words[0]
print words[len(words)-1]

print ('zygotic' in words)
print ('mistasdas' in words)

class SpellChecker:
    def __init__(self):
        self.words = []
    def load_words(self,file_name):
        self.words = open(file_name).readlines()
        self.words = map(lambda x: x.strip(), self.words)
    def check_word(self,word):
        return word.strip(".").lower() in self.words

    def check_words(self,sentence):
        words_to_check = sentence.split(' ')
        for word in words_to_check:
            if not self.check_word(word):
                print ("Word is misspelt: " + word)
                return False
        return True
if __name__=='__main__':

    spell_check = SpellChecker()
    words = spell_check.load_words("spellwords.txt")
    #print words[0]
    print spell_check.check_word("zygotic")
    print spell_check.check_word("mistasdas")
    print spell_check.check_words("zygotic mistasdas elementary")



#print load_words("spellwords.txt")[0]

#print check_word(words,'zygotic')
#print check_word(words,'mistasdas')
