# rasterioNDVI: A Tool for Easily Generating NDVI Rasters using Rasterio

This script utilizes the `rasterio` package to easily generate NDVI rasters using red and near-infrared (NIR) banded input rasters. The output NDVI rasters are saved as GeoTIFF images with in `.tif` format.

## Calculating NDVI
Normalized Difference Vegetation Index (NDVI) describes the health of vegetation within pixels of a raster image by measuring the amount of near-infrared (NIR) light being reflected by vegetation. Healthy vegetation reflects more NIR and less red relative to unhealthy vegetation or inorganic matter of the same visible color (such as turf fields), making it convenient for assessing the relative health of vegetation in a raster image compared to its surroundings.

NDVI is calculated for each pixel with the following calculation:

$\Large NDVI = \frac{(NIR - Red)}{(NIR + Red)}$

This formula generates a value between -1 and +1. Low reflectance in the red channel and high reflectance in the NIR channel will yield a high NDVI value (healthy vegetation), while the inverse will result in a low NDVI value (unhealthy vegetation). Negative values typically represent non-vegetation such as water or rock.

![](./demo/data/ndvi_1.tif?raw=true)

## Usage
To use this script, simply run the `rasterioNDVI.py` script from the command-line as seen below and provide the paths to the input and output raster images as additional command-line arguments in the correct sequence as seen below. Please refer to the `demonstration.ipynb` file within this repository for a demonstration of using this script with included output examples.

```Bash
python rasterioNDVI.py nir_path red_path output_path
```

**NOTE:** The order of command-line arguments given must follow the sequence as seen above where the path to the NIR-band raster is given first, followed by the path to the red-band raster given second, and finally the path to the desired output raster given last. If this order is not adheared to the resulting raster calculations to produce the NDVI raster will not be performed on the correct bands.

Parameters:
- `nir_path`: **Argument[1]**
    - Directory path (without quotations) to the input NIR-band raster being used to calculate NDVI (including file extension).
    - Depending on the directory this function is being called in, you can use the relative path prefix `./` like this: `./nir.tif`
        - Example: `C:/absolute/path/to/nir_band.tif` or `./nir_band.tif`
- `red_path`: **Argument[2]**
    - Directory path (without quotations) to the input red-band raster being used to calculate NDVI (including file extension).
    - Depending on the directory this function is being called in, you can use the relative path prefix `./` like this: `./red.tif`
        - Example: `C:/absolute/path/to/red_band.tif` or `./red_band.tif`
- `output_path`: **Argument[3]**
    - Directory path (without quotations) where the output NDVI raster image will be saved (including .tif file extension).
    - Depending on the directory this function is being called in, you can use the relative path prefix `./` like this: `./output_here.tif` in order to save the output raster in the directory it is called in.
        - Example: `C:/absolute/path/to/output.tif` or `./output_here.tif`

Usage example:
```Bash
python ./rasterioNDVI.py ./demo/data/red_band_1.tif ./demo/data/NIR_band_1.tif ./demo/data/ndvi_1.tif
```

Additionally, the `subprocess` package can be used with the `subprocess.run()` command to run the above terminal command from within other python scripts (assuming the directory of the `rasterioNDVI.py` script is specified). This may be usefull if you wish to automate the use of this script for batch processes.

Usage example:
```python
import subprocess

subprocess.run('python ./rasterioNDVI.py ./demo/data/red_band_1.tif ./demo/data/NIR_band_1.tif ./demo/data/ndvi_1.tif')
```