# Import packages
import rasterio
import numpy as np
import sys

# Define command line arguments as parameters for rasterioNDVI() function
nir_path_arg = str(sys.argv[1])
red_path_arg = str(sys.argv[2])
output_path_arg = str(sys.argv[3])

# Define function to generate NDVI from input rasters
def rasterioNDVI(nir_path = nir_path_arg, red_path = red_path_arg, output_path = output_path_arg):
    # Open input rasters
    nir_raster = rasterio.open(nir_path)
    red_raster = rasterio.open(red_path)

    # Read input rasters as numpy arrays
    nir_array = nir_raster.read(1).astype('float32')
    red_array = red_raster.read(1).astype('float32')

    # Make numpy ignore 0 or nul values when calculating NDVI
    np.seterr(divide='ignore', invalid='ignore')

    # Perform NDVI calculation
    NDVI = (nir_array - red_array) / (nir_array + red_array)
    
    # Copy metadata from input raster for use in writing output NDVI raster
    output_meta = red_raster.meta.copy()
    output_meta.update(dtype = rasterio.float32)
    
    # Write NDVI to new GeoTIFF raster image
    with rasterio.open(output_path, 'w', **output_meta) as dst:
        dst.write(NDVI, 1)

rasterioNDVI()