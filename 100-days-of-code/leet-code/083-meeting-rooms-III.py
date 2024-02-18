# 2402. Meeting Rooms III
# Hard
# Topics
# Companies
# Hint
# You are given an integer n. There are n rooms numbered from 0 to n - 1.

# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

# Meetings are allocated to rooms in the following manner:

# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

# A half-closed interval [a, b) is the interval between a and b including a and not including b.
class Solution:
  def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    count = [0] * n

    meetings.sort()

    occupied = []  # (endTime, roomId)
    availableRoomIds = [i for i in range(n)]
    heapq.heapify(availableRoomIds)

    for start, end in meetings:
      # Push meetings ending before this meeting in occupied to the
      # availableRoomsIds.
      while occupied and occupied[0][0] <= start:
        heapq.heappush(availableRoomIds, heapq.heappop(occupied)[1])
      if availableRoomIds:
        roomId = heapq.heappop(availableRoomIds)
        count[roomId] += 1
        heapq.heappush(occupied, (end, roomId))
      else:
        newStart, roomId = heapq.heappop(occupied)
        count[roomId] += 1
        heapq.heappush(occupied, (newStart + (end - start), roomId))

    return count.index(max(count))