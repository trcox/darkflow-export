# darkflow-export

Python library that uses the darkflow package to export using JSON. 

Focusing on cv2 to have access to the camera


## Installation

Anaconda2 for Windows
- Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
```{bash}
conda create -n darkflow-export python=3.5
source activate darkflow-export
pip install --ignore-installed --upgrade tensorflow-gpu cython
conda install -c menpo opencv3 
cd darkflow && python setup.py build_ext --inplace && pip install -e . && pip install .
```
