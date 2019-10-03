import numpy as np
import cv2

from blur_package import blur



def test_max_sum_decreased():
    """
    This test checks if the max value/total sum of an random array has decreased
    after being blurred.
    """
    test_array = np.random.randint(0, 255, size=((250, 250, 3)), dtype=np.uint32)

    image = test_array.copy()
    image = blur(test_array, image)

    assert np.sum(image) < np.sum(test_array)


def test_pixel_is_average_neighbors():
    """
    This tests choose a pixel and assert that the pixel in the blurred
    image is the average of its neighbors in the clear image(a).
    """
    test_array = np.random.randint(0, 255, size=((250, 250, 3)), dtype=np.uint32)

    image = test_array.copy()
    image = blur(test_array, image)

    x = 4
    y = 3
    z = 2
    a = (test_array[x, y, z]
    + test_array[x-1, y, z]
    + test_array[x+1, y, z]
    + test_array[x, y-1, z]
    + test_array[x, y+1, z]
    + test_array[x-1, y-1, z]
    + test_array[x-1, y+1, z]
    + test_array[x+1, y-1, z]
    + test_array[x+1, y+1, z]) // 9

    assert image[x,y,z] == a