#!/usr/bin/python

from sys import argv
import re
import numpy as np
import scipy.stats as stats

with open (argv[1]) as table:
    list1 = table.readlines()

with open (argv[2]) as ppup_bg:
    list_pp = ppup_bg.readlines()

ppup_bg_1 = []
for line in list_pp:
    line = line.strip()
    ppup_bg_1.append(line)

with open (argv[3]) as pven_bg:
    list_pv = pven_bg.readlines()

pven_bg_1 = []
for line in list_pv:
    line = line.strip()
    pven_bg_1.append(line)

with open (argv[4]) as pqin_bg:
    list_pq = pqin_bg.readlines()

pqin_bg_1 = []
for line in list_pq:
    line = line.strip()
    pqin_bg_1.append(line)

with open (argv[5]) as nvit_bg:
    list_nv = nvit_bg.readlines()

nvit_bg_1 = []
for line in list_nv:
    line = line.strip()
    nvit_bg_1.append(line)

for line in list1:
    line = line.strip()
    array1 = line.split('\t')
    GOid = array1[0]
    count = array1[2]
    annotation = array1[4]
    dnds = array1[5]
    array2 = dnds.split(';')
    ppup_dnds = []
    pven_dnds = []
    pqin_dnds = []
    nvit_dnds = []
    acal_dnds = []
    pvin_dnds = []
    for a in array2:
        b = re.search(r'\[(.*)\]',a).group(1)
        array3 = b.split(',')
        if float(array3[0]) < 10:
            ppup_dnds.append(array3[0])
        if float(array3[1]) < 10:
            pven_dnds.append(array3[1])
        if float(array3[2]) < 10:
            pqin_dnds.append(array3[2])
        if float(array3[3]) < 10:
            nvit_dnds.append(array3[3])
        if float(array3[4]) < 10:
            acal_dnds.append(array3[4])
        if float(array3[5]) < 10:
            pvin_dnds.append(array3[5])
    ppup_dnds_arr = np.array(ppup_dnds,dtype=float)
    pven_dnds_arr = np.array(pven_dnds,dtype=float)
    pqin_dnds_arr = np.array(pqin_dnds,dtype=float)
    nvit_dnds_arr = np.array(nvit_dnds,dtype=float)
    acal_dnds_arr = np.array(acal_dnds,dtype=float)
    pvin_dnds_arr = np.array(pvin_dnds,dtype=float)

    ppup_bg_1_arr = np.array(ppup_bg_1,dtype=float)
    pven_bg_1_arr = np.array(pven_bg_1,dtype=float)
    pqin_bg_1_arr = np.array(pqin_bg_1,dtype=float)
    nvit_bg_1_arr = np.array(nvit_bg_1,dtype=float)

    print (str(GOid) + '\t' + str(count) + '\t' + str(annotation) + '\t' + str(np.median(ppup_dnds_arr)) + '\t' + str(np.median(pven_dnds_arr)) + '\t' + str(np.median(pqin_dnds_arr)) + '\t' + str(np.median(nvit_dnds_arr)) + '\t' + str(np.median(acal_dnds_arr)) + '\t' + str(np.median(pvin_dnds_arr)) + '\t' + str(np.mean(ppup_dnds_arr)) + '\t' + str(np.mean(pven_dnds_arr)) + '\t' + str(np.mean(pqin_dnds_arr)) + '\t' + str(np.mean(nvit_dnds_arr)) + '\t' + str(np.mean(acal_dnds_arr)) + '\t' + str(np.mean(pvin_dnds_arr)) + '\t' + str(stats.mannwhitneyu(ppup_dnds_arr,ppup_bg_1_arr)) + '\t' + str(stats.mannwhitneyu(pven_dnds_arr,pven_bg_1_arr)) + '\t' + str(stats.mannwhitneyu(pqin_dnds_arr,pqin_bg_1_arr)) + '\t' + str(stats.mannwhitneyu(nvit_dnds_arr,nvit_bg_1_arr)) + '\t' + str(stats.kruskal(ppup_dnds_arr, pven_dnds_arr, pqin_dnds_arr, nvit_dnds_arr)) + '\t' + str(stats.mannwhitneyu(ppup_dnds_arr,pven_dnds_arr)) + '\t' + str(stats.mannwhitneyu(ppup_dnds_arr,nvit_dnds_arr)) + '\t' + str(stats.mannwhitneyu(pqin_dnds_arr,pven_dnds_arr))+ '\t' + str(stats.mannwhitneyu(pqin_dnds_arr,nvit_dnds_arr)) + '\t' + str(ppup_dnds) + '\t' + str(pven_dnds) + '\t' + str(pqin_dnds) + '\t' + str(nvit_dnds) + '\t' + str(acal_dnds) + '\t' + str(pvin_dnds))
