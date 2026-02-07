#2. main_test.py 파일을 하나 더 만들어준다. (test_llm파일을 main파일로 import한다)


from test_llm import ask_llm

if __name__ == "__main__":
    question = "생성형 AI의 특징을 3가지 설명하시오"
    answer = ask_llm(prompt=question,temperature=0.3)
    print(answer)

''' 
# 다른 호출방법으로 확인할 수 있다
def main()
    question = "생성형 AI의 특징을 3가지 설명하시오"
    anser = ask_llm(promp=question,temperature=0.3)
    print(answer)

if __name__ == "__main__" :
    main()
'''