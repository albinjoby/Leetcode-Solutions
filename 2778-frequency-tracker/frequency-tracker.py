class FrequencyTracker:

    def __init__(self):
        self.num = Counter()
        self.count = Counter()

    def add(self, number: int) -> None:
        self.num[number] += 1
        self.count[self.num[number]] += 1
        self.count[self.num[number] - 1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.num[number]:
            self.num[number] -= 1
            if self.num[number] == 0:
                del self.num[number]
            self.count[self.num[number]] += 1
            self.count[self.num[number] + 1] -= 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.count[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)