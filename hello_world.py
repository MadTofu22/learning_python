print('Hello World')
x = 1
print('x =', x)
testArr = [1, 2, 3, 4, 5]

reversedTestArr = testArr.copy().reverse()
print(testArr)
print(reversedTestArr)

def sumArray(arr):
    x = 0
    for num in arr:
        x += num
    
    if x < 10:
        print('arr sum is smaller than 10')
    else:
        print('arr summed =', x)

sumArray(testArr)
print(testArr[-3])


class Ball:
    def __init__ (self, radius):
        self.radius = radius

    def printProps(self):
        print(self.__dict__)

myBall = Ball(5)
myBall.color = 'red'
myBall.weight = 10
myBall.printProps()

class SoccerBall(Ball):
    def __init__ (self, shape):
        Ball.__init__(self, 8)
        self.shapePattern = shape

myOtherBall = SoccerBall('pentagon')
myOtherBall.printProps()