# coding: utf8
'''
# -------------------------------------------------------------------------------------------------------
# TRANSFORMAÇÕES CUSTOMIZADAS ENTRE DATUM
# -------------------------------------------------------------------------------------------------------
# Description: Creates a custom geographic transformation in the default directory.
# C:\Users\[USER]\AppData\Roaming\ESRI\Desktop[VERSION]\ArcToolbox\CustomTransformations
'''

# -------------------------------------------------------------------------------------------------------
# Módulos e Codificação
import os
import sys
import numpy as np
import arcpy

reload(sys)
sys.setdefaultencoding('utf8')

# -------------------------------------------------------------------------------------------------------
# Variáveis de Ambiente do ArcGIS
arcpy.ResetEnvironments()
arcpy.env.overwriteOutput = True

# -------------------------------------------------------------------------------------------------------
# Table with Parameters of Datum Transformation
tab = [['Name','inGCS', 'outGCS','X', 'Y', 'Z'],\
       ['SAD69_para_WGS84','South American Datum 1969', 'WGS 1984', -66.87, +4.37, -38.52],\
       ['SAD69_para_CórregoAlegre','South American Datum 1969','Corrego Alegre', +138.70, -164.40, -34.40],\
       ['SAD69_para_SIRGAS2000', 'South American Datum 1969', 'SIRGAS 2000', -67.348, +3.879, -38.223],\
       ['SIRGAS2000_para_WGS84', 'SIRGAS 2000', 'WGS 1984', +0.478, +0.491, -0.297],\
       ['SIRGAS2000_para_CórregoAlegre', 'SIRGAS 2000', 'Corrego Alegre', +206.048, -168.279, +3.823],\
       ['CórregoAlegre_para_WGS84', 'Corrego Alegre', 'WGS 1984', -205.57, +168.77, -4.12]]

transformations = np.array(tab)
n_linhas = transformations.shape[0]

# -------------------------------------------------------------------------------------------------------
# Loop Table
for i in range(1, n_linhas):
# Informations
    print '#' * 100
    print '# Custom Transformation >> "' + transformations[i, 0] +'"'
    print 'From "' + transformations[i, 1] + '" to "' + transformations[i, 2] + '"'
    print 'With X=' + transformations[i, 3] + \
          ', Y=' + transformations[i, 4] + \
          ' and Z=' + transformations[i, 5]    

# Transformation Looping
    try:
        # Name of Custom Geographic Transformation
        geoTransfmName = transformations[i, 0]
        
        # Create a Spatial Reference Objects (Input/Output)
        inGCS = arcpy.SpatialReference(transformations[i, 1])
        outGCS = arcpy.SpatialReference(transformations[i, 2])
        
        # Custom Transformation
        customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],\
                PARAMETER['X_Axis_Translation',"+str(transformations[i, 3])+"],\
                PARAMETER['Y_Axis_Translation',"+str(transformations[i, 4])+"],\
                PARAMETER['Z_Axis_Translation',"+str(transformations[i, 5])+"]]"
        
        arcpy.CreateCustomGeoTransformation_management(geoTransfmName,
                                                       inGCS, outGCS,
                                                       customGeoTransfm)
        
        print 'Done... '
        
    except arcpy.ExecuteError:
        print arcpy.GetMessages()


# -------------------------------------------------------------------------------------------------------
# Finalizando
arcpy.ResetEnvironments()
print '# ' + '-' * 100
print '# End'

