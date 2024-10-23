import os.path              # 파일 및 폴더 관련
import cgi,cgitb            # cgi 프로그래밍 관련
from pydoc import html      # html 코드 관련 : html을 객체로 처리?

import sys, os
import pandas as pd
from joblib import load
import io
import joblib

# 환경 변수로 UTF-8 인코딩 설정
os.environ["PYTHONIOENCODING"] = "utf-8"

# UTF-8로 인코딩 설정
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SCRIPT_MODE = True
cgitb.enable()

def showhtml(words, msg, res_show):
    print("Content-Type: text/html; charset=utf-8", flush=True)
    print()
    print(f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <title> 🎮 게임 플랫폼 분류🎮 </title>
            <style>
            *{{
                margin: 0;
                padding:0;
            }}
            body {{
                background-color: #f2f2f2;
            }}
            div.wrap{{
                display: flex; 
                height:100vh;
                justify-content: center; 
                align-items: center;
            }}
            div.wrap_inner{{
                float:left;
                width:60%;
                max-width: 800px;
                margin:0 auto;
            }}
            div.title{{
                float:left;
                width:100%;
                text-align:center; 
                margin-bottom:30px;
                font-size:40px;
                font-weight:bold;
                font-family: "Jua", sans-serif;
            }}
            div.imgbox{{
                width:50%;
                float:left;
            }}
            div.imgbox > img {{width:95%; padding: 10px;}}

            div.mbti{{
                width:100%;
                float:left;
                padding:10px 0 10px 0;
                margin-top:30px;
                background-color:#FBF2ED;
                border:solid #CDD5C6 4px;
                font-size:30px;
                font-weight:bold;
                text-align:center;
                font-family: "Jua", sans-serif;
            }}
            div.u-list{{
                float:left;
                width:46%;
                padding:0 2% 0 2%;
            }}
            ul {{
                width:100%;
                float:left;
                list-style-type: none;
                padding: 0; 
            }}
            li {{
                width:100%;
                margin: 10px 0;
            }}
            input[type="text"] {{
                width: 90%; 
                height: 30px;
                padding: 13px; 
                border: 2px solid #ccc; 
                border-radius: 5px; 
                font-size: 16px; 
                transition: border-color 0.3s;
            }}

            input[type="submit"]{{
                width: 97%;
                height : 100px;
                border: 2px solid #A9C9D4;
                border-radius: 5px;
                background-color: #FBF2ED;
                font-size:20px;
                font-weight:bold;
                font-family: "Jua", sans-serif;
            }}            
          </style>
          <link rel="preconnect" href="https://fonts.googleapis.com">
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
          <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">
          
        </head>
        <body>
            <form>
                <div class='wrap'>
                    <div class='wrap_inner'>
                        <div class='title'> 게임 플랫폼 분류 모델 </div>
                        <div class='u-list'>
                            <ul>
                                <li><input type='text' name='word1' placeholder='북미 판매량' value="{words[0]}"></li>
                                <li><input type='text' name='word2' placeholder='유럽 판매량' value="{words[1]}"></li>
                                <li><input type='text' name='word3' placeholder='일본 판매량' value="{words[2]}"></li>
                                <li><input type='text' name='word4' placeholder='글로벌 판매량' value="{words[3]}"></li>
                                <li><input type="submit" value="분류하기"></li>
                            </ul>
                        </div>
                        <div class='imgbox'><img src='https://st3.depositphotos.com/1218550/13880/v/450/depositphotos_138809642-stock-illustration-video-game-computer-gaming-isometric.jpg'/></div>
                        """)
    if res_show:
        print(f"""
                        <div class='mbti'>{msg}</div>
                    </div>
                </div>
            </form>
        </body>
        </html>
        """)


def preprocessing(text):
    col = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales']
    test_Df = pd.DataFrame([text], columns=col)
    test_Df = test_Df.astype(float)
    return test_Df

model_paths = [os.path.join(os.path.dirname(__file__), 'models', 'model.joblib')]
model = load(model_paths[0])

form = cgi.FieldStorage()

words = [
    form.getvalue("word1", default=""),
    form.getvalue("word2", default=""),
    form.getvalue("word3", default=""),
    form.getvalue("word4", default="")
]

res_show = False
msg = ""

if all(word != "" for word in words):
    res_show = True
    df = preprocessing([float(word) for word in words])
    result = model.predict(df)
    target=['Xbox', 'PlayStation','Nintendo','기타']
    msg = f'예측 결과: {target[result[0]]}'

showhtml(words, msg, res_show)
