# Predicting Antibiotic Resistance from Genetic Sequences

This is the project for CS-344 that compares resistance prediction models. The dataset is a collection of artificial genetic sequences labelled with whether or not it has a resistance gene. The features are genomic sequences, made of four letter nucleotides A, C, G, and T. Groups of three nucleotides are called codons and code for a unit of a protein. The order in which they come is important as it determines the structure and function of the protein it encodes.  

The model is based on an example by [Scarlat](https://www.kaggle.com/drscarlat/predict-antibiotic-resistance-w-gene-sequence/data) that is a binary classifier trained with convolutional and recurrent networks and has a random forest and a logistic regression added to it.

The goal of this project is to compare the different models and see what models perform the best. After initial runs of the neural networks and the random forest, I decided to compare runtimes as well since the random forest took significantly less time to train than the neural networks.

The dataset can be downloaded from [here](https://drive.google.com/file/d/1untjB6CcUpZBTAWJ8hYxvrVP_mW98fHA/view?usp=sharing).
