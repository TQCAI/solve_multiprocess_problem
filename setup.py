import pdb

from setuptools import setup, find_packages
from pathlib import Path
import os

os.system('find . -name "*.pyc" -type f -print -exec rm -rf {} \;')
os.system(f'rm -rf  build && rm -rf dist && rm -rf *.egg-info')



name="diy_module"


#conding=utf8
import os

g = os.walk(name)
lst=[]
for path,dir_list,file_list in g:
    for file_name in file_list:
        lst.append(os.path.join(path, file_name) )
# lst=list(filter(lambda x:not (x.endswith('.pyc') or x.endswith('.py')),lst))

M=len(name)+1
lst=[s[M:] for s in lst]
print(lst)
setup(
    name=name,
    version="0.0.1",
    packages=find_packages(),
    description=name,
    author="tang qichun",
    author_email="qichun.tang@xtalpi.com",
    package_data={name:lst},
    entry_points={'console_scripts': [f'{name}={name}:cli', ], }
)
#cd /home/tqc/anaconda3/envs/tf2/lib/python3.6/site-packages/scorefunc-0.0.1-py3.6.egg/scorefunc/models/rdock