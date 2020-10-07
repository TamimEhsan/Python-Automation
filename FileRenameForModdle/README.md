# File Rename Using Python

It is a simple python script to rename unordered files with specific substring to a sorted order. It uses KMP string matching algorithm to find the matching substring in O(n) time thus very efficient. And renames then with the matching pattern with arbitrary suffix. 
example: if the filename is: example1805000.txt and the substring is 1805 and the character number to be taken be 7, then the changed name will be 1805000_example.txt. 
Also by simply editing the py file it can be chaned to as like 1805022_example1805000.txt 

## Working Procedure:

### Saving the path
 At first copy the path of the folder in which the files to be rename are saved. \
 
![Image of Selection](https://github.com/TamimEhsan/Python-Automation/blob/master/FileRenameForModdle/Assets/Selecting%20path.gif)

### Giving Inputs

Then you need to run .py file by any python IDE or cmd and provide the asked informations

Path: Path where the files are saved \
Substring: if we need to rename files with name 1805xyz then the common identifier will be 1805
character count: The total number of characters to be taken. ie for 1805xyz it is 7

![Image of process](https://github.com/TamimEhsan/Python-Automation/blob/master/FileRenameForModdle/Assets/Process.gif)
![Image result](https://github.com/TamimEhsan/Python-Automation/blob/master/FileRenameForModdle/Assets/Snip.PNG)

### Results:

#### Before:
![Beofre Image](https://github.com/TamimEhsan/Python-Automation/blob/master/FileRenameForModdle/Assets/Before.PNG)

#### After:
![After Image](https://github.com/TamimEhsan/Python-Automation/blob/master/FileRenameForModdle/Assets/After.PNG)

### GUI

You can also use the simple GUI. This one has an extra option to rename the file in 2 way. One with original filename and the other with cut one
![Image of GUI](https://github.com/TamimEhsan/Python-Automation/blob/master/FileRenameForModdle/Assets/gui.PNG)
