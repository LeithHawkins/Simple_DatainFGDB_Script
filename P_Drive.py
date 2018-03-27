import arcpy
import os

arcpy.env.workspace = "P:\LLS_Data\Working Data\Working_data.gdb"

print "This is not the best song in the world" + "\n" + "But its easy to see one and one make two , two and one make three" + "\n"

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)
        print(path)
        file = open("output.txt","a")
        file.write(path + '\n')
        file.close()

print "Close of Process'

