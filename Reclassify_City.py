# Reclassify
# Author: Ricky Weng
# Description: This script helps to automatically reclassify land cover data in Metro Vancouver
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from arcpy import env
from arcpy.sa import *

# Call spatial extension
arcpy.CheckOutExtension("Spatial")

# Set the geoprocessing environments
arcpy.env.workspace = "C:\\Ricky\\Jenny\\Reclassify_City\\"

# Local variables:
myfile = arcpy.ListRasters("*","TIF")
print (myfile)
outFolder = "C:\\Ricky\\Jenny\\Reclassify_City\\"

# use loop to read, process, and output the data
for inRaster in myfile:
    print (inRaster)
    # set the output name for each output
    outFile = outFolder + "new"+inRaster
    # check the ouputs
    if arcpy.Exists(outFile): arcpy.Delete_management(outFile)
    # Process: Reclassify
    arcpy.gp.Reclassify_sa(inRaster, "Value", "1 1;1 2 2;2 3 3;3 4 3", outFile, "DATA")
    


