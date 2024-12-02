Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers = list(range(1, 16))
>>> for number in numbers:
...     if number % 2 == 0:
...         print(str(number) + "is even")
...     else:
...         print(str(number) + "is odd")
... 
...         
1is odd
2is even
3is odd
4is even
5is odd
6is even
7is odd
8is even
9is odd
10is even
11is odd
12is even
13is odd
14is even
15is odd
>>> for number in numbers:
...     if number % 2 == 0:
...         print(str(number ) + "is even")
...     else:
...         print(str(number ) + "is odd")
... 
...         
1is odd
2is even
3is odd
4is even
5is odd
6is even
7is odd
8is even
9is odd
10is even
11is odd
12is even
13is odd
14is even
15is odd
for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")

        
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd
10 is even
11 is odd
12 is even
13 is odd
14 is even
15 is odd
