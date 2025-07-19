"""
Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
"""
def hasNoConflicts(intervals):
    intervals.sort(key=lambda x: x.start)
    
    for i in range(len(intervals)):
        if intervals[i].end > intervals[i+1].start:
            return False
        
    return True
