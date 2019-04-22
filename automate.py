from nipype.interfaces import fsl
from cleaning import cleanUp

import os

def fsl_run(images_path,output_path):
    first = fsl.FIRST()
    file_Names = os.listdir(images_path)
    images_path = path = "/home/nikhil/Spine/Pipeline/MRI-Output"

    try:
        os.mkdir(path)
    except OSError:
        #print("Creation of the directory %s failed" % path)
        os.chdir(path)
    else:
        print("Successfully created the directory %s " % path)

    print(os.getcwd())
    first.inputs.in_file = 'sample-001.nii.gz'
    first.inputs.out_file = 'output.nii'
    print("Working - 1")
    try:
        res = first.run()
    except Exception as e:
        print(e)

path = os.getcwd()
fsl_run(path)