from nipype.interfaces import fsl
from cleaning import cleanUp
import shutil

import os

def fsl_run(images_path,output_path):
    first = fsl.FIRST()
    file_Names = os.listdir(images_path)

    #iterating over given path
    for i in range(len(file_Names)):
    	shutil.copy(images_path+"/"+file_Names[i], output_path)
        first.inputs.in_file = output_path+"/"+file_Names[i]
        output_file_name = str(i)+'output.nii'
        first.inputs.out_file = output_path+"/"+output_file_name
        output_log = str(i)+'output'
        try:
        	print("Run - 1")
        	res = first.run()
        	print("output - 1")
        	cleanUp(output_path,output_log)
        except Exception as e:
            print(e,"------tesing")

        cleanUp(output_path,output_log)
        print("output - ",i)

path = os.getcwd()
images_path = str(path)+'/MRI-Input'
output_path = str(path)+'/MRI-Output'
fsl_run(images_path,output_path)