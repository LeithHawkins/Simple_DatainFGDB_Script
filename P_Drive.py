import arcpy
import os

arcpy.env.workspace = "P:\LLS_Data\Working Data\Working_data.gdb"

print "Hello World"

# for path, dirs, files in os.walk(top_folder):
#     for d in dirs:
#         if not d.endswith(".gdb"):
#             continue
#         gdb_path = os.path.join(path, d)
#         print gdb_path
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)
        print(path)
        file = open("output.txt","a")
        file.write(path + '\n')
        file.close()




