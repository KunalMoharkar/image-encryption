# image-encryption
Implementation of research paper - Privacy-Preserving Threshold-Based Image Retrieval in Cloud-Assisted Internet of Things (2021 IEEE))

# Abstract
Encrypted image retrieval is a promising technique, for achieving data confidentiality and searchability the in cloudassisted Internet of Things (IoT) environment. 
However, most image retrieval solutions have low retrieval efficiency, and may leak the values and orders of similarity scores to the cloud server. 
Hence, if a malicious server learns user background information through some improper means, 
then the malicious server can potentially infer user preferences and guess the most similar image content according to similarity scores.
To solve the above challenges, we propose a privacy-preserving threshold-based image retrieval scheme which improves the retrieval
efficiency and prevents the cloud server from learning the values and orders of similarity scores.

# Algorithms
1) Keygen
2) Indexgen
3) Image Enc
4) Trapgen
5) Search
6) Image Dec

# Performance Analysis
In the test experiments, all our data are taken from the public dataset CIFAR-10 which contains 10 categories of RGB color pictures, with 6000 pictures of
each category. For convenience, we reduce the number of images of each category to 1000. Therefore, we can select different datasets, including 2000 images belonging to two
categories, 5000 images belonging to five categories, 8000 images belonging to eight categories. We use ResNet50 for feature extraction. 
In the simulation, since the dimension l of the feature vector has a great impact on the performance, we change l using PCA technology.

Dataset - https://drive.google.com/drive/folders/14FOnpwhj79fJAcUJqy6yRqqkE3BddGJU?usp=sharing
