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
    def getBallProps(self):
        print(self.__dict__)

myBall = Ball()
myBall.color = 'red'
myBall.radius = 5
myBall.weight = 10
myBall.getBallProps()

myOtherBall = Ball()
myOtherBall.shoeCount = 5

