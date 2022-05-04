# Water Body Detection

In this project we used NDWI to detect water bodies from Landsat 8 imagery and then use convectional neural networks to classify the water bodies in to lakes and rivers.

## NDWI

* NDWI with NIR and Green bands is used to detect water bodies.

![NIR](/Img/LC08_L2SP_141045_20211023_20211103_02_T1_SR_nir.png)

* NDWI with SWIR1 and Green bands is used to detect water bodies.

![SWIR1](/Img/LC08_L2SP_141045_20211023_20211103_02_T1_SR_swir1.png)

* NDWI with SWIR2 and Green bands is used to detect water bodies.

![SWIR2](/Img/LC08_L2SP_141045_20211023_20211103_02_T1_SR_swir2.png)

## Training

After applying the NDWI threshold, the images are cropped in to sections of 1024x1024 px and segregated in to lake and river segments for training.

![Lake and River Segments](/Img/Lake_and_River_Segments.png)

## Prediction

After training the model, the model is used to classify a image that has not been previously classified.

![New Image](/Img/LC09_L2SP_147043_20220419_20220421_02_T1_SR_swir1.png)

and the classification is shown below.

![Result](/Img/Result.png)

Red color indicates the portion water body is detected as lake and green indicates it is detected as river.
