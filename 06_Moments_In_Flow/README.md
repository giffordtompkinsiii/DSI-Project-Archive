# Moments in Flow
Capturings instances of yogic poses during a Vinyasa flow.

# Problem Statement
Computer Vision and Image recognition is becoming common place in our day to day life. Soon systems based on this technology like self-driving cares will become common place. 

We are already seeing image recognition being used to [predict bahviors](link about the police body cams) and seeing the consequences limitations of such technologies especially from some of our [biggest names](link about the misidentifying face thing).
For more reading please look to this lecture done by this person(link to this lecture).

In an effort to understand the coding, algorithms and inherent biases that image recognitions softwares like Computer Vision have, I decided to take a deep dive into the process.

In this repo, we will be looking at how to build an image recognition model and then how to build a ComputerVision Model on top of that.

# In This Repo
```
|code  
|   |00_Google_Custom_Search_API
|   |01_Data_Preprocessing_and_EDA
|   |02_Building_a_CNN_and_ResNet
|   |03_OpenCV_and_ComputerVision
|   |04_Webapp_for_Use_and_Contribution

|creds
|   |google-cse-api-sample.json
|   |

|images
|   |incoming images
|   |   |warrior_ii     # 1500 images
|   |   |warrior_iii    # images
|   |   |shoulder_stand # images
|   |   |crow           # images
|   |   |chair          # images
|   |   |horse          # images
|   |   |warrior_iii    # images


|models
|   |models

```

# Executive Summary
The following will walk the user through the repo, including how to use the Computer Visison module and contribute to the yoga pose database.

## Data Collection and Munging
In notebook [00_Google_Custom_Search_API](./code/00_Google_Custom_Search_API.ipynb) we use the Google Custom Search API to extract the the data came through Google Custom Search API which has a lot of limitations but is free. Was able to request based on post, imageType, and fileType.
Other options were Flikr, Shutterstock, and ImageNet. Would like to use ImageNet but it is under maintenance. Everything had to be saved into class files under a directory.
## Data Cleaning and Preprocessing
I had to make sure that no duplicates were present also had to make sure no files/images were corrupted.

The code for this section came laregly from this [website***]().
## Building A Convolutional Neural Neetwork (CNN)
A Convolutional Neural Network

## Exploring ResNet50V2
## Training A Computer Vision

# Summary and Findings

# Recommendations and Further Steps