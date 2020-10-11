# SHOT descriptors
A python binding for a C++ implementation of SHOT descriptors.

### Installation
This implementation runs on python >= 3.7, use the following commands

##### Install Pybind11
```
pip3 install pytest 

git clone https://github.com/pybind/pybind11.git
cd pybind11
mkdir build
cd build
cmake ..

make -j8
sudo make install
```

##### Install PCL
```
sudo apt install libpcl-dev
```

##### Compile SHOT
```
cd shot
cmake .
make
```

### Usage
To compute the SHOT descriptors from a 3D point cloud, you can use:
```
import numpy as np
import shot.shot as shot

# load point cloud
pct = np.array(...)

# define hyperparameters
normal_r = 0.1
shot_r = 0.1

# compute descriptors
shot_features = shot.compute(x, normal_r, shot_r).reshape(-1, 352)
```