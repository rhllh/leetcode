"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 
Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
"""
class SnapshotArray:
    
    def __init__(self, length):
        # array that holds history of element using (snap_id, val)
        self.records = [[(0,0)] for _ in range(length)]
        self.snap_id = 0
        
    def set(self, index, val):
        self.records[index].append(self.snap_id, val)
        
    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1
    
    def get(self, index, snap_id):
        record = self.records[index]        # get history at this index
        l, r = 0, len(record)-1
        
        # binary search
        while l <= r:
            mid = l + (r-l)//2
            if record[mid][0] <= snap_id:
                l = mid+1
            else:
                r = mid-1
                
                
        return record[r][1]
    
