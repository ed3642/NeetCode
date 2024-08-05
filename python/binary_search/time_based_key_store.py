class TimeMap:
    # hm <key, [(timestamp, val)]>
    # use hs to find key and binary_search the timestamps to find val 
    def __init__(self):
        self.hm = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = tuple([timestamp, value])
        if key in self.hm:
            self.hm[key].append(pair)
        else:
            self.hm[key] = [pair]

    def get(self, key: str, timestamp: int) -> str:
        def binary_search_prev_highest(nums: list[tuple], target) -> str:
            # returns the highest closest val in nums to target
            l = 0
            r = len(nums) - 1
            mid = None

            while l <= r:
                mid = (l + r) // 2
                if nums[mid][0] < target:
                    l = mid + 1
                elif nums[mid][0] > target:
                    r = mid - 1
                else:
                    return nums[mid][1]
            return "" if r == -1 else nums[r][1]
        
        pair_list = self.hm.get(key)
        if not pair_list:
            return ""
        return binary_search_prev_highest(pair_list, timestamp)
    
import collections
import bisect

class TimeMap2:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)