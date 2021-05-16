# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [useful functions]
'''
# ====== 保存和读取数据文件 ======
def save_obj(obj, name:str ):
    import pickle
    with open( f"{name}.pkl", 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name:str):
    import pickle
    with open(f"{name}.pkl", 'rb') as f:
        return pickle.load(f)

# ====== 按某粒度平滑数据 ======
def smooth_data( datas, numPerGroup:int ): # ->List
    """按某粒度平滑数据
    Args:
        datas : 需要被平滑的的数据
        numPerGroup : 每组数据的数量

    Returns:
        List: 分组后每组数据的均值
    """
    from more_itertools import chunked
    return chunked( sum(x)/len(x) ,numPerGroup )
