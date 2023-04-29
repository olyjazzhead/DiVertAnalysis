#### ANALYSIS SCRIPT####

### This analysis script perform cutflows for ANA-EXOT-2019-24-INTL ###

##Import packages
import numpy as np
import pandas as pd
import os
import itertools
import uproot
import awkward as ak
import coffea.processor as processor
from coffea.nanoevents import NanoEventsFactory, BaseSchema
from ntuple_schema import NtupleSchema
import hist
import vector 
vector.register_awkward

import pickle
from dask_jobqueue import HTCondorCluster
from distributed import Client

import mplhep as hep
import matplotlib.pyplot as plt

from files import *


#Define useful quantities

GeV = 1000


#luminosity = 2478.52 #pb -1 ??




#Return a list of all files

def return_list_of_files():

	myfiles = {}

	for key in refdict:
		myfiles[refdict[key]["long_name"]]={'files':[]}
		for filename in refdict[key]['ntup_filenames']:
			file_loc = f"{refdict[key]['subdir']}/{filename}"

			myfiles[refdict[key]["long_name"]]['files'].append(f"{file_loc}")

	return myfiles

myfiles = return_list_of_files()
myfiles


#Concatenate background files of preselection branches of interest only

branches = [("pass_HLT_j30_muvtx_noiso"), ("hasGoodPV"), ("MSVtx_nMDT"), ("MSVtx_nRPC"),("MSVtx_nTGC"),("MSVtx_eta"),("jet_pT")]
bkg_file = uproot.concatenate("user.calpert.mc16_13TeV.361022.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W.032123_trees.root.479322611/user.calpert*.root:trees_DV_",branches)
sig_file = sig_file = uproot.open("user.calpert.mc16_13TeV.311423.MGPy8EG_A14NNPDF23_NNPDF31ME_HSS_LLP_mH600_mS150_lthigh.032123_trees.root/user.calpert.311423.e7357_e5984_s3234_r10201_r10210_p4696.32829947._000001.trees.root:trees_DV_")


##Perform Preselection

def col_accumulator(a):
	return processor.column_accumulator(np.array(a))

class MyProcessor(processor.ProcessorABC):

	def __init__(self):

		self._accumulator = processor.dict_accumulator({})
		self.setupNPArr = None

		dataset_axis = hist.axis.StrCategory(name="d_axis", label="", categories=[], growth=True)
		#### FILL IN REMAINING VARIABLES OF INTEREST LATER AND DEFINE HISTOGRAMS####

	
	# The accumulator just acts to collect the information we read from various 
    # input files and combines it into single objects, like arrays or histograms. 
	@property
	def accumulator(self):
		return self._accumulator
		

	# Since we're saving arrays, we need to make sure that we initialize said 
    # arrays before we try and fill them. This function does that.

    def setupNPArray(self,varNames):
    	varDict={}
    	for v in varNames:
    		varDict[v] = processor.column_accumulator(np.zeros(shape=(0)))
    	self._accumulator = processor.dict_accumulator(varDict)
    	self.setupNPArr = True

    def process(self, events):

    	myVars=[
    			"MSVtx_nMDT"
    			"MSVtx_nRPC"
    			"MSVtx_nTGC"
    			"MSVtx_eta"
    			"jet_pT"]
    	#### FILL IN VARIABLES OF INTEREST LATER ####

    	# Initialize arrays, if needed 
        if self.setupNPArr is None: self.setupNPArray(myVars)
        output = self.accumulator.identity()

        

        # Define our relevant objects from the schema
        trig = events.trigPassed
        prim_vertex = events.PrimVertex

        #### FILL IN VARIABLES OF INTEREST LATER ####

        

        #Check to make sure trigger was fired
        passTrigger = trig.pass_HLT_j30_muvtx_noiso

        #Check to make sure at least one primary vertex is chosen
        passPrimVertex = prim_vertex.hasGoodPV

        #We only want events that pass trigger and have good PV #### LATER ADD EVENTS THAT SATISFY OTHER CRITERIA ####
        good_events = (passTrigger & passPrimVertex)



        return{#### RETURN ALL EVENTS THAT PASS TRIGGER AND HAVE GOOD PV
        }

    def postprocess(self, accumulator):
    	return accumulator






######Simpler Version










