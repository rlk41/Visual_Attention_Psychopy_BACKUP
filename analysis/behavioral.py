import pickle 
import pandas as pd
import h5py


pkl="/Users/richard/Visual_Attention/data/060781_DMS_et_12-36_2023-03-21_21h21.44.716_thisExp.pkl.psydat"
filename="/Users/richard/Visual_Attention/data/200002_DMS_BEST_eyetracking_DAN_base_12-36_looped_10minWORKING_2023-03-21_15h31.16.864.hdf5"
#pkl="/Users/richard/Visual_Attention/data/332117_DMS_et_12-36_2023-03-21_21h47.34.557_thisExp.pkl"
#filename=pkl.rstrip("_thisExp.pkl")+".hdf5"
filename="/Users/richard/Visual_Attention/data/570509_DMS_et_12-36_2023-03-24_10h53.14.619.hdf5"

#obj = pd.read_pickle(pkl)

objects = []
with (open(pkl, "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break


#filename = "file.hdf5"

f = h5py.File(filename, "r") 

#as f:
# Print all root level object names (aka keys) 
# these can be group or dataset names 
print("Keys: %s" % f.keys())
# get first object name/key; may or may NOT be a group
a_group_key = list(f.keys())[0]

# get the object type for a_group_key: usually group or dataset
print(type(f[a_group_key])) 

# If a_group_key is a group name, 
# this gets the object names in the group and returns as a list
data = list(f[a_group_key])

# If a_group_key is a dataset name, 
# this gets the dataset values and returns as a list
data = list(f[a_group_key])
# preferred methods to get dataset values:
ds_obj = f[a_group_key]      # returns as a h5py dataset object
ds_arr = f[a_group_key][()]  # returns as a numpy array

f['class_table_mapping']

f['data_collection']['condition_variables'].keys()
f['data_collection']['events'].keys()
f['data_collection']['experiment_meta_data']
f['data_collection']['session_meta_data']


for k in f['data_collection']['events']['eyetracker'].keys():
    print(f['data_collection']['events']['eyetracker'][k])


    
g = f['data_collection']['events']['eyetracker']["MonocularEyeSampleEvent"][()]

g = pd.DataFrame(g)

