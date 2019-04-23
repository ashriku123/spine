from nipype.interfaces import fsl

import os
import glob
import time
import shutil

def cleanUp(output_path, output_file):

	# Delete Dir
	shutil.rmtree(output_path + "/" + output_file + ".logs")
	for CleanUp in glob.glob(output_path+'/*'):
		if not CleanUp.endswith('_all_fast_firstseg.nii.gz'):
			os.remove(CleanUp)
