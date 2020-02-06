import numpy as np
from skimage import io
import cv2

original = io.imread("https://photos.gurushots.com/unsafe/0x500/24dcb21c9fc18cee4223b2393e57d0b8/3_1f0cc53e3d4e27b38e6c8e5eb0aab858.jpg")
duplicate = io.imread("https://photos.gurushots.com/unsafe/0x500/24dcb21c9fc18cee4223b2393e57d0b8/3_1f0cc53e3d4e27b38e6c8e5eb0aab858.jpg")

if original.shape == duplicate.shape:
	print("The images have same size and channels")
	difference = cv2.subtract(original, duplicate)
	b, g, r = cv2.split(difference)
	if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
		difference = cv2.subtract(duplicate, original)
		b, g, r = cv2.split(difference)
		if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
			print("The images are completely Equal")