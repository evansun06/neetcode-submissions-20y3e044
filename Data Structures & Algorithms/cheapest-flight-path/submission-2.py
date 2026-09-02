class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        adj = defaultdict(list)

        for departure, arrival, cost in flights:
            adj[departure].append((arrival, cost))

        # (cost, airport, flights_used)
        heap = [(0, src, 0)]

        # best[airport][flights_used]
        best = [[float("inf")] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        while heap:
            cost, airport, flights_used = heapq.heappop(heap)

            if airport == dst:
                return cost

            # k stops means at most k + 1 flights
            if flights_used == k + 1:
                continue

            if cost > best[airport][flights_used]:
                continue

            for next_airport, flight_cost in adj[airport]:
                new_cost = cost + flight_cost
                new_flights = flights_used + 1

                if new_cost < best[next_airport][new_flights]:
                    best[next_airport][new_flights] = new_cost
                    heapq.heappush(
                        heap,
                        (new_cost, next_airport, new_flights)
                    )

        return -1