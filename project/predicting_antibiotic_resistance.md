# Predicting Antibiotic Resistance Using Genetic Sequences
James Eapen

## Vision
This project compares different AI models and their effectiveness at predicting whether a genetic sequence contains a gene that confers antibiotic resistance. The dataset is a collection of artificial genetic sequences labelled with whether or not it has a resistance gene. The features are genomic sequences, made of four letter nucleotides A, C, G, and T. Groups of three nucleotides are called codons and code for a unit of a protein. The order in which they come is important as it determines the structure and function of the protein it encodes.  

The model is based on an example by Scarlat that is a binary classifier trained with convolutional and recurrent networks. Antibiotic resistance prediction is a growing field with active research and based on a review of machine learning methods, I will be adding a model with just a convolutional neural network, a random forest model, and a linear regression.

The goal of this project is to compare the different models and see what models perform the best. After initial runs of the neural networks and the random forest, I decided to compare runtimes as well since the random forest takes significantly less time to train than the neural networks.

## Background
Antibiotic resistance is a naturally occurring phenomenon that has been made worse by the human abuse of antibiotics. Antibiotics are compounds that interfere with bacterial metabolism and prevent normal functioning. They cure infections by killing the bacteria or by preventing its reproduction in the host. Every antibiotic has a mode of action that depends on a it getting into and staying inside the bacterium and on structures within it that can be used to disrupt normal function. 

However, if a bacterium acquires a gene that causes a change a structure that the antibiotic disrupts, the antibiotic is no longer able to work. A bacterium becomes resistant when it acquires an antibiotic resistance gene that codes for a protein that can either protect the bacterium by either changing a characteristic that the antibiotic depends on to work or by pumping the antibiotic out before it can take effect.

Studies of genomes have revealed the sequences that confer resistance and there are databases of known antibiotic resistance genes. Predicting whether a bacterium is resistant to an antibiotic from these sequences can help direct patients to the right antibiotic.

The review by Su et al. examined the performance of a number of machine learning models on different antibiotics and bacteria. Random forests and logistic regressions were common models among the studies they reviewed.

Random forests work by creating a large number of decision trees based on information theory. The trees have little correlation between them and the learning process picks the trees with the best predictions allowing the trees to correct errors between them.

I will be using Keras for the neural networks, Numpy, and pandas for data manipulation and matplotlib for plotting accuracy scores. The random forest and logistic regression models will be implemented with the Scikit-learn package.

## Implementation
This implementation is based on the implementation by Scarlat on Kaggle that uses convolutional and bi-directional Gated Recurrent Unit networks. The first part uses the raw nucleotides, A, C, G, and T. The second approach takes them in groups of three called codons that represent a unit of the protein the sequence codes. 

I extended on the work by Scarlat by adding the convolutional network, the random forest, and the logistic regression and comparing their performances and runtimes. Since the codon approach was more successful than the raw nucleotide approach, I built the models using the codon data.

This section contains the model training and the results section examines the models' predictions and potential clinical effectiveness.


## Random Forest Classifier




## Results

#### Accuracy

The codon based model had much better success than the raw nucleotide based model and had no false positives. 

The neural network and the random forest performed quite similarly on the codon dataset, with the random forest getting more false posititves than the neural network, which is clinically not so bad a problem.

#### Confusion Matrix

A confusion matrix can be used to visualize the results and see how well the model is making its predictions. It shows the true and false positives and negatives. This is useful because a false negative prediction can be clinically more damaging than a false positive prediction since it is worse to take ineffective action against an antibiotic resistant bacterium than to take an intensive treatment against a susceptible bacterium.

#### Runtimes

The runtimes of the models were not correlated with their quality.


## Implications

The ability to predict antibiotic resistance from genomic data will be an asset to fighting infections and antibiotic resistant bacteria. 

This dataset was a synthetic one and may have been easy to work with compared to a full bacterial genome. A full genome will be harder to analyze and predict resistance with and the chances of false negatives will be higher as new mutations arise that confer bacteria with novel resistance mechanisms. 

Using a random forest could allow for quick preliminary analyses that are quite robust and can be used to guide the making of better neural network models that take a lot longer to train.

## Citations
Scarlat, Alexander, Predict antibiotic resistance w gene sequence, Kaggle. https://www.kaggle.com/drscarlat/predict-antibiotic-resistance-w-gene-sequence/data

Su, M., Satola, S. W., & Read, T. D. (2019). Genome-Based Prediction of Bacterial Antibiotic Resistance. Journal of clinical microbiology, 57(3), e01405-18. https://doi.org/10.1128/JCM.01405-18

