class FrequencyTracker:

    def __init__(self):
        self.nos_tracker = defaultdict(int)
        self.freqs_tracker = defaultdict(int)

        

    def add(self, number: int) -> None:
        if number in self.nos_tracker and self.nos_tracker[number] > 0:
            no_id = self.nos_tracker[number]
            self.freqs_tracker[no_id] -=1
        self.nos_tracker[number] += 1
        self.freqs_tracker[self.nos_tracker[number]] +=1
            
        

    def deleteOne(self, number: int) -> None:
        if number in self.nos_tracker and self.nos_tracker[number] > 0:
            no_id = self.nos_tracker[number]
            self.freqs_tracker[no_id] -=1
            self.nos_tracker[number] -=1
        self.freqs_tracker[self.nos_tracker[number]] +=1    
            
            
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqs_tracker[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)