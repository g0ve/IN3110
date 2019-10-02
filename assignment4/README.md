# How to run and use the scripts

## Programs and versions
* Python 3.7.3
* Numpy 1.16.4
* Numba 0.44.1
* OpenCV-Python 4.1.1.26

## 4.1-3+5 Python implementation (6+6+6+6 points)
How to run blur_1.py, blur_1.py and blur_3.py\
There is two ways to run these three programs. 
### 1. One by one with parameter 'inputFilename'
* blur_1.py - Python implementation
```
$ python blur_1.py [inputFilename]
```
---
* blur_2.py - Numpy implementation
```
$ python blur_2.py [inputFilename]
```
---
* blur_3.py - Numba implementation
```
$ python blur_3.py [inputFilename]
```
---
### 2. User interface 
Parameters
* (optional) inputFilename - default = beatles.jpg 
* (optional) outputFilename - deafault = blurred_image.jpg 
F.eks - Run Python implementation (blur_1.py)
```
$ python blur.py -pp -i [inputFilename] -o [outputFilename]
```
---
For more options run:
```
$ python blur.py --help
```
---
## 4.6 Packaging and unit tests (6 points)
Blur program is also availible has a package. You can install it like this:
```
$ pip install . --user
```
If you want to test if it works you can use pytest like this:
```
$ pytest
```
---
## 4.7 Blurring faces (5 bonus points)
Images used is "beatles.jpg" and outputs to "blurred_faces.jpg"\
This program take use of the package above.
```
from blur_package import blur
```
You can run the the program with:
```
$ python blur_faces.py
```
---
<sub>Never used Numpy before like me? Highly highly recommend to read this: https://www.labri.fr/perso/nrougier/from-python-to-numpy. Helped me a lot to understand how numpy works and smart ways to use it.</sub>
