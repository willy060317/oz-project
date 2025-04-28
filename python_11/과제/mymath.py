x = input("삼각형 넓이, 원의 넓이, 직육면체의 넓이중 원하는 도형을 고르시요")
if x =="삼각형":
    x_1 =int(input("높이를 입력하시오"))
    x_2 =int(input("밑변를 입력하시오"))
    print((x_1*x_2)/2)
elif x =="원":
     x_3 =int(input("반지름를 입력하시오"))
     print(x_3*x_3)
elif x =="직육면체":
     x_4 =int(input("높이를 입력하시오"))
     x_5 =int(input("밑변를 입력하시오"))
     print(x_4*x_5)