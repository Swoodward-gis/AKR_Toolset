
#CREATES FOLDERS IN THE ROOT OF A PRO PROJECT BASED ON AN ORGANIZATION-ENFORCED PROJECT FOLDER STRUCTURE
import os
import errno
import arcpy
folders = arcpy.GetParameterAsText(0)
curr = arcpy.mp.ArcGISProject("CURRENT").filePath
folder = "/".join(curr.split("\\")[:-1])+"/"

#This is the GIS project folder structure GRSM policy requires
#Edit this to meet your needs
#'Data\\Working' is where Create Standard GDB in Enforced Location in Pro Project will write the output FGDB
############
#EDIT ME
directories = ["Documents",
                   "Export",
                   "Images",
                   "Import",
                   "Data",
                   "Data\\Working",
                   "Data\\GPS",
                   "Data\\Raster",
                   "Data\\GPS\\RawData",
                   "Data\\GPS\\DataDictionary",
                   "Data\\GPS\\RawData\\BackUp",
                   "Data\\GPS\\RawData\\Base",
                   "Data\\GPS\\RawData\\Export",
                   "MapOutputs",
                   "MapOutputs\\Working",
                   "MapProjects",
                   "MapProjects\\Working"]

basedirectory = folder +'\\'
                   
def Script_Tool(Directories, BaseDirectory):
  for i in range (len (directories)):
    newDir = basedirectory + directories[i]
    try:
        os.makedirs(newDir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
           raise
        else:
           print ("\nBE CAREFUL! Directory %s already exists." % newDir)
           
      
# This is used to execute code if the file was run but not imported
if __name__ == '__main__':
    # Tool parameter accessed with GetParameter or GetParameterAsText
    
    ScriptTool(directories, basedirectory)
    
    # Update derived parameter values using arcpy.SetParameter() or arcpy.SetParameterAsText()







