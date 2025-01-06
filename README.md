# rasterioNDVI: A Tool for Easily Generating NDVI Rasters using Rasterio

This script utilizes the `rasterio` package to easily generate NDVI rasters using red and near-infrared (NIR) banded input rasters. The output NDVI rasters are saved as GeoTIFF images with in `.tif` format.

## Calculating NDVI
Normalized Difference Vegetation Index (NDVI) describes the health of vegetation within pixels of a raster image by measuring the amount of near-infrared (NIR) light being reflected by vegetation. Healthy vegetation reflects more NIR and less red relative to unhealthy vegetation or inorganic matter of the same visible color (such as turf fields), making it convenient for assessing the relative health of vegetation in a raster image compared to its surroundings.

NDVI is calculated for each pixel with the following calculation:

$\Large NDVI = \frac{(NIR - Red)}{(NIR + Red)}$

This formula generates a value between -1 and +1. Low reflectance in the red channel and high reflectance in the NIR channel will yield a high NDVI value (healthy vegetation), while the inverse will result in a low NDVI value (unhealthy vegetation). Negative values typically represent non-vegetation such as water or rock.

## Usage
To use this script, import the `rasterioNDVI.py` module and call the `rasterioNDVI()` function with the paths to the NIR-band and red-band raster images given as parameters in addition to the desired output raster path. Please refer to the `demonstration.ipynb` file within this repository for a demonstration of using this module with included output examples.

```Python
rasterioNDVI(nir_path, red_path, output_path)
```

Parameters:
- `nir_path: str` **Requires string**
    - Directory path to the input NIR-band raster being used to calculate NDVI (including file extension).
    - Depending on the directory this function is being called in, you can use the relative path prefix `./` like this: `./nir.tif`
        - Example: `'C:/absolute/path/to/nir_band.tif'` or `./nir_band.tif`
- `red_path: str` **Requires string**
    - Directory path to the input red-band raster being used to calculate NDVI (including file extension).
    - Depending on the directory this function is being called in, you can use the relative path prefix `./` like this: `./red.tif`
        - Example: `'C:/absolute/path/to/red_band.tif'` or `./red_band.tif`
- `output_path: str` **Requires string**
    - Directory path where the output NDVI raster image will be saved (including .tif file extension).
    - Depending on the directory this function is being called in, you can use the relative path prefix `./` like this: `./output_here.tif` in order to save the output raster in the directory it is called in.
        - Example: `'C:/absolute/path/to/output.tif'` or `./output_here.tif`

Usage example:
```Python
# Generates an NDVI raster image from input NIR and red rasters using rasterioNDVI()
import rasterioNDVI.py

rasterioNDVI(nir_path = "C:/data/AreaOfInterest/2024-01-01_NIR.tif",
             red_path = "C:/data/AreaOfInterest/2024-01-01_red.tif",
             output_path = "C:/data/AreaOfInterest/2024-01-01_Output_NDVI.tif")

```