class UndergroundSystem:

    def __init__(self):
        self.dictionary = {}
        self.time = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dictionary[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        initialStation, ti = self.dictionary[id]
        # Store the check-out time
        self.time[initialStation][stationName].append(t - ti)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Return the average time
        return sum(self.time[startStation][endStation]) / len(self.time[startStation][endStation])