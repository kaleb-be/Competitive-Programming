class Solution:
    def sortSentence(self, s: str) -> str:            
        index_word_dict={}
        for word in s.split(" "):
            index_word_dict[int(word[-1])]= word[:-1:]
        words=""
        word_count=0
        for key in sorted(index_word_dict.keys()):
            word_count+=1
            words+=index_word_dict[key]
            if word_count>=len(index_word_dict.keys()):
                continue
            words+=" "
            
        return words
        
        
