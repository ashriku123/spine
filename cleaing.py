from nipype.interfaces import fsl

import os
import glob
import time



cwd = '/home/nikhil/Spine/Try1'
file_path = "/home/nikhil/Spine/Try1/output-1_all_fast_firstseg.nii.gz"

while not os.path.exists(file_path):
	print("1")
	time.sleep(10)

for CleanUp in glob.glob(cwd+'/*'):
	print CleanUp
	if not CleanUp.endswith('_all_fast_firstseg.nii.gz'):
	    print("Delete")    
	    os.remove(CleanUp)

