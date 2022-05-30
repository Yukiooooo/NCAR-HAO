#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:47:38 2022

@author: yxh5920
"""
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc

import os 
os.environ["CDF_LIB"] = "/Applications/cdf/cdf37_1-dist/lib"
from spacepy import pycdf

from spacepy.pybats import gitm
from netCDF4 import Dataset
import datetime

from matplotlib.pyplot import MultipleLocator

ktb = nc.Dataset('./muntinlupa.nc'); #  jrs.nc  aae

lkw = nc.Dataset('./davao.nc'); #  hua.nc    a04
#print (lkw)

for var in ktb.variables.values():
    n_ktb = ktb['dbn_nez'][:]; e_ktb = ktb['dbe_nez'][:]
    nn_ktb = ktb['dbn_geo'][:]; ee_ktb = ktb['dbe_geo'][:]

for var in lkw.variables.values():
    n_lkw = lkw['dbn_nez'][:]; e_lkw = lkw['dbe_nez'][:]
    nn_lkw = lkw['dbn_geo'][:]; ee_lkw = lkw['dbe_geo'][:]
    
### calculate the H-component
H_ktb = np.sqrt(np.square(n_ktb) + np.square(e_ktb))
H_lkw = np.sqrt(np.square(n_lkw) + np.square(e_lkw))

dn = n_lkw - n_ktb; de = e_lkw - e_ktb; dhh = np.sqrt(np.square(dn) + np.square(de))

dhh = H_lkw - H_ktb
#%%
fig, ((ax3,ax4),(ax1,ax2)) = plt.subplots(2,2,figsize=(15,5.5))
plt.subplots_adjust(wspace=0.15, hspace =0.28)

pt = np.arange(0,len(H_ktb),1)
ax1.plot(pt,H_ktb,'r',pt,H_lkw,'b',linestyle ='-.', linewidth = 1.5)
# =============================================================================
# ax2.plot(pt,H_lkw-H_ktb,'k',linestyle ='dashed', linewidth = 1.8)
# =============================================================================
ax2.plot(pt,dhh,'k',linestyle ='dashed', linewidth = 1.8)

ax3.plot(pt,n_ktb,'tomato',pt,e_ktb,'royalblue',linestyle ='dashed', linewidth = 1.5)
ax4.plot(pt,n_lkw,'tomato',pt,e_lkw,'royalblue',linestyle ='dashed', linewidth = 1.5)

for ax in [ax1,ax2,ax3,ax4]:
    x_major_locator = MultipleLocator(360); 
    ax.xaxis.set_major_locator(x_major_locator)
    y_major_locator = MultipleLocator(100); 
    ax.yaxis.set_major_locator(y_major_locator)
    ax.axhline(0,0,2880,color='seagreen',linestyle='--')
    ax.set_xlim(0,4320,2); ax.set_xlabel('UT of October 07-10 2012 (Hours)',fontsize=12.5,color="k")
    ax.set_ylabel('H (nT)',fontsize=12,color="seagreen"); ax.set_ylim(-300,200,2);
    ax.set_xticklabels((' ', '00','06','12','18','00','06','12','18','00','06','12','18','00'),fontsize=10)
    ax.legend(['northward','eastward'],frameon=False,fontsize=9.5,loc=1)
    ax.axvline(1440,0,500,color='darkgray',linestyle='--'); ax.axvline(2880,0,500,color='darkgray',linestyle='--')
    ax1.set_ylim(-50,300,2); ax2.set_ylabel('dH (nT)',fontsize=12,color="seagreen"); ax2.set_ylim(-150,50,2)
    ax1.legend(['JRS','HUA'],frameon=False,fontsize=9.5,loc=1)
    ax2.legend(['AAE - A04'],frameon=False,fontsize=9.5,loc=1)
    y1_major_locator = MultipleLocator(50); 
    ax1.yaxis.set_major_locator(y1_major_locator)
    y2_major_locator = MultipleLocator(50); 
    ax2.yaxis.set_major_locator(y2_major_locator)

ax4.set_xlabel('              ',fontsize=12.5,color="k")
   
# =============================================================================
# for ax in [ax1,ax2,ax3,ax4]:
#     x_major_locator = MultipleLocator(360); 
#     ax.xaxis.set_major_locator(x_major_locator)
#     y_major_locator = MultipleLocator(30); 
#     ax.yaxis.set_major_locator(y_major_locator)
#     ax.axhline(0,0,3440,color='seagreen',linestyle='--')
#     ax.set_xlim(0,4320,2); ax.set_xlabel('UT of October 07-10 2012 (Hours)',fontsize=12.5,color="k")
#     ax.set_ylabel('dH (nT)',fontsize=12,color="seagreen"); ax.set_ylim(-180,50,2);
#     ax.set_xticklabels((' ', '00','06','12','18','00','06','12','18','00','06','12','18','00'),fontsize=10)
#     ax.axvline(1440,0,500,color='darkgray',linestyle='--'); ax.axvline(2880,0,500,color='darkgray',linestyle='--')
# #    ax.legend(['northward','eastward'],frameon=False,fontsize=9.5,loc=1)
# =============================================================================
    
# =============================================================================
# #%%
# f=open('./davao_dh.txt','w'); dH = -H_lkw+H_ktb
# for ii,data in enumerate(dH):
#     if ii <0:
#         continue
#    
#     f.write('%10.3f' %data + '\n')
# f.close()     
# =============================================================================
    


# =============================================================================
# ktb = nc.Dataset('./muntinlupa_qt_st.nc');
# print (ktb)
# 
# lkw = nc.Dataset('./davao_qt_st.nc');
# #print (lkw)
# 
# for var in ktb.variables.values():
#     day = ktb['time_dy'][:]
#     n_ktb = ktb['dbn_nez'][:]; e_ktb = ktb['dbe_nez'][:]
#     nn_ktb = ktb['dbn_geo'][:]; ee_ktb = ktb['dbe_geo'][:]
# 
# for var in lkw.variables.values():
#     n_lkw = lkw['dbn_nez'][:]; e_lkw = lkw['dbe_nez'][:]
#     nn_lkw = lkw['dbn_geo'][:]; ee_lkw = lkw['dbe_geo'][:]
#     
# ### calculate the H-component
# H_ktb = np.sqrt(np.square(n_ktb) + np.square(e_ktb))
# H_lkw = np.sqrt(np.square(n_lkw) + np.square(e_lkw))
# 
# ### calculate the average background
# H_ktb0 = H_ktb[0:1440]; H_ktb1 = H_ktb[1440:2880]; H_ktb_bgk = np.mean((H_ktb0,H_ktb1),axis=0) 
# H_lkw0 = H_lkw[0:1440]; H_lkw1 = H_lkw[1440:2880]; H_lkw_bgk = np.mean((H_lkw0,H_lkw1),axis=0)
# 
# H_ktb_bgk = np.concatenate((H_ktb_bgk,H_ktb_bgk,H_ktb_bgk),axis=0)
# H_lkw_bgk = np.concatenate((H_lkw_bgk,H_lkw_bgk,H_lkw_bgk),axis=0)
# 
# dH = H_ktb_bgk - H_lkw_bgk
# #%%
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(15,5.5))
# plt.subplots_adjust(wspace=0.15, hspace =0.28)
# 
# pt = np.arange(0,len(H_ktb_bgk),1)
# ax1.plot(pt,-H_lkw_bgk,'tomato',pt,-H_ktb_bgk,'royalblue',linestyle ='dashed', linewidth = 1.5)
# ax2.plot(pt,dH,'k',linestyle ='dashed', linewidth = 1.8)
# 
# for ax in [ax1,ax2,ax3,ax4]:
#     x_major_locator = MultipleLocator(360); 
#     ax.xaxis.set_major_locator(x_major_locator)
#     y_major_locator = MultipleLocator(25); 
#     ax.yaxis.set_major_locator(y_major_locator)
#     ax.axhline(0,0,3440,color='seagreen',linestyle='--')
#     ax.set_xlim(0,4320,2); ax.set_xlabel('UT of October 07-10 2012 (Hours)',fontsize=12.5,color="k")
#     ax.set_ylabel('dH (nT)',fontsize=12,color="seagreen"); ax.set_ylim(-100,30,2);
#     ax.set_xticklabels((' ', '00','06','12','18','00','06','12','18','00','06','12','18','00'),fontsize=10)
#     ax.axvline(1440,0,500,color='darkgray',linestyle='--'); ax.axvline(2880,0,500,color='darkgray',linestyle='--')
# #    ax.legend(['northward','eastward'],frameon=False,fontsize=9.5,loc=1)
#     
# # =============================================================================
# # #%%
# # f=open('./davao_dh_bgk.txt','w')
# # for ii,data in enumerate(dH):
# #     if ii <0:
# #         continue
# #    
# #     f.write('%10.3f' %data + '\n')
# # f.close()     
# # =============================================================================
# =============================================================================
    
    
    
    
    
    
    
    
    
    