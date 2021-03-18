Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tutle
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import tutle
ModuleNotFoundError: No module named 'tutle'
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('turtle')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.back(200)
>>> tao.foward(200)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tao.foward(200)
AttributeError: 'Turtle' object has no attribute 'foward'
>>> tao.forward(400)
>>> tao.right(90)
>>> tao.right(90)
>>> tao.right(90)
>>> tao.forward(200)
>>> tao.left(90)
>>> tao.forward(200)
>>> tao.right(90)
>>> tao.left(180)
>>> tao.forward(200)
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)

	
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)

	
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(5):
	print(i+1)

	
1
2
3
4
5
>>> for i in [10,50,90]:
	print(i)

	
10
50
90
>>> tao.reset()
>>> for i in range(4)
SyntaxError: invalid syntax
>>> for i in range(4)
SyntaxError: invalid syntax
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)
	print('No.',i+1)

	
No. 1
No. 2
No. 3
No. 4
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No.',i+1)

	
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
No. 8
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No.',i+1)

	
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
No. 8

>>> for i in range(4):
	for j in range(8):
	    tao.forward(100)
	    tao.left(45)   
	print('8เหลียมรูปที่',i+1)

	
8เหลียมรูปที่ 1
8เหลียมรูปที่ 2
8เหลียมรูปที่ 3
8เหลียมรูปที่ 4
>>> for i in range(4):
	for j in range(8):
	    tao.forward(100)
	    tao.left(45)
	print('8เหลียมรูปที่',i+1)
	tao.left(90)

	
8เหลียมรูปที่ 1
8เหลียมรูปที่ 2
8เหลียมรูปที่ 3
8เหลียมรูปที่ 4
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
	    tao.forward(100)
	    tao.left(45)
	print('8เหลียมรูปที่',i+1)
	tao.left(180)

	
8เหลียมรูปที่ 1
8เหลียมรูปที่ 2
8เหลียมรูปที่ 3
8เหลียมรูปที่ 4

>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
	    tao.forward(100)
	    tao.left(45)
	print('8เหลียมรูปที่',i+1)
	tao.left(135)

	
8เหลียมรูปที่ 1
8เหลียมรูปที่ 2
8เหลียมรูปที่ 3
8เหลียมรูปที่ 4

>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
	    tao.forward(100)
	    tao.left(45)
	print('8เหลียมรูปที่',i+1)
	tao.left(135)

	
8เหลียมรูปที่ 1
8เหลียมรูปที่ 2
8เหลียมรูปที่ 3
8เหลียมรูปที่ 4

>>> tao.reset()
>>> for i in range(10):
	for j in range(8):
	    tao.forward(100)
	    tao.left(45)
	print('8เหลียมรูปที่',i+1)
	tao.left(36)

	
8เหลียมรูปที่ 1
8เหลียมรูปที่ 2
8เหลียมรูปที่ 3
8เหลียมรูปที่ 4
8เหลียมรูปที่ 5
8เหลียมรูปที่ 6
8เหลียมรูปที่ 7
8เหลียมรูปที่ 8
8เหลียมรูปที่ 9
8เหลียมรูปที่ 10

>>> tao.reset()
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> regtangle()
>>> for i in range(10):
	regtangle()
	tao.left(36)

	

>>> 
