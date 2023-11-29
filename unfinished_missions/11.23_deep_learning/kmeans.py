#!/usr/bin/env python
# coding: utf-8

# ### Task Specification:
# 
# 1. **Convert the Image to Two Dimensions (samples and three features):**
#    - The image should be reshaped so that each row corresponds to a pixel and each row should have three features (presumably the RGB values of the pixel).<br><br>
# 
# 2. **Compute the k Centroids:**
#    - Use the K-means algorithm to compute the k cluster centroids, where k is a pre-specified number of clusters.<br><br>
# 
# 3. **For Each Pixel (feature), Assign its Values to its Cluster:**
#    - For each pixel in the image, calculate the Euclidean distance to each of the k cluster centroids. Assign the pixel to the cluster whose centroid is closest to it. The value of the pixel should be updated to be the value of its cluster centroid.<br><br>
# 
# 4. **Reshape the Matrix to its Original Form and Display:**
#    - After all pixels have been assigned to clusters and their values have been updated to be their respective cluster centroids, reshape this matrix back to the original shape of the image and display the result.<br><br>
# 
# 5. **(The last steps have been implemented for you...)**
# 

# In[17]:


get_ipython().system('condainstall -c anaconda opencv')


# In[15]:



from matplotlib import pyplot as plt
import requests
import numpy as np
import cv2

# URL of the image to download
image_url = 'https://cdn.pixabay.com/photo/2014/08/15/11/29/beach-418742_640.jpg'

# Send a GET request to the URL
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the response
    image_data = response.content

    # Convert the image data to a NumPy array
    nparr = np.frombuffer(image_data, np.uint8)

    # Decode the image array using OpenCV
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    desired_width = 426
    desired_height = 320

    # Downsample the image
    image = cv2.resize(image, (desired_width, desired_height))

    # Display the image
    plt.figure(figsize=(7,7))
    plt.imshow(image[:,:,::-1])
    plt.show()
    
else:
    print('Failed to download the image. Status code:', response.status_code)


# In[4]:


img = image.reshape...


# In[6]:


centroids = np.array(centroids)
# Map each pixel to its corresponding cluster center
segmented_image = centroids[labels]

# Reshape the segmented image back to its original shape
segmented_image = segmented_image.reshape(image.shape).astype(int)


# Display the original and segmented images
plt.figure(figsize=(7,7))
plt.imshow(segmented_image[:,:,::-1])
plt.show()


# In[ ]:





# In[ ]:




