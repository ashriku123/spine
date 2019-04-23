from nipype.interfaces import fsl
from cleaning import cleanUp
from execute import volume_calc
import shutil
import sys
import os

def fsl_run(images_path,output_path):
    first = fsl.FIRST()
    file_names = os.listdir(images_path)

    #iterating over given path
    for image in range(len(file_names)):
        shutil.copy(images_path + "/" + file_names[image], output_path)
        first.inputs.in_file = output_path + "/" + file_names[image]
        output_file_name = str(file_names[image]) + 'output.nii'
        first.inputs.out_file = output_path + "/" + output_file_name
        output_log = str(file_names[image])+'output'
        try:
            print("Running " + file_names[image])
            res = first.run()
        except Exception as e:
            print("Error running - " + file_names[image])

        print("Cleaning up unnecessary files of - " + file_names[image])
        cleanUp(output_path,output_log)
        print("Calculating Volumed for each region of - " + output_file_name)
        volume_calc(output_path + "/" + output_file_name)

if __name__ == '__main__':
    path = sys.argv[0]

    if(os.path.isdir("/MRI-Output") == False):
        os.mkdir("MRI-Output")
    if (os.path.isdir("/MRI-Input") == False):
        os.mkdir("MRI-Intput")

    images_path = str(path)+'/MRI-Input'
    output_path = str(path)+'/MRI-Output'
    fsl_run(images_path, output_path)