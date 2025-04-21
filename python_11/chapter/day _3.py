# # # # # str = "a b c"
# # # # # print(str.split()하지
# # # # # input()
# # # # # 안녕ㅏ세요
# # # # print("python")
# # # # print("python".find("p       ython"))
# # # print("Hello".isupper())
# # # print( "a" in "apple")
# # my_string = "jarson"
# # print(my_string[::-1])
# pip3 install requests
# import requests

# keyword = input("검색할 키워드를 입력해주세요 :")
# url ="https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

# html = requests.get(url)
# print(html.text)
# i=0
# while True:
#     i += 1
#     if i>9999999999999*9999999999999999999999999999:
#         break
# print(i)
num = 7
정답 = 0
while num != 1:
    if num%2==0:
        num = num/2
    else:
        num=num*3+1
    
    정답+= 1
print(정답)    