import numpy as np
import blur_package import blur_image

test_array = np.random.randint(0, 255, size=((250, 250, 3)), dtype=np.uint8)
image = blur_image("beatles.jpg")

def test_max_sum_decreased():
    """

    """
    assert np.sum(image) < np.sum(test_array)


# def test_():
#     """
#
#     """
