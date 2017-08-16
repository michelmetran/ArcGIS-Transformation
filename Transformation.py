# Name: CreateCustomGeographicTransformation.py
# Description: Creates a custom geographic transformation in the default directory.
# http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/create-custom-geographic-transformation.htm
# Piracicaba, 19 de Setembro de 2016
# Michel Metran


# Import System Modules
import arcpy

# Set the variables
geoTransfmName = "SAD69_para_WGS84"

# Create a Spatial Reference Object for GCS Input
inGCS = arcpy.SpatialReference("South American Datum 1969")

# Create a Spatial Reference Object for GCS Output
outGCS = arcpy.SpatialReference("WGS 1984")

# Set Parameters
customGeoTransfm ="GEOGTRAN[METHOD['Geocentric_Translation'],PARAMETER['X_Axis_Translation',-66.87],PARAMETER['Y_Axis_Translation',+4.37],PARAMETER['Z_Axis_Translation',-38.52]]"

# Aplly Fuction
arcpy.CreateCustomGeoTransformation_management(geoTransfmName, inGCS, outGCS, customGeoTransfm)

# ############################################################################
# ############################################################################

# Set the variables
geoTransfmName = "SAD69_para_CorregoAlegre"

# Create a Spatial Reference Object for GCS Input
inGCS = arcpy.SpatialReference("South American Datum 1969")

# Create a Spatial Reference Object for GCS Output
outGCS = arcpy.SpatialReference("Corrego Alegre")

# Set Parameters
customGeoTransfm ="GEOGTRAN[METHOD['Geocentric_Translation'],PARAMETER['X_Axis_Translation',+138.70],PARAMETER['Y_Axis_Translation',-164.40],PARAMETER['Z_Axis_Translation',-34.40]]"

# Aplly Fuction
arcpy.CreateCustomGeoTransformation_management(geoTransfmName, inGCS, outGCS, customGeoTransfm)

# ############################################################################
# ############################################################################

# Set the variables
geoTransfmName = "SAD69_para_SIRGAS2000"

# Create a Spatial Reference Object for GCS Input
inGCS = arcpy.SpatialReference("South American Datum 1969")

# Create a Spatial Reference Object for GCS Output
outGCS = arcpy.SpatialReference("SIRGAS 2000")

# Set Parameters
customGeoTransfm ="GEOGTRAN[METHOD['Geocentric_Translation'],PARAMETER['X_Axis_Translation',-67.348],PARAMETER['Y_Axis_Translation',+3.879],PARAMETER['Z_Axis_Translation',-38.223]]"

# Aplly Fuction
arcpy.CreateCustomGeoTransformation_management(geoTransfmName, inGCS, outGCS, customGeoTransfm)

