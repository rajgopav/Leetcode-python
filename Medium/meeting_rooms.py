class Interval():
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution():
    def minMeetingRooms(self, intervals):
        starts, end = [], []
        for elem in intervals:
            starts.append(elem.start)
            end.append(elem.end)

        starts.sort()
        end.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < end[e]:
                cnt_rooms += 1
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1
                e += 1
        return min_rooms

if __name__ == '__main__':
    inter1 = Interval(0,30)
    inter2 = Interval(5, 10)
    inter3 = Interval(15, 20)

    print Solution().minMeetingRooms([inter1,inter2,inter3])

