class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        sentence = sentence.split(' ')

        for i in range(1,len(sentence)):
            if sentence[i-1][-1] != sentence[i][0]:
                return False

        return True