# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [useful functions]
'''
def save_obj(obj, name:str ):
    """保存和读取数据文件
    Args:
        obj ([type]): 保存的对象
        name (str): 保存的对象名字前缀 (name.pkl)
    """
    import pickle
    with open( f"{name}.pkl", 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name:str):
    import pickle
    with open(f"{name}.pkl", 'rb') as f:
        return pickle.load(f)

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

class safeContext:
    """catch exceptgion with context
    """
    def __enter__(self):
        return 1

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exc_type: %s' % exc_type)
        print('exc_value: %s' % exc_value)
        print('exc_tb: %s' % exc_tb)

def testSafeContext():
    with safeContext() as cont:
        test = open('./test','r')

def main():
    testSafeContext()

if __name__=='__main__':
    main()