Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> data = list()
>>> data = [10, 45.44, "Hello"]
>>> data = []
>>> dir(data)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
data.append(10)
data
[10]
data.append(15)
data
[10, 15]
data.append(5)
data
[10, 15, 5]
data.append(9)
data
[10, 15, 5, 9]
data.append(9,3,6,7,2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data.append(9,3,6,7,2)
TypeError: list.append() takes exactly one argument (5 given)
data.append([9,3,6,7,2])
data
[10, 15, 5, 9, [9, 3, 6, 7, 2]]
data[0]
10
data[-1]
[9, 3, 6, 7, 2]
data.pop()
[9, 3, 6, 7, 2]
data
[10, 15, 5, 9]
data.extend([9,3,6,7,2])
data
[10, 15, 5, 9, 9, 3, 6, 7, 2]
data.pop()
2
data
[10, 15, 5, 9, 9, 3, 6, 7]
data.pop(4)
9
data.remove(2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data.remove(2)
ValueError: list.remove(x): x not in list
data.remove(9)
data
[10, 15, 5, 3, 6, 7]
data.insert(3,11)
data
[10, 15, 5, 11, 3, 6, 7]
data.count(7)
1
data.index(3)
4
data
[10, 15, 5, 11, 3, 6, 7]
data.reverse()
data
[7, 6, 3, 11, 5, 15, 10]
sorted(data)
[3, 5, 6, 7, 10, 11, 15]
data
[7, 6, 3, 11, 5, 15, 10]
data.sort()
data
[3, 5, 6, 7, 10, 11, 15]
data.sort(reverse=True)
for i in range(len(data)):
    print(i, data[i])

    
0 15
1 11
2 10
3 7
4 6
5 5
6 3
for i in data:
    print(i)

    
15
11
10
7
6
5
3
data = [[101, "John"], [102, "Sam"], [103, "Tom"]]
data[0]
[101, 'John']
data[1]
[102, 'Sam']
data[0][0]
101
data[0][1]
'John'
data = []
for i in range(50):
    if i % 2 == 0:
        data.append(i)

        
data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
data = [i for i in range(10)]
data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data = [i**2 for i in range(10)]
data
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
data = [i for i in range(20) if i % 2 == 0]
data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

data = 10
data = 10,
data = 10,34,5,3
data = (10,34,5,3)
data
(10, 34, 5, 3)
data[0] = 100
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    data[0] = 100
TypeError: 'tuple' object does not support item assignment
del data[0]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    del data[0]
TypeError: 'tuple' object doesn't support item deletion
data = ("John", "Sam", "Mac")
name_1, name_2, name_3 = data # unpacking
name_1
'John'
name_2
'Sam'
name_3
'Mac'
