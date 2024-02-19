from typing import List


def solution(data: List[int], n: int) -> List[int]:
    data = list(data)
    data = [x for x in data if data.count(x) <= n]
    return data
