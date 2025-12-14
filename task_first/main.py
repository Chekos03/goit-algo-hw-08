import heapq

def min_cost(cables):
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first+second
        total_cost +=cost
        heapq.heappush(cables,cost)
    return total_cost

cables = [5,4,3,7]
result = min_cost(cables)
print(result)