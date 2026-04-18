# https://leetcode.com/problems/minimum-number-of-people-to-teach

from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        M = len(languages)

        lang_set = [set() for _ in range(M + 1)]
        need_teach = set()

        for person in range(1, M + 1):
            lang_set[person].update(languages[person - 1])

        for _from, _to in friendships:
            if len(lang_set[_from] & lang_set[_to]) == 0:
                need_teach.add(_from)
                need_teach.add(_to)

        if not need_teach:
            return 0
        
        speakers = [0] * (n + 1)

        for person in need_teach:
            for lang in languages[person - 1]:
                speakers[lang] += 1

        # maximize already speakers in need_teach
        return len(need_teach) - max(speakers)

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        def count_need_to_teach(lang):
            count = 0

            for person in need_teach:
                if lang not in lang_set[person]:
                    count += 1
            
            return count

        M = len(languages)

        lang_set = [set() for _ in range(M + 1)]
        need_teach = set()

        for person in range(1, M + 1):
            lang_set[person].update(languages[person - 1])

        for _from, _to in friendships:
            if len(lang_set[_from] & lang_set[_to]) == 0:
                need_teach.add(_from)
                need_teach.add(_to)

        if not need_teach:
            return 0
        
        min_people = float('inf')

        for lang in range(1, n + 1):
            min_people = min(count_need_to_teach(lang), min_people)

        return min_people


    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        def get_min_people(lang):
            tought = set()

            for person in range(1, m + 1):
                for nei in al[person]:
                    if (nei not in can_talk[person] and 
                        person not in tought and 
                        lang not in lang_set[person]
                        ):
                        tought.add(person)

            return len(tought)
        
        m = len(languages)
        al = [[] for _ in range(m + 1)]
        lang_set = [set() for _ in range(m + 1)]
        can_talk = [set() for _ in range(m + 1)]

        for person in range(1, m + 1):
            lang_set[person].update(languages[person - 1])

        for _from, _to in friendships:
            al[_from].append(_to)
            al[_to].append(_from)

        for _from, _to in friendships:
            if len(lang_set[_from] & lang_set[_to]) > 0:
                can_talk[_from].add(_to)
                can_talk[_to].add(_from)
        
        min_people = float('inf')

        for lang in range(1, n + 1):
            min_people = min(get_min_people(lang), min_people)
        
        return min_people
    