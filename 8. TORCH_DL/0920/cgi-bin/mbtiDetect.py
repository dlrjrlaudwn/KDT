# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
from pydoc import html # html 코드 관련 : html을 객체로 처리?
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import sys, os
from models.mlpmodel import MLPModel


# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할 수 있도록 하는 기능

# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(words, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="ko">
         <head>
          <meta charset="UTF-8">
          <title>---MBTI판별---</title>
         </head>
         <body>
          <form>
            <input type='text' name='word1' placeholder='단어입력 ㄱㄱ' value={words[0]}><br/>
            <input type='text' name='word2' placeholder='단어입력 ㄱㄱ' value={words[1]}><br/>
            <input type='text' name='word3' placeholder='단어입력 ㄱㄱ' value={words[2]}><br/>
            <input type='text' name='word4' placeholder='단어입력 ㄱㄱ' value={words[3]}><br/>
            <input type='text' name='word5' placeholder='단어입력 ㄱㄱ' value={words[4]}><br/>
            <p><input type="submit" value="mbti 진단"><Br/>[{msg}]</p>
          </form>
         </body>
        </html>""")

    
# 사용자 입력 텍스트 판별하는 함수---------------------------------------------------------------------------

def wordtoVector(text,loaded_vectorizer):
    return loaded_vectorizer.transform(text).toarray()

def detectMbti(resultWord, snmodel,c1,c2):
    score = 0
    for word in resultWord:
        dataTS = torch.FloatTensor(word)
        # 새로운 데이터에 대한 예측 즉, predict
        snmodel.eval()
        with torch.no_grad():
        #     # 추론 / 평가
            outputs = snmodel(dataTS).view(-1)
            predicted = torch.round(torch.sigmoid(outputs)) 
            score += int(predicted)
    return checkMbti(score,c1,c2)

def checkMbti(num,c1,c2):
    num = round(num / 5)
    if num: return c2
    else : return c1

# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    SN_MODEL = os.path.dirname(__file__)+ '/models/sn_model.pth' # 웹상에서는 절대경로만
    EI_MODEL = os.path.dirname(__file__)+ '/models/ei_model.pth' # 웹상에서는 절대경로만
    FT_MODEL = os.path.dirname(__file__)+ '/models/ft_model.pth' # 웹상에서는 절대경로만
    PJ_MODEL = os.path.dirname(__file__)+ '/models/pj_model.pth' # 웹상에서는 절대경로만
else:
    SN_MODEL = './models/sn_model.pth'
    
VECTOR_LINK = os.path.dirname(__file__)+ '/models/tfidf_vectorizer.pkl' # 웹상에서는 절대경로만
loaded_vectorizer = joblib.load(VECTOR_LINK)

snmodel = torch.load(SN_MODEL, weights_only=False,map_location=torch.device('cpu'))
eimodel = torch.load(EI_MODEL, weights_only=False,map_location=torch.device('cpu'))
ftmodel = torch.load(FT_MODEL, weights_only=False,map_location=torch.device('cpu'))
pjmodel = torch.load(PJ_MODEL, weights_only=False,map_location=torch.device('cpu'))

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태크 속 데이터 가져오기
words = []
words.append(form.getvalue("word1", default="").lower())
words.append(form.getvalue("word2", default="").lower())
words.append(form.getvalue("word3", default="").lower())
words.append(form.getvalue("word4", default="").lower())
words.append(form.getvalue("word5", default="").lower())
#text ="Happy New Year" # 테스트용 (쥬피터 내부)

# (3-3) 판별하기
msg =""
scores = 0
if not '' in words:
    resultWord = wordtoVector(words,loaded_vectorizer)
    msg += detectMbti(resultWord,eimodel,'E','I')
    msg += detectMbti(resultWord,snmodel,'S','N')
    msg += detectMbti(resultWord,ftmodel,'F','T')
    msg += detectMbti(resultWord,pjmodel,'P','J')
        
# (4) 사용자에게 WEB 화면 제공
showHTML(words,msg)
