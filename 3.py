
class complex :

    def __init__(self, real=None, image=None):
        self.x = real
        self.y = image

    def sum(self, second):
        result=complex()
        result.x= self.x + second.x
        result.y= self.y + second.y
        return result

    def sub(self, second):
        result=complex()
        result.x= self.x - second.x
        result.y= self.y - second.y
        return result


    def multiple(self, second):
        result=complex()
        result.x= self.x * second.x - self.y * second.y
        result.y= self.x * second.y - self.y * second.x
        return result

    def show(self):
        return str(self.x) +'+('+str(self.y) +')i'

r1=int(input('enter num1 : real : \t'))
i1=int(input('enter num1 : image : \t'))

r2=int(input('\n enter num2 : real : \t'))
i2=int(input('enter num2 : image : \t'))

a = complex(r1,i1)
b = complex(r2,i2)

print('\nsum: %s\tsub: %s\tmul: %s'% ( (a.sum(b)).show(), (a.sub(b)).show() , (a.multiple(b)).show() ))