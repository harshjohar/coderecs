# Coderecs

Coderecs is a competitive programming platform, which recommend the users to solve the next cp questions, based on their previous performance, in the contests.

> Note : It is built as a prototype for now, by college students. We aim to put this forward for production in upcoming future.

## Motivation
The motivation for CodeZone came when the creators of the website were facing a common problem. All of them knew about the resources to learn programming, but were perplexed as to how to proceed.

Nowhere offered a thorough road to mastery, so we set out to create a single platform where everyone could study regardless of ability level so that this issue would never arise again.

## What we did?
This project consists of several breakpoints throughout the phase of development.

We divided this into 3 main aspects:
1. Data collection and preprocessing
2. Model Training
3. Website and deployment

## Data Collection and Preprocessing
The data which we used to train and test out model was taken from a renowned competitive programming platform [codeforces](https://codeforces.com/).

Collected data was then preprocessed to generate the ratings corresponding to a user and a problem. Basically a mapping was created in a user and a problem, i.e., how much a user will rate a particular problem, given the user has solved it. 

This was done with the use of parameters such as number of correct submissions and wrong submission, time taken and rating comparison on question and user rating on codeforces.

## Model Training

This was the **most** crucial part of the development of the whole project.

We tried several models to serve the purpose, we were looking for.

Some of them failed too, but in the end `tensorflow deep learning ranking model` was most suitable for the purpose of the platform.

### Tensorflow Deep learning ranking model
This model basically generates the rating for a question, which the user has not solved yet. Based on this rating, recommendation is given to the user, i.e., the problems which the user is __likely__ to rate the highest.

## Website and Deployment
This was the final footstep of the completion of the platform. The website was developed with the use of the modern react based framework : NEXTjs and TailwindCSS.

UI/UX was taken care with utmost priority, as this website's main use case is to provide a user friendly experience to a competitive programmer.

The user should not feel the chaos, which one usually faces on cp websites. A clean and clear UI is provided for the user to track the progress and upsolving the recommended problems.

## Technologies Used
This is a full stack project consisting of modern technologies.

### Website
The website is built using the following frameworks/libraries
+ NEXTjs 
+ TailwindCSS
+ React
+ Font Awesome
+ Material UI

### Machine Learning
The model is based on deep learning and uses  collaborative filtering to recommend problems to the user.

Libraries/Frameworks used:
+ Tensorflow
+ Scikit-Learn
+ Numpy
+ Pandas

### Data preprocessing
The data is collected from the Open Source API of [codeforces](https://codeforces.com/apiHelp/methods).

## Contributors
+ Harshpreet Singh Johar
+ Uttam Mittal
+ Harasees Singh
