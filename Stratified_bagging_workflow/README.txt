In this folder you can find a KNIME workflow for executing ML models with Stratified bagging as a meta-classifier and semi-automatic iterative descriptor combination.


Installation and dependencies
1)	KNIME (https://www.knime.com/) >= 3.7.0
2)	Machine learning extensions
Usage
1)	Download the workflow and load it into your knime installation.
2)	Under the ‘Descriptor calculation and Merging’ double click on the ‘RDKit descriptors’ Metanode.
a.	Choose your sdf (containing descriptors, dataset: training/test and activity column: 1/0) in the ‘SDF Reader’ node. 
b.	Rename the ‘activity’ column to ‘class’ in the ‘Column Rename’ node
c.	In the ‘Column filter’ node, retain only ‘descriptor’, ‘dataset’ and ‘class’ columns.
d.	In the ‘Column Rename (Regex)’, add initial character (say ‘1’)
e.	Remove these initial from the “dataset” and ‘class’ column in the ‘Column Rename’ node.
f.	Run the ‘RDKit descriptors’ Metanode.

3)	Repeat the above steps (a-f) for other ‘Metanode’ under ‘Descriptor calculation and Merging’
4)	Under the ‘Model generation and Evaluation ‘, double click on the ‘number of minority class sample’ node and add the size of the minority class. Run the node.
5)	Double click on the ‘CSV Writer’: ‘training set’ node and add the path and name of the output file that would containing the training set accuracies for the descriptor combinations.
6)	Repeat the step 5 for the ‘CSV Writer’: ‘test set’ node. Run the node.
7)	Execute the ‘Parameter Optimization Loop End’ node
