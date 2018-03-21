"""
package: Images2Dataset
class: utils
Author: Rodrigo Loza
Description: Utils methods 
"""
# General purpose
import os
import sys
from tqdm import tqdm
import math
# Image manipulation
import cv2
# Tensor manipulation
import numpy as np
from numpy import r_, c_


# # General purpose
# import os
# import sys
# from tqdm import tqdm
# # Matrix manipulation
# import numpy as np
# # Data manipulation
# import pandas as pd
# # Image manipulation
# import cv2
# from PIL import Image
# # XML manipulation
# import xml.etree.cElementTree as ET
# # Regular expressions
# import re



# Global variables
RESIZE_DATASET = "Your images are too big, try to scale your data"
PROBLEM_CREATING_FOLDER = "There was a problem creating the file"
DATAFRAME_IS_NONE = "You have to convert your image dataset to a dataframe first"
VECTORS_MUST_BE_OF_EQUAL_SHAPE = "Both vectors should have the same len"
RESIZING_COMPLETE = "Resize operation is complete"
RBG2GRAY_COMPLETE = "Conversion operation from RGB to GRAY complete"
SLIDE_WINDOW_SIZE_TOO_BIG = "Slide window's size cannot be bigger than image"
STRIDE_WINDOW_SIZE_TOO_BIG = "Stride window's size cannot be bigger than image"

def getFolders(folder):
	"""
	:param folder: string that contains the name of the folder that we want to extract subfolders
	: return: list of subfolders in the folder
	"""
	pathsReturn = []
	#print(os.listdir(folder))
	for fold in os.listdir(folder):
			path = os.path.join(folder, fold)
			if os.path.isdir(path):
					pathsReturn.append(path)
			else:
					pass
	return pathsReturn

def getImages(folder):
	""" 
	:param folder: string that contains the name of the folder that we want to extract images
	: return: list of images in the folder
	"""
	filesReturn = []
	for file in os.listdir(folder):
			path = os.path.join(folder, file)
			if os.path.isfile(path):
					filesReturn.append(path)
			else:
					pass
	return filesReturn

def createFolder(folder, verbosity = False):
	"""
	:param folder: string that contains the name of the folder to be created.
									It is assumed folder contains the complete path
	: return: boolean that asserts the creation of the folder 
	"""
	if os.path.isdir(folder):
			if verbosity:
					print("Folder {} already exists".format(folder))
			return True
	else:
			try:
					os.mkdir(folder)
			except:
					raise ValueError("The folder could not be created")
					return False
			return True

def fillDictRows(dict_):
	"""
	Fill missing data points so all the values in the dictionary 
	have the same length
	:param dict_: dictionary that has the keys and values to fix
	: return: return the filled dictionary 
	"""
	keys = dict_.keys()
	size_ = []
	for key in keys:
			size_.append(len(dict_.get(key, None)))
	size_len = len(set(size_))
	if size_len > 1:
			print("Classes are not of the same size, fixing ...")
			# find the maximum
			max_rows = max(size_)
			# Fill the rest of the classes
			for key in keys:
					# If the class has less examples than the maximum, 
					# fill them 
					size_class = len(dict_.get(key, None))
					if size_class < max_rows:
							for i in range(max_rows - size_class):
									dict_[key].append(np.nan)
	return dict_