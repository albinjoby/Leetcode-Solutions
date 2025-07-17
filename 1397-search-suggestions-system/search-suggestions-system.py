class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        currentWord = ""
        for word in searchWord:
            currentWord += word
            print(currentWord)
            curr = sorted([product for product in products if product.startswith(currentWord)])[0:3]
            print(curr)
            res.append(curr)
        
        return res