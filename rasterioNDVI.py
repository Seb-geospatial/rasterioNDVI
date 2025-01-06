# Import packages
import rasterio

# Define function to generate NDVI from input rasters
def rasterioNDVI(NIR_path: str, red_path: str, output_path: str):
    with rasterio.open(NIR_path) as src_NIR:
        NIR_band = src_NIR.read(1)

    with rasterio.open(red_path) as src_red:
        red_band = src_red.read(1)