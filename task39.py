from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def traverse(candid, arr, sm):
            if sm == target:
                self.ans.append(arr)
            if sm >= target:
                return
            for i in range(len(candid)):
                traverse(candid[i:], arr + [candid[i]], sm+candid[i])
        traverse(candidates, [], 0)
        return self.ans


def main():
    a = Solution()
    answ = a.combinationSum(candidates=[2, 7, 6, 3, 5, 1], target=9)
    print(answ)


if __name__ == '__main__':
    main()