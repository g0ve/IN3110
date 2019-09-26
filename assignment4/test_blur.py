import numpy as np
import blur_package
import cv2

blur_image = blur_package.blur_image



def test_max_sum_decreased():
    """

    """
    test_array = np.random.randint(0, 255, size=((250, 250, 3)), dtype=np.uint8)
    image = blur_image(test_array)

    image = image.astype ("uint8")
    cv2.imshow('image', image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    assert np.sum(image) < np.sum(test_array)


# def test_():
#     """
#
#     """
