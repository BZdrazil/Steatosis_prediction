Installing:
conda install python=3 numpy pandas scikit-learn=0.17.1 cloudpickle
pip install nonconformist==1.2.5

Building models:
python conformal_prediction.py -i example.txt -n 5 -m t -s t

Predicting:
python conformal_prediction.py -i example.txt -n 5 -m p -s t -p <test-file>

Building and predicting:
python conformal_prediction.py -i example.txt -n 5 -m b -s t -p <test-file>
