# DiVertAnalysis
#This repository hosts files related to analysis of ANA-EXOT-2019-24-INTL.

This package is used to search for Long Lived Particles decaying in the Muon Spectrometer in the ATLAS experiment at CERN. These scripts are designed to input signal and background data and feed it through a Boosted Decision Tree (XGBoost) which hope to achieve a better efficiency than the manual cutflow (also provided in the repository). As of 4/25/2024, the model is still in development.


The data used for this model is not included in the repository due to it's size. 

The ntuple maker used is referenced on the DiVertAnalysis Gitlab page: https://gitlab.cern.ch/atlas-phys-exotics-llp-mscrid/fullrun2analysis/DiVertAnalysisR21/

To use run this model, first import your signal file into the Training Signal (Either Barrel or Endcap depending on which region of the MS Spectromoeter you are running). The background data will be run from the Training Background (The files will likely have to be concatenated since this seems to be how lxplus deals with these sorts of data).

These Training Sets will output either sig_train_barrel.csv, sig_train_endcap.csv, or bkg_train.csv

The Run either the Endcap Training Model or the Barrel Training Model to import your data file (bkg_train.csv and one of either sig_train_barrel.csv if analyzing barrel data, or sig_train_endcap.csv if analyzing endcap data). These models will train the BDT and output performance results.


If you have your own ntuples created from the gitlab repository above. If you don't have access to this data or the ntuple maker, you can work with the provided .csv files and test out the BDT, as the .csv files are just the training sets themselves.
