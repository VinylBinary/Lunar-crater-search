import rasterio
import matplotlib.pyplot as plt

# Path to your .img file
img_path = r"E:\pc\code\python\isro_hackathon\ch2_tmc_ncn_20220511T0809312081_d_img_d18\data\calibrated\20220511\ch2_tmc_ncn_20220511T0809312081_d_img_d18.img"

# Open the image
with rasterio.open(img_path) as src:
    img_data = src.read(1)  # Read the first band

    # Display the image
    plt.imshow(img_data, cmap='gray')
    plt.title("NCN Image")
    plt.show()
