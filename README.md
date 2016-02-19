# WordUp
A complete machine learning project.  [textfitXL](https://github.com/jonneff/textfit) done the right way.

Since I started textfitXL, Reddit comments have been loaded into Google Bigquery. I am shifting the compute-intensive statistical and filtering operations into Bigquery, which will dramatically reduce the time to read and process the data for training the model. I am also replacing the existing features with a feature vector based on the words in the comment body, which I expect will reduce training and test error. Finally, I play to use Naive Bayes for my classification model.  
