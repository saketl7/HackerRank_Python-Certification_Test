class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

def area (self):
    return self.length*self.width

class Circle:
    def __init__(self, radius): 
        self.radius=radious 
    def area (self):
        return math.pi*(self.radius**2)

if __name__ == '_main_':
    fptr = open (os.environ['OUTPUT PATH'], 'w')
    q = int(raw_input())
    queries =[]
    for _ in xrange (q) :
        args = raw_input().split() 
        shape_name, params = args[0], map(int, args[1:])
        if shape_name == "rectangle" :
            a, b = params [0], params [1] 
            shape = Rectangle (a, b)
        elif shape_name == "circle":
            r = params [0]
            shape = Circle(r)
        else:
            raise ValueError ("invalid shape type")
        fptr.write ("%.2f\n" % shape.area())
    fptr.close()