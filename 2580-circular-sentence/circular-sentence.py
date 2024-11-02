class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        print(sentence)

        if sentence[0][0] != sentence[-1][-1]:
            return False
        
        for i in range(1,len(sentence)):
            if sentence[i-1][-1] != sentence[i][0]:
                return False

        return True