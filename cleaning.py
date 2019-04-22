from nipype.interfaces import fsl

import os
import glob
import time
import shutil

def cleanUp(output_path, output_file):

	output_path = cwd = '/home/nikhil/Spine/Try1'

	# Delete Dir
	shutil.rmtree(output_file + ".logs")

	for CleanUp in glob.glob(output_path+'/*'):
		if not CleanUp.endswith('_all_fast_firstseg.nii.gz'):
			print("Delete")
			os.remove(CleanUp)