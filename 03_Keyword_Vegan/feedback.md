## The Data Science Process
### **Problem Statement**
- [x]  I really like how you made the problem statement your own (with your own company, too!)
- [x]  Project is steered towards appropriate stakeholders who would find the project extremely important
- [x]  Types of models not listed explicitly, but not really necessary to name them in the problems statement
- [x]  Nice twist on things by making the target metric specificity, as opposed to just accuracy!
- [x]  Perhaps including a baseline would make the project more black and white on what success is
- [x]  Scope of the project is appropriate
#### Score : 3 / 3

### **Data Collection**
- [x]  Nice job collection over 20,000 posts
- [x]  Data collected was useful and relevant to the project
- [x]  Data collected and storage was optimized through custom functions housed in separate Python files
- [x]  Good job including a sleep of 10 seconds to prevent overloading the server
#### Score : 3 / 3

### **Data Cleaning and EDA**
- [x]  Nice job handling the null and `[removed]` values for self-text (considering if those features contain signal or not!)
- [x]  Nice job cleaning the "duplicate" rows after cleaning!
- [x]  I'm really loving the detailed explanations that are provided with each step of cleaning notebook!
- [x]  Distributions are examined and described in great detail!
- [x]  Nice job contextualizing the EDA process into the broader picture of the project; you're using EDA to help determine the strategy to take in your modeling phase
#### Score : 3 / 3

### **Preprocessing and Modeling**
- [x]  Text data is successfully vectorized with CountVectorizer and TF-IDF
- [x]  Awesome job using lemmatization in a custom function to help clean the data!
- [x]  Proper train/test split made for model training purposes
- [x]  A total of (MultinomialNB, GaussianNB, LogReg)
- [x]  Good exploration into SVD-ing the data
- [ ]  Nice job defending the final production model (LogReg with TFIDF) by comparing the test and specificity scores!
- [ ]  Might want to include a short discussion on why you think LogReg might perform the best  
#### Score : 2.5 / 3

### **Evaluation and Conceptual Understanding**
- [ ]  Nice job accurately identifying the baseline score
- [ ]  Awesome job selecting specificity as the metric to guide the discussion
- [ ]  Awesome job with the super in-depth look at the performance of all the models you created!
- [ ]  How could background knowledge/research be used to interpret the results of the modeling?
#### Score : 2.5 / 3

### **Conclusion and Recommendations**
- [ ]  Each individual step in the project is placed within the context of the bigger picture of the project as a whole
- [ ]  Final conclusions and recommendations are clearly reached
- [ ]  Conclusion answers the original problem statement of achieving a greater score than the baseline
- [ ]  Nice blurb at the end of README that shows how the research will benefit the stakeholders at hand
- [ ]  Future steps are clearly identified!
#### Score : 3 / 3

### Organization and Professionalism
### **Project Organization**
- [ ]  Modules are imported correctly with appropriate aliases
- [ ]  Data is imported and saved using relative paths
- [ ]  Executive summary is robust and outlines the steps taken in the project without getting too in-depth
- [ ]  Markdown formatting is used appropriately to structure notebooks and README
- [ ]  Appropriate amount of comments to help understand the code
- [ ]  Files and directories are organized expertly
- [ ]  No unnecessary files are included
#### Score : 3 / 3

### **Visualizations**
- [ ]  Abundance of great visualizations
- [ ]  Plots demonstrate valid relationships in the data
- [ ]  Plots are labeled and interpreted appropriately
- [ ]  Plots are formatted and scaled appropriately for inclusion in a notebook-based technical report
#### Score : 3 / 3

### **Python Syntax and Control Flow**
- [ ]  Nice job housing functions in separate Python files, even going so far as to separating the functions into appropriate groups
- [ ]  Nice job creating documentation for the functions that you wrote - Extremely professional!
- [ ]  Code is human-readable
- [ ]  Code is free from syntactical (for the most part - not including the "experimental" notebooks that you should clean up before putting on a portfolio!) and logical errors
- [ ]  Code follows general best practices and style guidelines
- [ ]  Pandas, `sklearn`, and `NLTK` functions are used appropriately
#### Score : 3 / 3

### **Presentation**
- [x]  Time : 09:55
- [x]  Problem statement is clear, and the framing of the project is golden
- [x]  Nice inclusion of metrics of success and what kind of model to be created
- [x]  Nice overview of data collection and cleaning / preprocessing
- [x]  Good inclusion of baseline score
- [x]  Nice inclusion of "signal words" with groupings; very compelling evidence for successful classifications
- [x]  Excellent modeling portion and breakdown of the "cost of modeling" = pretty realistic in terms of actual machine learning projects
- [x]  Strong narrative that flows through the presentation and builds to a final conclusion of finding the best model that maximizes specificity
- [x]  Nice defense of what model to use based on the problem statement, as opposed to just finding the most accurate model
- [x]  A little bit over time!
- [x]  Message is delivered with clarity and volume
- [x]  Slides are nicely crafted, nice mix of visualizations and big numbers to draw attention to important
#### Score : 2.5 / 3

## Total : 28.5 / 30
