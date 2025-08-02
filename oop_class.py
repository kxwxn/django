# class는 객체를 생성하는 틀이다. 객체는 클래스의 인스턴스이다. 
# 기본적으로 파이썬에서 모든 것은 객체이다. 문자열, 숫자, 리스트, 딕셔너리, 튜플, 함수, 클래스 등등.

# 클래스 정의
class NameOfClass:
      def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2

      def some_method(self):
            print(self.param1)

# 클래스 인스턴스 생성
my_object = NameOfClass("hello", "world")
print(my_object.param1)

# 클래스 상속
class NameOfClass2(NameOfClass):
      def __init__(self, param1, param2):
            super().__init__(param1, param2)
            self.param3 = param3
            


# example
class Student():
      planet= "Earth" # class object attribute
      species = "Human" # class object attribute
      def __init__(self,name,gpa): # instance attribute
            self.name=name 
            self.gpa=gpa


stu1 = Student("KW",2.2)
stu2 = Student("Teresa",4.0)

print(stu1.gpa,stu1.species)
print(stu2.name)