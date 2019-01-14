# Extract by mask loop
# Author: Ricky Weng
# Description: This script helps to automatically project city of Vancouver boundary and extract area of interests
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from arcpy import env
from arcpy.sa import *

# Call spatial extension
arcpy.CheckOutExtension("Spatial")

# Set the geoprocessing environments
arcpy.env.workspace = "C:\\Ricky\\Jenny\\Data visualization\\long term imagery VAN"

# Local variables:
myfile = arcpy.ListRasters("*","TIF")
print (myfile)
outFolder = "C:\\Ricky\\Jenny\\project_extract_gif\\long term imagery VAN\\"
Van_boundary = "C:\\Ricky\\Jenny\\Data visualization\\Van_boundary\\AdminBoundary.shp"
Van_proj_boundary = "C:\\Ricky\\Jenny\\Data visualization\\Van_boundary\\Van_proj_boundary.shp"

# check the ouputs
if arcpy.Exists(Van_proj_boundary): arcpy.Delete_management(Van_proj_boundary)
# Process: Project
arcpy.Project_management(Van_boundary, Van_proj_boundary, "PROJCS['UTM_Zone_10N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['false_easting',500000.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',-123.0],PARAMETER['scale_factor',0.9996],PARAMETER['latitude_of_origin',0.0],UNIT['Meter',1.0]]", "WGS_1984_(ITRF00)_To_NAD_1983", "PROJCS['NAD_1983_UTM_Zone_10N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")

# use loop to read, process, and output the data
for inRaster in myfile:
    print (inRaster)
    # set the output name for each output
    outFile = outFolder + "Van"+inRaster
    # check the ouputs
    if arcpy.Exists(outFile): arcpy.Delete_management(outFile)
    # Process: Extract by Mask
    arcpy.gp.ExtractByMask_sa(inRaster, Van_proj_boundary, outFile)

