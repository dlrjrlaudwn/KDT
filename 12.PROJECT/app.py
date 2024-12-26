from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import os
import json
from datasets import Dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling, EarlyStoppingCallback, AutoTokenizer
import torch
from safetensors.torch import load_file

#파이썬 텍스트 요약 모듈
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

app = Flask(__name__)

#모델 인스턴스 생성

from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained(r"C:\dlrj_rlaudwn\kdt\KDT-2\12.PROJECT\models\summarization_model")
tokenizer = AutoTokenizer.from_pretrained(r"C:\dlrj_rlaudwn\kdt\KDT-2\12.PROJECT\models\summarization_model")

# model = AutoModelForCausalLM.from_pretrained(r"C:\dlrj_rlaudwn\kdt\KDT-2\12.PROJECT\models\summarization_model")

# # model = load_file(r"C:\dlrj_rlaudwn\kdt\KDT-2\12.PROJECT\models\summarization_model\model.safetensors")
# tokenizer = AutoTokenizer.from_pretrained(r"C:\dlrj_rlaudwn\kdt\KDT-2\12.PROJECT\models\summarization_model")

from transformers import AutoConfig

config = AutoConfig.from_pretrained(r"C:\dlrj_rlaudwn\kdt\KDT-2\12.PROJECT\models\summarization_model")
print(config.__class__.__name__)




#파이썬 모듈 활용 ver.
def summarize(text):
    # 텍스트 파싱
    parser = PlaintextParser.from_string(text, Tokenizer('french'))
    
    # 요약기 정의
    summarizer = LsaSummarizer()
    
    # 요약 실행 (sentences_count=3 : 요약된 문장 수)
    summary = summarizer(parser.document, sentences_count=3)
    
    # 요약된 문장 반환
    return ' '.join(str(sentence) for sentence in summary)


@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    text = ""

    if request.method == 'POST':
        text = request.form.get("input_text", "").strip()

        if text:
            summary = summarize(text)
            print("summary:", {summary})

    return render_template("web.html", summary=summary, input_text=text)


# #모델 활용 ver.
# def generate_summary(text):
#     # 새로운 텍스트 요약하기
#     inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

#     # `attention_mask` 생성: 패딩된 토큰을 0으로 설정
#     attention_mask = (inputs['input_ids'] != tokenizer.pad_token_id).long()

#     # 모델과 토크나이저에서 pad_token_id를 동일하게 설정
#     tokenizer.pad_token_id = tokenizer.eos_token_id  # tokenizer의 pad_token_id를 eos_token_id로 설정
#     model.pad_token_id = tokenizer.pad_token_id  # 모델 설정에서 pad_token_id를 일치시킴

#     # 모델에서 요약 생성
#     outputs = model.generate(inputs['input_ids'], attention_mask=attention_mask, max_new_tokens=512, num_beams=4, early_stopping=True,
#                             no_repeat_ngram_size=2)  # 반복 방지

#     # 생성된 요약 출력
#     summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return summary


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     summary = ""
#     text = ""

#     if request.method == 'POST':
#         text = request.form.get("input_text", "").strip()

#         if text:
#             with torch.no_grad():
#                 summary = generate_summary(text)
#                 print("summary:", {summary})

#     return render_template("web.html", summary=summary, input_text=text)

if __name__ == '__main__':
    app.run(debug=True)
