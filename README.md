# Mass Rename OGP Output Images
### Introduction
This Python script was developed to rename several images in a single directory. Zone3 software captures images of a module being inspected with an automated CMM video micropscope. The output images have filenames that only contain timestamps and are not easily relatable to the physical features of the module. Each entry in the json file describes what channel connections are shown in the associated image. The original timestamp names are overwritten by the new json names without changing the file extensions. This script can be used to rename several files in the same directory, regardless of file extension, and is not specific to Zone3 software. This program does not account for arbitrary order, however.

The modules being inspected have two possible naming schemes, V3 and V2. While V3 cooresponds to the latest version of the module, the Python and json files were designed with flexibility to be backward and forward compatible.

### Get Images
#### This section is specific to Zone3 software and the qpf files in this repository.
- Run the first two routines to create an alignment on the module being inspected.
- Set active the appropriate routine. In the image below, the routine *before_bonding* is being utilized to perform visual inspection prior to wire bonding.
- Before running this routine, verify that the output images are going to the correct directory and edit as needed by selecting the camera button. The pencil button allows the user to edit the directory. The last three folders are determined by variables that do not need to be updated for every inspeciton:
   - *$ModuleID* is the module ID that is entered in the second step.
   - *@PROJECT* is the program name.
   - *@ROUTINE* is the routine name.
![](https://github.com/jparshook/rename-OGP-images/blob/main/Zone3.jpg)
- After making adjustments to the main directory, run the routine.
- Output images are now available in the folder generated by the routine.
  - *Images.json* can be deleted. This is used by Zone3 for archiving purposes.
![](https://github.com/jparshook/rename-OGP-images/blob/main/Zone3output.jpg)

### Running the Python Script
- Save the Python and json files in the main modules directory.
- Open a terminal window and use `cd` to navigate to the main modules directory containing the Python and json files.
- Run the Python script:
`Python.exe rename_module.py -d “{moduleID/project/routine}” -v “{module version}”`
  - For example: `Python.exe rename_module.py -d “CERN1/frontside_bonding/before_bonding” -v “V3”`
  - Try `python.exe rename_module.py -h` for a brief explanation of the inputs.
![](https://github.com/jparshook/rename-OGP-images/blob/main/renamed_output.jpg)

### General Tips
#### Terminal window navigation
- `cd` changes directory
- `cd..` Goes up one folder
- `cd C:\Users\Admin\Documents` is an absolute path change
- `cd .\GitHub` is a relative path change from the current directory
- `ls` lists everything in the current directory
- `-h` gives an explanation of each input
- The Tab button cycles through possible next directory options
#### Utilizing *names.json*
- V2 module channel names are also in *names.json*: change `“V3"` to `“V2”` in the command line input
- This json file can be modified to add more keys for different board arrangements
- The naming conventions are specific to the steps called in the Zone3 files on GitHub. Changing the order of the steps requires also manually changing the names in this json file.
