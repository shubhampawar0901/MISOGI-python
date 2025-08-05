#1.traditional loop

squares = []

for i in range(4):
    squares.append(i*i)

print(squares)

#list comprehension

squares = [ i * i for i in range(4)]

#2. with filtering

squares = [ i*i for i in range(4) if i % 2 == 0]

#3. nested loop 

squares = [(i,j) for i in range(5) if i % 2 == 0 for j in range(6) if  j % 2 == 0]