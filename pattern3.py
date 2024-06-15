import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Path to the image
img_path = "C:\Users\HP\Pictures\COLLEGE\IMG20230128182424.jpg"

# Load the image
img = mpimg.imread(img_path)

# Display the image
plt.imshow(img)
plt.axis('off')  # Hide axes
plt.show()
