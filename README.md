# darkflow-export

Python library that uses the darkflow package to export using JSON.

Focusing on cv2 to have access to the camera


## Installation

### Windows 10

Anaconda2 for Windows
- Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
- [cuda8](https://developer.nvidia.com/cuda-80-ga2-download-archive)
- [cudnn6](https://developer.nvidia.com/rdp/cudnn-download)
- add cuda8 and cudnn6 to PATH using default installation
	- `C:/Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0\bin`
	- `C:\Program Files\NVIDIA GPU Computing Toolkit\cudnn6\cuda\bin`

```{bash}
./install.bsh
```

### Linux
- [cuda8](https://developer.nvidia.com/cuda-80-ga2-download-archive)
- [cudnn6](https://developer.nvidia.com/rdp/cudnn-download)
- Add cuda8 and cudnn6 to LD_LIBRARY_PATH (Put in `.bashrc` or `.bash-profile`
	- cuda-8.0
	```{bash}
	# Cuda-8.0
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-8.0/lib64
	```
	- cuda-8.0 cuDNN6
	```{bash}
	# cuda-8.0 cuDNN6
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-cudnn6/lib64
	```
```{bash}
conda create -n darkflow-export python=3.5
source activate darkflow-export
