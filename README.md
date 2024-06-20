# Partial Discharge Localization

This repository maintains codes and logs for [Partial discharge localization in power transformer tanks using machine learning methods](https://www.nature.com/articles/s41598-024-62527-9) paper [^1]. 

![Website](https://img.shields.io/website?url=https%3A%2F%2Fdoi.org%2F10.1038%2Fs41598-024-62527-9&style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Farzinkh/Partial_Discharge?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/Farzinkh/Partial_Discharge?style=for-the-badge&color=red)
![GitHub watchers](https://img.shields.io/github/watchers/Farzinkh/Partial_Discharge?style=for-the-badge&color=purple)
![GitHub Repo stars](https://img.shields.io/github/stars/Farzinkh/Partial_Discharge?style=for-the-badge&color=fedcba)
![GitHub Created At](https://img.shields.io/github/created-at/Farzinkh/Partial_Discharge?style=for-the-badge&color=orange)

This paper presents a comparison of machine learning (ML) methods used for three-dimensional localization of partial discharges (PD) in a power transformer tank. The study examines ML and deep learning (DL) methods, ranging from support vector machines (SVM) to more complex approaches like convolutional neural networks (CNN). Multiple case studies are considered, each with different attributes, including sensor position, frequency content of the PD signal, and size of the transformer tank. The paper focuses on predicting the PD location in three-dimensional space using single-sensor electric field measurements. Various aspects of each method are analyzed, such as the input signal, core methodology, correlation coefficient between the predicted location and the actual location, and root mean square error (RMSE). These features are discussed and compared across the different methods. The results indicate that the CNN model exhibits superior performance in terms of location accuracy among the methods considered.

![Alt Text](logs/1D_final_case_study_one/Animation.gif)

[^1]: DOI: 10.1038/s41598-024-62527-9 
