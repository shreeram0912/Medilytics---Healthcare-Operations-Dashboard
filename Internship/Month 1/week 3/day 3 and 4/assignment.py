import numpy as np
import cv2
from matplotlib import pyplot as plt

#Creating an image as a NumPy array
img = np.random.randint(0,125,(3,3,3), dtype = np.uint8)
print(img)
print("Image Shape:", img.shape)

plt.imshow(img)
plt.axis('off')
plt.title("random image using NumPy library + matplotlib")
plt.show()


