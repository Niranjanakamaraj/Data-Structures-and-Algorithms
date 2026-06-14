class Solution:
    def maxMeetings(self, start, end):
        meetings = sorted(zip(end, start))

        count = 1
        last_end = meetings[0][0]

        for curr_end, curr_start in meetings[1:]:
            if curr_start > last_end:
                count += 1
                last_end = curr_end

        return count