# Brain Tumor Classification & Segmentation

# Classification

This project implements a deep learning model for classifying brain tumors using MRI images. The model differentiates between four classes: glioma, meningioma, no tumor, and pituitary tumor.

## About the Dataset

This dataset is a combination of the following three datasets:
- **figshare**
- **SARTAJ dataset**
- **Br35H**

It contains **7,023 images** of human brain MRIs classified into the following classes:
- **Glioma**
- **Meningioma**
- **No Tumor**
- **Pituitary Tumor**

The **no tumor** class images were sourced from the **Br35H** dataset. It was noted that the **SARTAJ dataset** has issues with the categorization of glioma images, leading to the removal of those images in favor of more accurate images from the **figshare** site.

---

# Segmentation

This project implements a deep learning model for segmenting brain tumors in MRI images. The segmentation model uses a **U-Net** architecture to identify tumor regions in brain MRIs, specifically lower-grade gliomas. The dataset contains MRI images with manual FLAIR abnormality segmentation masks for training and validation.

## About the Dataset

### LGG Segmentation Dataset

The dataset used in this project was introduced in the following publications:
- **Mateusz Buda, Ashirbani Saha, Maciej A. Mazurowski**. "Association of genomic subtypes of lower-grade gliomas with shape features automatically extracted by a deep learning algorithm." *Computers in Biology and Medicine*, 2019.
- **Maciej A. Mazurowski, Kal Clark, Nicholas M. Czarnek, Parisa Shamsesfandabadi, Katherine B. Peters, Ashirbani Saha**. "Radiogenomics of lower-grade glioma: algorithmically-assessed tumor shape is associated with tumor genomic subtypes and patient outcomes in a multi-institutional study with The Cancer Genome Atlas data." *Journal of Neuro-Oncology*, 2017.

This dataset includes:
- **110 patients** with lower-grade gliomas.
- **MRI images** with FLAIR sequence.
- **Manual FLAIR abnormality segmentation masks**.
- **Tumor genomic cluster data** provided in a `data.csv` file.

The data is sourced from **The Cancer Imaging Archive (TCIA)** and corresponds to the lower-grade glioma collection from **The Cancer Genome Atlas (TCGA)**.

For more details on the genomic data, please refer to the supplementary materials in this publication: [Comprehensive, Integrative Genomic Analysis of Diffuse Lower-Grade Gliomas](https://www.nejm.org/doi/full/10.1056/NEJMoa1402121).
