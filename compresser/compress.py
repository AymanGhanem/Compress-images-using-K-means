from skimage import io
from sklearn.cluster import KMeans
import numpy as np
from PIL import Image
import base64
from io import BytesIO

import matplotlib.image as ima


def compress(input, colors=2):
    img = io.imread(input)
    img_r = (img / 255.0).reshape(-1, 3)

    # Fit K-means on resized image. n_clusters is the desired number of colors
    k_colors = KMeans(n_clusters=colors).fit(img_r)
    # Assign colors to pixels based on their cluster center
    # Each row in k_colors.cluster_centers_ represents the RGB value of a cluster centroid
    # k_colors.labels_ contains the cluster that a pixel is assigned to
    # The following assigns every pixel the color of the centroid it is assigned to
    img128 = k_colors.cluster_centers_[k_colors.labels_]
    # Reshape the image back to 128x128x3 to save
    compressed_image = np.reshape(img128, (img.shape))
    compressed_image = np.uint8(255 * compressed_image)
    # Save image
    img = Image.fromarray(compressed_image, 'RGB')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    img_str = img_str.decode()
    return img_str



