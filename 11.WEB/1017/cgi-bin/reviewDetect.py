# 모듈 로딩
import os.path              # 파일 및 폴더 관련
import cgi,cgitb            # cgi 프로그래밍 관련
import joblib               # AI 모델 관련
import sys, codecs          # 인코딩 관련
from pydoc import html      # html 코드 관련 : html을 객체로 처리?
import torch
import numpy as np
import sys, os
import re
import pickle
from konlpy.tag import Okt, Kkma
import string
from reviewclassifiermodel import *


# 동작관련 전역 변수
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()

# 사용자 정의 함수
def showhtml(words,msg,res_show):
    print("Content-Type: text/html; charset=utf-8")
    print("""
    
        <!DOCTYPE html>
        <html lang="ko">
         <head>
          <meta charset="UTF-8">
          <title> 🛒리뷰 분석🛒 </title>
          """+
          """
          <style>
            *{
                margin: 0;
                padding:0;
            }
            body {
                background-color: #f2f2f2;
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
            div.imgbox > img {width:95%; padding: 10px;}

            div.mbti{
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


            input[type="text"] {
                width: 90%; 
                height: 180px;
                padding: 11px; 
                border: 2px solid #ccc; 
                border-radius: 5px; 
                font-size: 16px; 
                transition: border-color 0.3s;
            }

            input[type="submit"]{
                width: 97%;
                height : 50px;
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
          <form>
          """)
    print(f"""
            <div class='wrap'>
                <div class='wrap_inner'>
                    <div class='title'> 패션제품 리뷰 분석 </div>
                    <div class='u-list'>
                        <ul>
                            <li><input type='text' name='word1' placeholder='리뷰 입력' value={words[0]}></li>

                            <li><input type="submit" value="분석하기"></li>
                        </ul>
                    </div>
                    <div class='imgbox'><img src='https://thumb.ac-illust.com/7b/7b5fb6f8502a9dd8fb6801ea616afa8f_t.jpeg'/></div>
    """)
    if(res_show):
        print(f"""
                    <div class='aspect'>{msg}</div>
                </div>
            </div>
          </form>
         </body>
        </html>""")
    
def load_vocab():
    vocab_path = r'C:\dlrj_rlaudwn\kdt\KDT-2\11.WEB\1017\cgi-bin\models\fashion_vocab.pkl'
    with open(vocab_path, 'rb') as f:
        vocab = pickle.load(f)
    return {token: idx for idx, token in enumerate(vocab)}

def load_stopwords():
    STOP_WORD = r'C:\dlrj_rlaudwn\kdt\KDT-2\11.WEB\1017\cgi-bin\data\stopwords.txt'
    with open(STOP_WORD, 'r', encoding='utf-8') as f:
        stop_words = set([line.strip() for line in f])
    return stop_words

def preprocess_text(text, punc):
    for p in punc:
        text = text.replace(p, '')
    text = re.sub('[^ ㄱ-ㅣ가-힣]+', ' ', text)
    return text.strip()

def split_sentences(text):
    kkma = Kkma()
    sentences = kkma.sentences(text)
    return sentences

def tokenize_and_remove_stopwords(tokenizer, texts, stop_words):
    tokens = []
    for text in texts:
        if text:  # Check if text is not empty
            morphs = tokenizer.morphs(text)
            tokens.append([token for token in morphs if token not in stop_words])
    return tokens

def encoding_ids(token_to_id, tokens, unk_id):
    return [[token_to_id.get(token, unk_id) for token in doc] for doc in tokens]

def pad_sequences(sequences, max_length, pad_value):
    padded_seqs = []
    for seq in sequences:
        seq = seq[:max_length]  # 최대 길이에 맞춤
        pad_len = max_length - len(seq)
        padded_seq = seq + [pad_value] * pad_len
        padded_seqs.append(padded_seq)
    return np.array(padded_seqs)

def analyze_review(model, sentence_tensor):
    classesd, logits = model(sentence_tensor)
    return classesd, logits

vocab=load_vocab()

review_list = ['착용감', '소재', '활용성', '디자인', '가격', '사이즈', '기능', '색상', '품질', '착화감']


model_path = r'C:\dlrj_rlaudwn\kdt\KDT-2\11.WEB\1017\cgi-bin\models\fashion_model.pt'
model = reviewClassifierModel(n_vocab=len(vocab), hidden_dim=64, embedding_dim=128, n_layers=2,n_classes=len(review_list))
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))  # 상태 사전 로드
model.eval()  # 평가 모드로 전환


model_names = ['fashion_model']
model_paths = []
models = []
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    for mod in model_names:
        model_paths.append(os.path.dirname(__file__)+ '/models/'+mod+'.pt') # 웹상에서는 절대경로만
else:
    for mod in model_names:
        model_paths.append('./models/'+mod+'.pt') 

for pat in model_paths:
    models.append(torch.load(pat, weights_only=False,map_location=torch.device('cpu')))

form = cgi.FieldStorage()

words = []
words.append(form.getvalue("word1", default=""))



res_show=False
msg =""

if not '' in words:
    res_show = True
    outputdata = []

    tokenizer = Okt()
    vocab = load_vocab()
    stop_words = load_stopwords()
    punc = string.punctuation

    sentences = split_sentences(words[0])  
    pre_sentences = [preprocess_text(sentence, punc) for sentence in sentences if sentence.strip()]
    sentence_tokens = tokenize_and_remove_stopwords(tokenizer, pre_sentences, stop_words)
    sentence_ids = encoding_ids(vocab, sentence_tokens, vocab.get('<unk>'))

    input_data = pad_sequences(sentence_ids, 25, vocab.get('<pad>'))
    sentence_tensor = torch.tensor(input_data, dtype=torch.long)

    classesd, logits = analyze_review(models[0], sentence_tensor)
    classesd = torch.argmax(classesd, dim=1)
    logits = torch.sigmoid(logits)
    classesd = classesd.tolist()
    logits = logits.tolist()

    for i in range(len(classesd)):
        print(f"Index: {classesd[i]}, Class: {review_list[classesd[i]]}")  # Debug print
        outputdata.append([review_list[classesd[i]], '긍정' if logits[i][0] > 0.5 else '부정'])


showhtml(words, msg, res_show)