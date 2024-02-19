# Solution

## [Approach 1](./approach1.py):

I try to solve the problem by using the brute force approach using list comprehension and inbuilt count function. But as we know the time complexity of count function is O(n) and we are using it inside the list comprehension which is also O(n). So the overall time complexity of the solution is O(n^2).

## [Approach 2 / Final Answer](./finalAns.py):

I tried it using hash map, it stores the count of each element in the list. Then I iterate through the list and check if the count of the element is smaller than or equal to the input number. If it is, then I added the element to the result list. The time complexity of this solution is order of n (more towards 2n).