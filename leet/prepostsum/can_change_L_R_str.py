# https://leetcode.com/problems/move-pieces-to-obtain-a-string
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        # order must match
        # L can never gain left_
        # R can never gain right_
        # check if start has same properties as target
        target_total_ = target.count('_')
        num_left_ = 0
        num_right_ = target_total_
        target_order = []
        target_left_ = []
        target_right_ = []

        for ch in target:
            if ch != '_':
                target_order.append(ch)
                target_left_.append(num_left_)
                target_right_.append(num_right_)
            else:
                num_left_ += 1
                num_right_ -= 1

        start_total_ = start.count('_')
        num_left_ = 0
        num_right_ = start_total_
        if start_total_ != target_total_:
            return False

        i = 0
        for ch in start:
            if ch != '_':
                if target_order[i] != ch:
                    return False
                if target_order[i] == 'L' and target_left_[i] > num_left_:
                    return False
                if target_order[i] == 'R' and target_right_[i] > num_right_:
                    return False
                i += 1
            else:
                num_left_ += 1
                num_right_ -= 1
        
        return True
