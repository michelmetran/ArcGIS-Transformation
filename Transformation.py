# ########################################################################################
# Python Script to ArcGIS
# Description: Creates a custom geographic transformation in the default directory.
# C:\Users\[USER]\AppData\Roaming\ESRI\Desktop[VERSION]\ArcToolbox\CustomTransformations

# ########################################################################################
# Import System Modules
import os
import arcpy

# ########################################################################################
# Transformation between SAD69 to WGS84
try:
    geoTransfmName = "SAD69_para_WGS84"
    
    # Set Parameters
    x = -66.87
    y = +4.37
    z = -38.52
    
    # Create a Spatial Reference Objects (Input/Output)
    inGCS = arcpy.SpatialReference("South American Datum 1969")
    outGCS = arcpy.SpatialReference("WGS 1984")
    
    # Custom Transformation
    customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],\
            PARAMETER['X_Axis_Translation',"+str(x)+"],\
            PARAMETER['Y_Axis_Translation',"+str(y)+"],\
            PARAMETER['Z_Axis_Translation',"+str(z)+"]]"
    
    arcpy.CreateCustomGeoTransformation_management(geoTransfmName,
                                                   inGCS, outGCS,
                                                   customGeoTransfm)
    
except arcpy.ExecuteError:
    print arcpy.GetMessages()

# ########################################################################################
# Transformation between SAD69 to Córrego Alegre
try:
    geoTransfmName = "SAD69_para_CórregoAlegre"
    
    # Set Parameters
    x = +138.70
    y = -164.40
    z = -34.40
    
    # Create a Spatial Reference Objects (Input/Output)
    inGCS = arcpy.SpatialReference("South American Datum 1969")
    outGCS = arcpy.SpatialReference("Corrego Alegre")
    
    # Custom Transformation
    customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],\
            PARAMETER['X_Axis_Translation',"+str(x)+"],\
            PARAMETER['Y_Axis_Translation',"+str(y)+"],\
            PARAMETER['Z_Axis_Translation',"+str(z)+"]]"
    
    arcpy.CreateCustomGeoTransformation_management(geoTransfmName,
                                                   inGCS, outGCS,
                                                   customGeoTransfm)  

except arcpy.ExecuteError:
    print arcpy.GetMessages()
    
# ########################################################################################
# Transformation between SAD69 to SIRGAS2000
try:
    geoTransfmName = "SAD69_para_SIRGAS2000"
    
    # Set Parameters
    x = -67.348
    y = +3.879
    z = -38.223
    
    # Create a Spatial Reference Objects (Input/Output)
    inGCS = arcpy.SpatialReference("South American Datum 1969")
    outGCS = arcpy.SpatialReference("SIRGAS 2000")
    
    customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],\
            PARAMETER['X_Axis_Translation',"+str(x)+"],\
            PARAMETER['Y_Axis_Translation',"+str(y)+"],\
            PARAMETER['Z_Axis_Translation',"+str(z)+"]]"
    
    arcpy.CreateCustomGeoTransformation_management(geoTransfmName,
                                                   inGCS, outGCS,
                                                   customGeoTransfm)
    
except arcpy.ExecuteError:
    print arcpy.GetMessages()

# ########################################################################################
# Transformation between SIRGAS2000 to WGS84
try:
    geoTransfmName = "SIRGAS2000_para_WGS84"
    
    # Set Parameters
    x = +0.478
    y = +0.491
    z = -0.297
    
    # Create a Spatial Reference Objects (Input/Output)
    inGCS = arcpy.SpatialReference("SIRGAS 2000")
    outGCS = arcpy.SpatialReference("WGS 1984")
    
    customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],\
            PARAMETER['X_Axis_Translation',"+str(x)+"],\
            PARAMETER['Y_Axis_Translation',"+str(y)+"],\
            PARAMETER['Z_Axis_Translation',"+str(z)+"]]"
    
    arcpy.CreateCustomGeoTransformation_management(geoTransfmName,
                                                   inGCS, outGCS,
                                                   customGeoTransfm)
    
except arcpy.ExecuteError:
    print arcpy.GetMessages()

# ########################################################################################
# Transformation between SIRGAS2000 to Córrego Alegre
try:
    geoTransfmName = "SIRGAS2000_para_CórregoAlegre"
    
    # Set Parameters
    x = +206.048
    y = -168.279
    z = +3.823
    
    # Create a Spatial Reference Objects (Input/Output)
    inGCS = arcpy.SpatialReference("SIRGAS 2000")
    outGCS = arcpy.SpatialReference("Corrego Alegre")
    
    customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],\
            PARAMETER['X_Axis_Translation',"+str(x)+"],\
            PARAMETER['Y_Axis_Translation',"+str(y)+"],\
            PARAMETER['Z_Axis_Translation',"+str(z)+"]]"
    
    arcpy.CreateCustomGeoTransformation_management(geoTransfmName,
                                                   inGCS, outGCS,
                                                   customGeoTransfm)
    
except arcpy.ExecuteError:
    print arcpy.GetMessages()
    
# ########################################################################################
# Transformation between Córrego Alegre to WGS84
try:
    geoTransfmName = "CórregoAlegre_para_WGS84"
    
    # Set Parameters
    x = -205.57
    y = +168.77
    z = -4.12
    
    # Create a Spatial Reference Objects (Input/Output)
    inGCS = arcpy.SpatialReference("Corrego Alegre")
    outGCS = arcpy.SpatialReference("WGS 1984")
    
    customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],\
            PARAMETER['X_Axis_Translation',"+str(x)+"],\
            PARAMETER['Y_Axis_Translation',"+str(y)+"],\
            PARAMETER['Z_Axis_Translation',"+str(z)+"]]"
    
    arcpy.CreateCustomGeoTransformation_management(geoTransfmName,
                                                   inGCS, outGCS,
                                                   customGeoTransfm)
    
except arcpy.ExecuteError:
    print arcpy.GetMessages()
    
# ########################################################################################

print 'End'
