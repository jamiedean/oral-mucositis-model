# Severe acute oral mucositis normal tissue complication probability model

Random forest classification model of severe acute oral mucositis resulting from head and neck radiotherapy.

To run the model use the PredictMucositisNtcp.py Python script. The Model folder and inputData.csv file should be in the working directory. Values for the model covariates should be entered into the inputData.csv file.

The following dependencies should be installed:

- Python version 2 (https://www.python.org/downloads/)
- numpy
- pandas
- scikit-learn
- The simplist way to install all of the necessary packages is to use a Python distribution, such as Enthought Canopy (https://www.enthought.com/products/canopy/). Other distributions are available (https://wiki.python.org/moin/PythonDistributions).  Most distributions have free versions and full versions are often free for academics. 

Details on model training and validation can be found in the article:

Normal tissue complication probability (NTCP) modelling using spatial dose metrics and machine learning methods for severe acute oral mucoositis resulting from head and neck radiotherapy. Dean  JA et al. Radiother Oncol 2016.

Please cite the above article in publications using the model.

This model is intended for research purposes only. It has not yet been externally validated and so should not be employed to make individual patient management decisions.
