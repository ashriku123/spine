from radiomics import featureextractor
import SimpleITK as sitk
import json
import os

def volume_calc(imageName):

    #Load MRI image data from ITK
    json_output = "JSON-Output"
    if (os.path.isdir(json_output) == False):
        os.mkdir(json_output)
    img = sitk.ReadImage(imageName)
    file_name = imageName.split("/")[2]

    #casting the image so that the pixel dimesions all match with each other
    img_mask = sitk.Cast(img , sitk.sitkUInt8)
    img = sitk.Cast(img, sitk.sitkFloat32)
    corrector = sitk.N4BiasFieldCorrectionImageFilter()

    #corrector is used so that there is an equation of the dimensions
    img_c = corrector.Execute(img, img_mask)
    #img_c = corrector.Execute(img)

    #params = os.path.join(dataDir, "bin", "Params.yaml")
    #specify the parameters for the program to execute(Pyradiomics)
    params="Params.yaml"

    #Setting up model to extract features
    extractor = featureextractor.RadiomicsFeaturesExtractor(params)

    #check configuration
    print('Extraction parameters:\n\t', extractor.settings)
    print('Enabled filters:\n\t', extractor._enabledImagetypes)
    print('Enabled features:\n\t', extractor._enabledFeatures)

    #Hippocampus ROI
    hippocampus = extractor.execute(img, img_mask, label=53)
    save(json_output, hippocampus, "hippocampus", file_name)

    #Thalamus
    thalamus=extractor.execute(img, img_mask, label=10)
    save(json_output, thalamus, "thalamus", file_name)

    '''
    #Sample output
    print('Result type:', type(thalamus))  # result is returned in a Python ordered dictionary)
    print('')
    print('Calculated features for Label 6')
    for key, value in thalamus.items():
        print('\t', key, ':', value)
    '''

    #Caudate
    caudate=extractor.execute(img, img_mask, label=11)
    save(json_output,caudate,"caudate",file_name)

    #Putamen
    putamen=extractor.execute(img, img_mask, label=12)
    save(json_output, putamen, "putamen", file_name)

    #Pallidum
    pallidum=extractor.execute(img, img_mask, label=13)
    save(json_output, pallidum, "pallidum", file_name)

#Function to save json file
def save(json_output,dic,name,file_name):
    if (os.path.isdir(json_output+"/"+file_name) == False):
        os.mkdir(json_output+"/"+file_name)
    output=json_output + name+'.json'
    with open(output, 'w') as outfile:
        json.dump(dic, outfile)




