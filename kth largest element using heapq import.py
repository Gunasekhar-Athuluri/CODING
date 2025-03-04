import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        Initializes the KthLargest object with a given value of k and an initial list of nums.
        
        Args:
            k (int): The position of the largest number to track.
            nums (List[int]): The initial list of numbers.
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # Convert nums into a heap
        # If the heap has more than k elements, remove the smallest elements until it has exactly k elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        Adds a value to the stream and returns the current k-th largest element.
        
        Args:
            val (int): The value to add to the stream.
            
        Returns:
            int: The k-th largest element after adding the new value.
        """
        heapq.heappush(self.nums, val)  # Push the new value to the heap
        # If after adding the new value, the heap has more than k elements, pop the smallest one
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # The smallest element in the heap is the k-th largest element
        return self.nums[0]

# Example usage:
k = 3
nums = [4, 5, 8, 2]

kthLargest = KthLargest(k, nums)
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10))  # Output: 5
print(kthLargest.add(9))   # Output: 8
print(kthLargest.add(4))   # Output: 8
