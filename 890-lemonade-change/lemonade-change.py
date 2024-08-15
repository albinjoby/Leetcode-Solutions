class Solution(object):
    def lemonadeChange(self, bills):
        money = {
            "5": 0,
            "10": 0,
            "20": 0
        }
        for bill in bills:
            if bill == 5:
                money["5"] += 1
            elif bill == 10:
                if money["5"] >= 1:
                    money["10"] += 1
                    money["5"] -= 1
                else:
                    return False
            elif bill == 20:
                if money["10"] >= 1 and money["5"] >= 1:
                    money["20"] += 1
                    money["10"] -= 1
                    money["5"] -= 1
                elif money["5"] >= 3:
                    money["20"] += 1
                    money["5"] -= 3
                else:
                    return False
        return True