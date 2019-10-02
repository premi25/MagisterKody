import pathlib
#----------------------------------------------------------------
from datetime import datetime
#----------------------------------------------------------------
path = pathlib.Path('C:\\')
#----------------------------------------------------------------
dt = datetime.datetime
#----------------------------------------------------------------
def addExtensionToFilename(name, extension):
    if not extension in name:
        return name+extension

    return name
	
def listOfFileLines(filepath):
    try:
        with open(filepath, 'r') as fp:
            lines = fp.readlines()

        return lines
    except IOError:
        raise IOError("Reading error")
        
def mergePathOfFile(filepath, filename):
    return pathlib.Path(str(filepath)+'\\'+filename)
	
def writeItemToCSV(item, filename, delimiter=',', filepath=path, accessmode='a'):
    filename = addExtensionToFilename(filename, '.csv')
	
    try:
        with open (mergePathOfFile(filepath, filename), accessmode) as f:
            f.write(str(item)+delimiter)
            f.write('\n')
        return True
    except IOError:
        raise IOError("Writing error")
        

def writeListItemsToCSV(List, filename, delimiter=',', filepath=path, accessmode='a'):
    filename = addExtensionToFilename(filename, '.csv')
    i = 0

    try:
        with open (mergePathOfFile(filepath, filename), accessmode) as f:
            while (i < len(List)-1):
                f.write(str(List[i])+delimiter)
                f.write('\n')
                i += 1
            f.write(str(List[-1])+delimiter)
        return True
    except IOError:
        raise IOError("Writing error")
    
def writeItemToTxtWithDateTime(item, filename, delimiter=' ', filepath=path, accessmode='a', note=''):
    filename = addExtensionToFilename(filename, '.txt')
	
    try:
        with open (mergePathOfFile(filepath, filename), accessmode) as f:
            line = str(dt.now().strftime("%Y-%m-%D %H:%M:%S")) + delimiter + note + delimiter + str(item) + delimiter
            f.write(line)
            f.write('\n')
        return True
    except IOError:
        raise IOError("Writing error")
    
"""def writeListItemsToTxtWithDateTime(List, filename, delimiter=' ', filepath=path, accessmode='a'):
    filename = addExtensionToFilename(filename, '.txt')
    i = 0

    try:
        with open (mergePathOfFile(filepath, filename), accessmode) as f:
            while (i < len(List)-1):
                f.write(str(List[i])+delimiter)
                f.write('\n')
                i += 1
            f.write(str(List[-1])+delimiter)
        return True
    except IOError:
        raise IOError("Writing error")
        return False
        """