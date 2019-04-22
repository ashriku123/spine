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

    #iterating over given path
    for i in range(len(file_Names)):
        first.inputs.in_file = file_Names[i]
        output_file_name = i+'output.nii'
        first.inputs.out_file = output_path+"/"+output_file_name

        try:
            res = first.run()
            cleanUp(output_path,output_file_name)
        except Exception as e:
            print(e)

path = os.getcwd()
fsl_run(path)