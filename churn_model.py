# -*- coding: utf-8 -*-
__author__ = 'xead'
import pickle
import os
import numpy as np
import pandas as pd

class model(object):
    def __init__(self):        
        with open("./pred_file.pkl", 'rb') as pred_file:
            self.pred = pickle.load(pred_file)
        
    
    def effect(self, weight, arpu, retention_cost, retention_prob, retention_scale, retention_life_exp, fix_costs):
        
        name='pred_'+str(int(weight))
        name_prob='pred_'+str(int(weight))+'_prob'
        
        self.pred.sort_values(name_prob, ascending=False, inplace=True)

        true_pos = self.pred[(self.pred[name]==1)&(self.pred.true==1)].index[:int(40000*float(retention_scale))].shape[0]
        false_pos = self.pred[(self.pred[name]==1)&(self.pred.true==0)].index[:int(40000*float(retention_scale))].shape[0]
        
        effect1=(float(arpu)*true_pos-(true_pos+false_pos)*float(retention_cost))*float(retention_prob)*float(retention_life_exp)-float(fix_costs)        
        
        return effect1
    
    
    
    
    
    