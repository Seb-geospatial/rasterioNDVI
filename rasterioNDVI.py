# Import packages
import rasterio
from rasterio.plot import show
import numpy as np

# Define function to generate NDVI from input rasters
def rasterioNDVI(nir_path: str, red_path: str):
    # Read in input rasters
    nir_band = rasterio.open(nir_path).read(1).astype('float64')
    red_band = rasterio.open(red_path).read(1).astype('float64')

    # Make numpy ignore 0 or nul values when calculating NDVI
    np.seterr(divide='ignore', invalid='ignore')

    # Perform NDVI calculation
    NDVI = (nir_band.astype(float) - red_band.astype(float)) / (nir_band + red_band)

rasterioNDVI(nir_path = './demo/data/NIR.tif', red_path = './demo/data/red.tif')