# what for
a directory to test import mechanism in python. 

# how to use
```bash
cd ..
python -m importTree.m1
```
and \_\_package\_\_ is importTree for m1, and importTree.subTree for m3
* do not run ```python -m m1.py ``` in the importTree directory, cause in this way, \_\_package\_\_ is None for m1
* tip: once use relative import from the top, it's better to delete all \_\_init\_\_.py and keep the way of relative import in sub-directory, e.g., use ```from .subTree import m3``` instead of ```from subTree import m3```

# more detail
refer to my blog:[python导包相关](https://blog.csdn.net/Hesy_H/article/details/103859841)