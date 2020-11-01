# Steatosis_prediction

In this repository we are collecting code, workflows, data, annd models associated to the paper "Combining in vivo data with in silico predictions for modeling hepatic steatosis by using stratified bagging and conformal prediction" written by S. Jain, U. Norinder, S.E. Escher, and B. Zdrazil

Code_Conformal_Prediction/
  Contains python code needed to run the conformal prediction models and an example input training file
  
Prediction_CP_SB/
  Contains models based on both meta-classifiers used: bagging with stratified under-sampling and conformal prediction
  In addition, a KNIME workflow for descriptor calculation is included (RDKit descriptors)
  
Stratified_bagging_workflow/
  Contains a KNIME workflow for automated iterative descriptor combination, model generation and execution based on bagging with stratified under-sampling as meta-   classifier
 
dataset/
  Contains the steatosis training and test data set (based on in vivo rodent measurements); the annotation as steatotic positive ("1") or negative ("0") is given ("class"), the assignement to either training or test set ("dataset"), and 26 RDKit physicochemical properties have been calculated

