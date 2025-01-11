class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        bookedFlightsSeatsCount = [0] * (n + 1)

        #Setting total no. of bookings in each flight
        for booking in bookings:
            first = booking[0]
            last = booking[1]
            seats = booking[2]

            bookedFlightsSeatsCount[first - 1] += seats
            bookedFlightsSeatsCount[last] -= seats

        #Prefix Sum
        for i in range(0,n):
            bookedFlightsSeatsCount[i + 1] += bookedFlightsSeatsCount[i]
            ans[i] = bookedFlightsSeatsCount[i]
        return ans
