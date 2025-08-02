# try except 는 오류가 발생하면 except 블록을 실행하고 오류가 발생하지 않으면 try 블록을 실행한다. javsscript의 try catch 와 동일하다.

try:
      print("10"+10) # 사용자가 URL에 방문
except IOError: # 사용자가 잘못된 파일을 사용
      print("You are using the wrong file")
except TypeError: # 사용자가 잘못된 데이터 타입을 사용
      print("You are using the wrong data type")
except: # 사용자에게 에러를 보고
      print("An error occurred")
finally: # 다른페이지로 이동 혹은 리프레시
      print("This will always execute")


