import math as mt
import numpy as np
import pandas as pd
from scipy.stats import norm


baseline = {"Cookies":40000,"Clicks":3200,"Enrollments":660,"CTP":0.08,"GConversion":0.20625,
           "Retention":0.53,"NConversion":0.109313}

baseline["Cookies"] = 5000
baseline["Clicks"]=baseline["Clicks"]*(5000/40000)
baseline["Enrollments"]=baseline["Enrollments"]*(5000/40000)
print(baseline)

GC={}
GC['d_min']=0.01
GC['p']=baseline['GConversion']
GC['n']=baseline['Clicks']
GC['sd']=round(mt.sqrt((GC['p']*(1-GC['p']))/GC['n']),4)
print(GC['sd'])


R={}
R['d_min']=0.01
R['p']=baseline['Retention']
R['n']=baseline['Enrollments']
R['sd']=round(mt.sqrt((R['p']*(1-R['p']))/R['n']),4)
print(R['sd'])

NC={}
NC['d_min']=0.0075
NC['p']=baseline['NConversion']
NC['n']=baseline['Clicks']
NC['sd']=round(mt.sqrt((NC['p']*(1-NC['p']))/NC['n']),4)
print(NC['sd'])



def get_z_score(alpha):
    return norm.ppf(alpha)


def get_sds(p,d):
    sd1=mt.sqrt(2*p*(1-p))
    sd2=mt.sqrt(p*(1-p)+(p+d)*(1-(p+d)))
    sds=[sd1,sd2]
    return sds


def get_sampSize(sds,alpha,beta,d):
    n=pow((get_z_score(1-alpha/2)*sds[0]+get_z_score(1-beta)*sds[1]),2)/pow(d,2)
    return n

GC["d"]=0.01
R["d"]=0.01
NC["d"]=0.0075


GC['sampsize']=round(get_sampSize(get_sds(GC['p'],GC['d']),0.05,0.2,GC['d']))
print(GC['sampsize'])
GC['sampsize']=round(GC['sampsize']/0.08*2)
print(GC['sampsize'])

R['sampsize']=round(get_sampSize(get_sds(R['p'],R['d']),0.05,0.2,R['d']))
print(R['sampsize'])
R['sampsize']=R['sampsize']/0.08/0.20625*2
print(R['sampsize'])

NC['sampsize']=round(get_sampSize(get_sds(NC['p'],NC['d']),0.05,0.2,NC['d']))
print(NC['sampsize'])
NC['sampsize']=NC['sampsize']/0.08*2
print(NC['sampsize'])


control=pd.read_csv("control_data.csv")
experiment=pd.read_csv("experiment_data.csv")
print(control.head())
pageviews_cont = control['Pageviews'].sum()
pageviews_exp = experiment['Pageviews'].sum()
pageviews_total=pageviews_cont+pageviews_exp
print ("number of pageviews in control:", pageviews_cont)
print ("number of Pageviewsin experiment:" ,pageviews_exp)


clicks_cont = control['Clicks'].loc[control['Enrollments'].notnull()].sum()
print(clicks_cont)
clicks_exp = experiment['Clicks'].loc[experiment['Enrollments'].notnull()].sum()
print(clicks_exp)

enrollments_cont=control['Enrollments'].sum()
enrollments_exp=experiment['Enrollments'].sum()
print(enrollments_cont)
print(enrollments_exp)
GC_cont = enrollments_cont/clicks_cont
GC_exp = enrollments_exp/clicks_exp
GC_pooled = (enrollments_cont+enrollments_exp)/(clicks_cont+clicks_exp) #d
GC_sd_pooled = mt.sqrt(GC_pooled*(1-GC_pooled)*(1/clicks_cont+1/clicks_exp))
alpha = 0.05
GC_ME = round(get_z_score(1-alpha/2)*GC_sd_pooled,4)
GC_diff = round(GC_exp-GC_cont,4)
print("The change due to the experiment is",GC_diff*100,"%")
print("Confidence Interval: [",GC_diff-GC_ME,",",GC_diff+GC_ME,"]")
print ("The change is statistically significant if the CI doesn't include 0. In that case, it is practically significant if",-GC["d_min"],"is not in the CI as well.")


payments_cont = control['Payments'].sum()
payments_exp = experiment['Payments'].sum()
print(payments_cont)
print(payments_exp)
NC_cont = payments_cont/clicks_cont
NC_exp = payments_exp/clicks_exp
NC_pooled = (payments_cont+payments_exp)/(clicks_cont+clicks_exp) #d
NC_sd_pooled = mt.sqrt(NC_pooled*(1-NC_pooled)*(1/clicks_cont+1/clicks_exp))
alpha = 0.05
NC_ME = round(get_z_score(1-alpha/2)*NC_sd_pooled,4)
NC_diff = round(NC_exp-NC_cont,4)
print("The change due to the experiment is",NC_diff*100,"%")
print("Confidence Interval: [",NC_diff-NC_ME,",",NC_diff+NC_ME,"]")
print ("The change is statistically significant if the CI doesn't include 0. In that case, it is practically significant if",NC["d_min"],"is not in the CI as well.")


import statsmodels.stats.api as sms
from math import ceil
print(GC)

effect_size = sms.proportion_effectsize(GC['p']-1.0*GC['d_min'],GC['p']+0.0*GC['d_min'])
required_n = sms.NormalIndPower().solve_power(
    effect_size,
    power = 0.8,
    alpha = 0.05,
    ratio = 1
    )
required_n = ceil(required_n)
print(effect_size, required_n)
print('required n of pageviews=',required_n/0.08*2)

import scipy.stats as stats
def two_proprotions_confint(success_a, size_a, success_b, size_b, significance = 0.05):
    prop_a = success_a / size_a
    prop_b = success_b / size_b
    pooled = (success_a+success_b)/(size_a+size_b)
    sd_pooled = mt.sqrt(pooled*(1-pooled)*(1/size_a+1/size_b))
    z = stats.norm.ppf(1 - (significance / 2))
    prop_diff = prop_b - prop_a
    confint = prop_diff + np.array([-1, 1]) * z * sd_pooled
    return prop_diff, confint
print(two_proprotions_confint(enrollments_cont, clicks_cont, enrollments_exp, clicks_exp, significance = 0.05))