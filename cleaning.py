from nipype.interfaces import fsl

import os
import glob
import time
import shutil

def cleanUp(output_path, output_file):

	# Delete Dir
	#shutil.rmtree("MRI-Output" + "/" + output_file + ".logs")
	shutil.rmtree("MRI-Output" + "/" + output_file + ".logs")
	for CleanUp in glob.glob("MRI-Output"+'/*'):
		if not CleanUp.endswith('_all_fast_firstseg.nii.gz'):
			os.remove(CleanUp)
