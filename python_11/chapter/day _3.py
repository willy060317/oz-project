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
import requests

keyword = input("검색할 키워드를 입력해주세요 :")
url ="https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

html = requests.get(url)
print(html.text)
