##### RECURSIVELY

The getit function from extract.by is a simple way to extract elements from multidimensional arrays.
```
Input:
[345,3,[2,[788,[[76899,67,[8,[452,[[[45,123,[5464545645,4566,876,88665,652]]]]]]]]]]]
```

```
Output:
[345, 3, 2, 788, 76899, 67, 8, 452, 45, 123, 5464545645, 4566, 876, 88665, 652]
```
---

##### BINARY SEARCH

The search function from binary_search.py simply updates the left / right position till the element is (not)found.
I added a simple runtime decorator to see the elapsed time. 

```
Input:
[2, 3, 8, 45, 67, 123, 345, 452, 652, 788, 876, 4566, 76899, 88665, 5464545645]
```
```
Output:
1  : 452 < 876
2  : 4566 > 876
3  : 788 < 876
876 found on index 10
runtime : 5.221366882324219e-05 sec
```
---

The search left function searches the first element in the array (if there are duplicates).

```
Input:
duplicated = [2, 2, 2, 3, 8, 8, 45, 67, 123, 123, 123, 345, 452, 652, 788, 788, 788, 876, 4566, 76899, 88665, 5464545645]
```

```
search_left(duplicated, 2)
Output:
1: 345 >= 2
2: 8 >= 2
3: 2 >= 2
4: 2 >= 2
5: 2 >= 2
2 found on index 0
runtime : 0.0002338886260986328 sec
```
```
search_left(duplicated, 788)
Output:
1: 345 < 788
2: 876 >= 788
3: 788 >= 788
4: 652 < 788
788 found on index 14
runtime : 0.00013947486877441406 sec
```

