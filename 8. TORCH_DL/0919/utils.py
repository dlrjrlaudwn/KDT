#모듈 로딩
# Model 관련
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset,DataLoader
import torch.optim as optim
from torchmetrics.classification import F1Score,BinaryF1Score,BinaryAccuracy
from torchmetrics.classification import BinaryConfusionMatrix
from torchinfo import summary

# Data 및 시각화 관련
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split

class dynamicModel(nn.Module):
    
    #모델 구조 설계 함수(생성자 메서드)
    def __init__(self,in_in,in_out,out_in,out_out,h_ins=[],h_outs=[]):

        #부모 클래스 생성
        super().__init__()

        #설계
        self.in_layer=nn.Linear(in_in,h_ins[0] if len(h_ins) else in_out)

        self.h_layers=nn.ModuleList()
        for idx in range(len(h_ins)):
            self.h_layers.append(nn.Linear(h_ins[idx],h_outs[idx]))
        
        self.out_layer=nn.Linear(h_outs[-1] if len(h_outs) else out_in,out_out)      

    #학습 진행 콜백 메서드
    def forward(self,x):

        #입력층
        y=self.in_layer(x)          # y = x1·w1 + x2·w2 + x3·w3 + b
        y=F.relu(y)                 # 0 <= y
        # y=F.relu(self.in_layer(x))

        #은닉층
        for linear in self.h_layers:
            y=linear(y)
            y=F.relu(y)

        #출력층
        return self.out_layer(y)

class dynamic_bcf_Model(nn.Module):
    
    #모델 구조 설계 함수(생성자 메서드)
    def __init__(self,in_in,in_out,out_in,out_out,h_ins=[],h_outs=[]):

        #부모 클래스 생성
        super().__init__()

        #설계
        self.in_layer=nn.Linear(in_in,h_ins[0] if len(h_ins) else in_out)

        self.h_layers=nn.ModuleList()
        for idx in range(len(h_ins)):
            self.h_layers.append(nn.Linear(h_ins[idx],h_outs[idx]))
        
        self.out_layer=nn.Linear(h_outs[-1] if len(h_outs) else out_in,out_out)      

    #학습 진행 콜백 메서드
    def forward(self,x):

        #입력층
        y=self.in_layer(x)          # y = x1·w1 + x2·w2 + x3·w3 + b
        y=F.relu(y)                 # 0 <= y
        # y=F.relu(self.in_layer(x))

        #은닉층
        for linear in self.h_layers:
            y=linear(y)
            y=F.relu(y)

        #출력층
        return F.sigmoid(self.out_layer(y))
    
class make_dataset(Dataset):
    def __init__(self,feature_df,target_df):
        self.feature_df=feature_df
        self.target_df=target_df

        self.n_rows=feature_df.shape[0]
        self.n_features=feature_df.shape[1]

    def __len__(self):
        return self.n_rows
    
    def __getitem__(self, index):

        #tensor화
        feature_ts=torch.FloatTensor(self.feature_df.iloc[index].values)
        target_ts=torch.FloatTensor(self.target_df.iloc[index].values)

        #feature/target 반환
        return feature_ts,target_ts
    

