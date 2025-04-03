# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:55:06 2025

@author: Jiyeon Baek

student_mental_health.py
주제 :
    대학생의 인구통계학적 정보, 학업과 관련된 요소, 정신 건강과 관련된 요소 등을 분석하여 
    학생들의 정신 건강에 영향을 미치는 요인을 파악
        학생들의 정신 건강에 영향을 미치는 요인이 무엇인지를 분석하여 해결방안 제시
과제 :
    분석 결과 및 해결방안
    작업 프로젝트 및 시각화 자료 제출
        시각화 자료는  result 폴더에 저장, 압축 후 제출

"""
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 


df = pd.read_csv('C:/Users/Admin/Desktop/JY/Python/20250222-20250223/data/Student Mental health.csv')
df.info() 

