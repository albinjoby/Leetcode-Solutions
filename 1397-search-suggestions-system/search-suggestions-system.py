class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        currentWord = ""
        products  = sorted(products)
        for word in searchWord:
            currentWord += word
            print(currentWord)
            curr = [product for product in products if product.startswith(currentWord)][0:3]
            print(curr)
            res.append(curr)
        
        return res