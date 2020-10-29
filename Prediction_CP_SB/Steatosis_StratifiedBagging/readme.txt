The jupyter notebook for the prediction of steatosis using Stratified Bagging models.

Installation and dependencies
Anaconda (https://docs.anaconda.com/anaconda/navigator/install/) >= 1.9.12
Python >= 3.7.7
Pandas >= 1.0.3
numpy >= 1.18.1

Usage

1)	From the anaconda navigator, start the jupyter notebook and load the file ‘Steatosis_Prediction_StratifiedBagging.ipynb’ available under the folder ‘Steatosis_StratifiedBagging’
2)	Use the knime workflow ‘Descriptor_Calculation’ to calculate the following 26 physicochemical properties: SlogP, SMR, LabuteASA, TPSA, AMW, ExactMW, NumLipinskiHBA, NumLipinskiHBD, NumRotatableBonds, NumHBD, NumHBA, NumAmideBonds, NumHeteroAtoms, NumHeavyAtoms, NumAtoms, NumRings, NumAromaticRings, NumSaturatedRings, NumAliphaticRings, NumAromaticHeterocycles, NumSaturatedHeterocycles, NumAliphaticHeterocycles, NumAromaticCarbocycles, NumSaturatedCarbocycles, NumAliphaticCarbocycles, FractionCSP3.
3)	Place the generated file with the calculated descriptor in the folder ‘test_data’. A sample file is available (sample_test_file.csv) .
4)	In the jupyter notebook Steatosis_Prediction_StratifiedBagging.ipynb’, change the name of the test file (3rd cell; #Path to the test file)
5)	Execute the notebook.
6)	The steatosis prediction using our Stratified Bagging models will be saved in the ‘output_predictions’ folder.
