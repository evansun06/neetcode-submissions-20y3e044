from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adjc_list = defaultdict(list)

        for start, end in tickets:
            adjc_list[start].append(end)

        # Reverse sort so pop() gives smallest destination
        for airport in adjc_list:
            adjc_list[airport].sort(reverse=True)

        itinerary = []

        def dfs(departure):

            while adjc_list[departure]:
                arrival = adjc_list[departure].pop()
                dfs(arrival)

            itinerary.append(departure)

        dfs("JFK")

        return itinerary[::-1]