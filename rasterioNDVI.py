# Import packages
import rasterio
import numpy as np

# Define function to generate NDVI from input rasters
def rasterioNDVI(nir_path: str, red_path: str):
    NIR = rasterio.open(nir_path)

    red = rasterio.open(red_path)

rasterioNDVI(nir_path = './demo/data/NIR.tif', red_path = './demo/data/red.tif')