# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [useful functions]
'''

import pickle
def save_obj(obj, name:str ):
    with open( f"{name}.pkl", 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name:str):
    with open(f"{name}.pkl", 'rb') as f:
        return pickle.load(f)
