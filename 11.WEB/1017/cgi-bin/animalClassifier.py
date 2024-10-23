# 모듈 로딩
import os.path                  # 파일 및 폴더 관련
import cgi, cgitb               # cgi 프로그래밍 관련
import joblib                   # AI 모델 관련
import sys, codecs              # 인코딩 관련
from pydoc import html          # html 코드 관련 : html을 객체로 처리?
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import sys, os
from PIL import Image
from animalmodel import * 
import io


# 동작관련 전역 변수
SCRIPT_MODE = True              # Jupyter Mode : False, WEB Mode : True
cgitb.enable()                  # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 사용자 정의 함수
def showHTML(msg):
    print("Content-Type: text/html; charset=utf-8")
    print("""
        
        <!DOCTYPE html>
        <html lang="ko">
         <head>
          <meta charset="UTF-8">
          <title> 🦁 동물 분류 🦁 </title>
          """+
          """
          <style>
            *{
                margin: 0;
                padding:0;
            }
            body {
                background-color: #f2f5f8;
            }
            div.wrap{
                display: flex; 
                height:100vh;
                justify-content: center; 
                align-items: center;
            }
            div.wrap_inner{
                float:left;
                width:60%;
                max-width: 800px;
                margin:0 auto;
            }
            div.title{
                float:left;
                width:100%;
                text-align:center; 
                margin-bottom:30px;
                font-size:40px;
                font-weight:bold;
                font-family: "Jua", sans-serif;
            }
            div.imgbox{
                width:50%;
                float:left;
                
            }
            div.imgbox > img {width:100%; padding: 12px; height: 233px;}

            div.animal{
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
            }
            div.u-list{
                float:left;
                width:46%;
                padding:0 2% 0 2%;
            }
            ul {
                width:100%;
                float:left;
                list-style-type: none;
                padding: 0; 
            }
            li {
                width:100%;
                margin: 10px 0;
            }
            input[type="file"] {
                width: 90%;
                height : 120px; 
                padding: 11px; 
                border: 2px solid #ccc; 
                border-radius: 5px; 
                transition: border-color 0.3s;
            }

            input[type="submit"]{
                width: 97%;
                height : 80px;
                border: 2px solid #A9C9D4; 
                border-radius: 5px;
                background-color: #FBF2ED; 
                font-size:20px;
                font-weight:bold;
                font-family: "Jua", sans-serif;
            }
        </style>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">
        </head>
        <body>
        <form enctype="multipart/form-data" method="post">
        """)
    print(f"""
            <div class='wrap'>
                <div class='wrap_inner'>
                    <div class='title'> 동물 판별 모델 </div>
                    <div class='u-list'>
                        <ul>
                            <li><input type='file' name='file1' accept='image/*' onchange='previewImage(event)' required></li>
                            <li><input type="submit" value="검사"></li>
                        </ul>
                    </div>
                    <div class='imgbox'><img src='https://sm.ign.com/ign_kr/gallery/l/lion-king-/lion-king-trailer-comparison_fbap.jpg'></div>
                    <div class='animal'>{msg}</div>

                </div>
            </div>
        </form>
    """)
    print("""
         <script>
            function previewImage(event) {
                const preview = document.getElementById('image-preview');
                const file = event.target.files[0];

                if (file) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        preview.src = e.target.result;
                    }
                    reader.readAsDataURL(file);
                }
            }
        </script>
        </body>
        </html>
        
    """)


# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정

model_names = ['lion_model']
model_paths = []
model_file = []
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# # (2) 모델 로딩
model_paths = [os.path.join(os.path.dirname(__file__), 'models', f'{mod}.pth') for mod in model_names]

for pat in model_paths:
    with open(pat, 'rb') as f:
        model_file.append(torch.load(io.BytesIO(f.read()), map_location=torch.device('cpu')))

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

msg=''
if 'file1' not in form:
    msg = "<p>파일을 선택해주세요.</p>"

# (3-2) Form안에 textarea 태크 속 데이터 가져오기
else:
    file_field = form['file1']

    if file_field.filename:
        image = Image.open(file_field.file)
        preprocessed_image = joo_preprocessing_img(image)
        result=joo_predict_value(preprocessed_image, model_file)

        if result==1:
            msg='<p>사자입니다.</P>'

        else: msg='<p>사자가 아닙니다.</p>'
    
    else: msg='<p>올바른 파일을 업로드하세요.</p>'


#(4) 사용자에게 WEB 화면 제공

showHTML(msg)
