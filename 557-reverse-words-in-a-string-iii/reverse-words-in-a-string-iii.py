class Solution(object):
    def reverseWords(self, s):

        # Create a list to store the words
        lst = []
        lst = s.split(" ")

        # iterate through each word in s, reversing and storing it in a string
        res = ""
        for i in lst:
            res += i[::-1]
            res += " "

        return res[:-1]