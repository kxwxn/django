class Circle():

      pi=3.14

      def __init__(self,radius=1):
            self.radius=radius

      def area(self):
            return self.radius * self.radius * self.pi 
      
      def perimeter(self):
            return 2 * Circle.pi * self.radius
      
      def multiply_radius(self,number):
            self.radius *= number # self.radius = self.radius * number
            print(f"Radius has been changed to {self.radius}")


my_circle = Circle(radius=4)

print(my_circle.area())
print(my_circle.perimeter())








