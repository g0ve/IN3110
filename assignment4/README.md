# How to run scripts

## 4.1-3 Python implementation (6 points)
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

## 3.2/3/4/5
* If you want to run the test. You need python-pytest.
* After you have installed pytest. You can run it like this:
```
$ pytest
```
If everything works you wil see this message 'x passed in y seconds'
