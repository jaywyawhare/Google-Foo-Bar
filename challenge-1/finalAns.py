from typing import List, Dict, Union


def solution(data: List[int], n: int) -> List[int]:
    map: Dict[int, int] = {}
    answer: List[int] = []

    for entry in data:
        if entry in map:
            map[entry] += 1
        else:
            map[entry] = 1

    for entry in data:
        if map[entry] <= n:
            answer.append(entry)
    return answer
