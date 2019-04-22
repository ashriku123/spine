from nipype.interfaces import fsl

import os


#MriFile = ["sample-001.nii.gz","sample-002.nii.gz","sample-003.nii.gz","sample-004.nii.gz"]

first = fsl.FIRST()

path = "/home/nikhil/Spine/Pipeline/MRI-Output"

try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
    os.chdir(path)
else:  
    print ("Successfully created the directory %s " % path)

print(os.getcwd())
first.inputs.in_file = 'sample-001.nii.gz'
first.inputs.out_file = 'output.nii'
print("Working - 1")
try:
    res = first.run()
except Exception as e:
    print(e)



"""
for i in range(len(MriFile)):
    first.inputs.in_file = MriFile[i]
    first.inputs.out_file = 'output.nii'
    print("Working - ",i)
    try:
       res = first.run()
    except Exception as e:
       print(e)

"""
