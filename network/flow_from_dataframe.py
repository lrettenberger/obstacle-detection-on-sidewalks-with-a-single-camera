import numpy as np

def flow_from_dataframe(img_data_gen, in_df, path_col, y_col,base_dir,number_of_classes, **dflow_args):
    base_dir = base_dir
    df_gen = img_data_gen.flow_from_directory(base_dir, class_mode = 'categorical',**dflow_args)
    df_gen.filenames = in_df[path_col].values
    df_gen.class_indices = np.zeros(number_of_classes) #Just to make categorical work. actual class indices do not matter.
    df_gen._filepaths = in_df[path_col].values
    df_gen.classes = np.stack(in_df[y_col].values)
    df_gen.samples = in_df.shape[0]
    df_gen.n = in_df.shape[0]
    df_gen._set_index_array()
    df_gen.directory = '' # since we have the full path
    return df_gen