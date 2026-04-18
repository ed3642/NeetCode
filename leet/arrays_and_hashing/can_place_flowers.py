class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        def can_plant(pos):
            if pos == 0:
                if flowerbed[pos + 1] == 0:
                    return True
            elif pos == len(flowerbed) -1:
                if flowerbed[pos - 1] == 0:
                    return True
            else:
                return (flowerbed[pos - 1] == 0 and flowerbed[pos + 1] == 0)
            return False

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        planted = 0
        i = 0
        while i < len(flowerbed):
            pot = flowerbed[i]
            if pot == 1:
                i += 1 # can double jump if its already occupied
            else:
                if can_plant(i):
                    planted += 1
                    i += 1 # can double jump if we just planted one
            i += 1
                
        return planted >= n