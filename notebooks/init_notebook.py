import os, sys
currentFolder = os.path.abspath('')
try:
    sys.path.remove(str(currentFolder))
except ValueError: # Already removed
    pass

# projectFolder = '/home/ababil/BUET/AV/Behavior Hypotheses/behavior-hypotheses/src'
projectFolder = 'D:\\AV\\Code\\behavior-hypotheses\\src'
projectFolder = 'F:/PSI-Dataset'
sys.path.append(str(projectFolder))
os.chdir(projectFolder)
print( f"current working dir{os.getcwd()}")
