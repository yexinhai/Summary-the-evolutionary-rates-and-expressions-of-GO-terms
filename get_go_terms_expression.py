#!/usr/bin/python

from sys import argv
import numpy as np
import scipy.stats as stats

with open (argv[1]) as expression_tab:
    list1 = expression_tab.readlines()

dict_expression = {}

for line in list1:
    if line[0] == 'P':
        line = line.strip()
        array1 = line.split('\t')
        geneid = array1[0]
        array1_pop = array1.pop(0)
        expressionlist = '\t'.join(array1)
#        print (expressionlist)
        dict_expression[geneid] = expressionlist

with open (argv[2]) as GO2genelist:
    list2 = GO2genelist.readlines()

for line in list2:
    line = line.strip()
    array2 = line.split('\t')
    GOid = array2[0]
    GOanno = array2[1]
    GOcount = array2[2]
    GObgc = array2[3]
    GOP = array2[4]
    GOQ = array2[5]
    genelist = array2[-1].split(';')
    
    expression_EE_F = []
    expression_EE_M = []
    expression_LE_F = []
    expression_LE_M = []
    expression_EL_F = []
    expression_EL_M = []
    expression_P_F = []
    expression_P_M = []
    expression_AD_F = []
    expression_AD_M = []
    expression_VC = []
    expression_VG = []
    expression_SG = []
    
    for a in genelist:
        expression_EE_F.append(dict_expression[a].split('\t')[0])
        expression_EE_M.append(dict_expression[a].split('\t')[1])
        expression_LE_F.append(dict_expression[a].split('\t')[2])
        expression_LE_M.append(dict_expression[a].split('\t')[3])
        expression_EL_F.append(dict_expression[a].split('\t')[4])
        expression_EL_M.append(dict_expression[a].split('\t')[5])
        expression_P_F.append(dict_expression[a].split('\t')[6])
        expression_P_M.append(dict_expression[a].split('\t')[7])
        expression_AD_F.append(dict_expression[a].split('\t')[8])
        expression_AD_M.append(dict_expression[a].split('\t')[9])
        expression_VC.append(dict_expression[a].split('\t')[10])
        expression_VG.append(dict_expression[a].split('\t')[11])
        expression_SG.append(dict_expression[a].split('\t')[12])
    
    expression_EE_F_arr = np.array(expression_EE_F,dtype=float)
    expression_EE_M_arr = np.array(expression_EE_M,dtype=float)
    expression_LE_F_arr = np.array(expression_LE_F,dtype=float)
    expression_LE_M_arr = np.array(expression_LE_M,dtype=float)
    expression_EL_F_arr = np.array(expression_EL_F,dtype=float)
    expression_EL_M_arr = np.array(expression_EL_M,dtype=float)
    expression_P_F_arr = np.array(expression_P_F,dtype=float)
    expression_P_M_arr = np.array(expression_P_M,dtype=float)
    expression_AD_F_arr = np.array(expression_AD_F,dtype=float)
    expression_AD_M_arr = np.array(expression_AD_M,dtype=float)
    expression_VC_arr = np.array(expression_VC,dtype=float)
    expression_VG_arr = np.array(expression_VG,dtype=float)
    expression_SG_arr = np.array(expression_SG,dtype=float)

    print (str(GOid) + '\t' + str(GOanno) + '\t' + str(GOcount) + '\t' + str(GOP) + '\t' + str(np.median(expression_EE_F_arr)) + '\t' + str(np.median(expression_EE_M_arr)) + '\t' + str(np.median(expression_LE_F_arr)) + '\t' + str(np.median(expression_LE_M_arr)) + '\t' + str(np.median(expression_EL_F_arr)) + '\t' + str(np.median(expression_EL_M_arr)) + '\t' + str(np.median(expression_P_F_arr)) + '\t' + str(np.median(expression_P_M_arr)) + '\t' + str(np.median(expression_AD_F_arr)) + '\t' + str(np.median(expression_AD_M_arr)) + '\t' + str(np.median(expression_VC_arr)) + '\t' + str(np.median(expression_VG_arr)) + '\t' + str(np.median(expression_SG_arr)))


