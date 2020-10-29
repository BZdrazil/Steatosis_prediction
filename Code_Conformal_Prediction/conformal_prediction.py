#!/usr/bin/env python
 
def writeOutListsApp(filePath, dataLists, delimiter = '\t'):
    with open(filePath, 'a') as fd:
        numOfLists = len(dataLists)
        lenOfLists = len(dataLists[0])
        for lineNum in range(lenOfLists):
            tmpString = ""
            for column in range(numOfLists):
                tmpString += str(dataLists[column][lineNum]) + delimiter
            fd.write(tmpString.strip() + "\n")


import os,sys
from sklearn.ensemble import RandomForestClassifier
from nonconformist.icp import IcpClassifier
from nonconformist.nc import ProbEstClassifierNc, margin
import pandas as pd
import numpy as np
from argparse import ArgumentParser
from sklearn.utils import shuffle
import cloudpickle

parser = ArgumentParser()
parser.add_argument('-i','--infile', help='input training file')
parser.add_argument('-n','--nmodels', type=str, help='number of models (default 20 models)')
parser.add_argument('-m','--mode', type=str, choices=['t','p', 'b'], help='mode: build models, predict new data from models, both build and predict')
parser.add_argument('-s','--sep', type=str, choices=['t','c'], help='file separator: tab or comma')
parser.add_argument('-p','--predfile', help='input prediction file if mode == p')
args = parser.parse_args()

infile = args.infile
nmodels = args.nmodels
mode = args.mode
sep = args.sep
predfile = args.predfile

if infile == None or mode == None or sep == None:
    parser.print_help(sys.stderr)
    sys.exit(1)

if mode == 'p' and predfile == None or mode == 'b' and predfile == None:
    parser.print_help(sys.stderr)
    sys.exit(1)

if nmodels == None:
    nmodels = 20
nmodels = int(nmodels)

modelfile = infile +"_nonconf"+".model"
if mode != 'p':
    if os.path.isfile(modelfile):
        os.remove(modelfile)
    f= open(modelfile, mode='ab')
    cloudpickle.dump(nmodels, f)
    if sep == 't':
        data = pd.read_csv(infile, sep='\t', header = 0, index_col = None)
    if sep == 'c':
        data = pd.read_csv(infile, sep=',', header = 0, index_col = None)
    if 'name' or 'Name' or 'Molecule name' in data.columns:
        data.rename(columns={'name': 'id', 'Name': 'id', 'Molecule name': 'id'}, inplace=True)
    if 'class' in data.columns:
        data.rename(columns={'class': 'target'}, inplace=True)
    data.loc[data['target'] < 0, 'target'] = 0
    target = data['target'].values
    train = data.drop(['id'], axis=1, errors='ignore')
    train = train.drop(['dataset'], axis=1, errors='ignore')
    train = train.drop(['target'], axis=1, errors='ignore').values
    part1 = int(0.7*len(train))
    for xx in range(1, nmodels+1):
        modelfile2 = infile +"_nonconf"+"_"+str(xx)+".model"
        print ("Working on model", xx)
 
        idx = np.random.permutation(int(len(train)))
#        print (idx)
        trainset = idx[:part1]
        calset = idx[part1:]

        nc = ProbEstClassifierNc(RandomForestClassifier,margin,model_params={'n_estimators': 100})
        icp_norm = IcpClassifier(nc, condition=lambda instance: instance[1])

        icp_norm.fit(train[trainset], target[trainset])
        icp_norm.calibrate(train[calset], target[calset])
        cloudpickle.dump(icp_norm, f)
    f.close()

if mode != 't':
    if sep == 't':
        data = pd.read_csv(predfile, sep='\t', header = 0, index_col = None)
    if sep == 'c':
        data = pd.read_csv(predfile, sep=',', header = 0, index_col = None)
    if 'name' or 'Name' or 'Molecule name' in data.columns:
        data.rename(columns={'name': 'id', 'Name': 'id', 'Molecule name': 'id'}, inplace=True)
    if 'class' in data.columns:
        data.rename(columns={'class': 'target'}, inplace=True)
    data.loc[data['target'] < 0, 'target'] = 0
    labels = data['id']
    ll = len(labels)
    target = data['target'].values
    test = data.drop(['id'], axis=1, errors='ignore')
    test = test.drop(['dataset'], axis=1, errors='ignore')
    test = test.drop(['target'], axis=1, errors='ignore').values

    f= open(modelfile, mode='rb')
    nmodels_built = cloudpickle.load(f)
    print ("Models built:",  nmodels_built)
    outfile = predfile + "_nonconf_pred" + str(nmodels_built) + "sum.csv"
    f2 = open(outfile,'w')
    f2.write('id\tp-value_low_class\tp-value_high_class\tclass\tmodel\n')
    f2.close()
    if nmodels > nmodels_built:
        print ("More models ordered (",nmodels,") than the file contains. Setting the number of models to built models.")
        nmodels = nmodels_built

    for xx in range(1, nmodels+1):
        print ("Predicting from model", xx)
        modelfile2 = infile +"_nonconf"+"_"+str(xx)+".model"
        num = [xx]*ll
        icp_norm = cloudpickle.load(f)
        predicted = icp_norm.predict(test)
        predicted0 = [x[0] for x in predicted]
        predicted1 = [x[1] for x in predicted]
        writeOutListsApp(outfile, [labels, predicted0,  predicted1, target, num])
    f.close()

print (" - finished\n")
