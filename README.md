<h1 align="center"> Predicting Restaurants’ Popularity Based On Yelp Dataset </h1>

<p align="center">
<a href="https://tsmanral.github.io/" target="_blank"><img alt="Website" src="https://img.shields.io/badge/-Portfolio-informational"></a>
<a href="https://twitter.com/tribhuwan50" target="_blank"><img alt="Twitter" src="https://img.shields.io/twitter/follow/tribhuwan50.svg?style=social&label=Follow"></a>
<a href="https://www.linkedin.com/in/tribhuwan-singh-9411a175/" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/-Connect-blue?style=flat&logo=linkedin"></a>
<a href="https://github.com/tsmanral" target="_blank"><img alt="Github" src="https://img.shields.io/github/followers/tsmanral.svg?style=social"></a>
</p>



The project is aimed at the creation and analysis of multiple deep learning models for the task to predict the popularity of local businesses based on the actual star rating (which we'll calculate with true score) and the textual review given by a user, in order to carry out a quantitative comparison of the performance accuracies of these models and ascertain the optimal model for this task.

The project applies deep learning and Natural Language Processing methodologies. We also make use of sentiment analyis at pre-processing step thus, to make model training faster. TextBlob is used to convert the original text into its corresponding grammatical structure called Parts of Speech (POS). Once all these factors are evaluated, the stars are then weighted average with weights as the subjectivity scores grouped as business. Thus, for each business we get the weighted_star rating along with the number of reviews as count and total upvotes for all the grouped reviews as funny, cool, and useful. The weighted_stars are plotted in the bar plot below where most of
the ratings lie in mid 70%.

The first phase of this project includes Data Retrieval and Cleaning. The raw data is taken after merging the dataset after sentiment analysis with the original Yelp Business Dataset with business_id as a key. This dataset then contained 100 columns. This dataset is very large and complex where most of the columns have not enough number of values to cope up with the size of the training set. Thus, we only used the subset of this dataset as the dataset for the machine learning models.

In total, three different models are created: Feedforward Neural Network , Polynomial Regression, and LSTM Recurrent Neural Network. The performance accuracies of the training and test sets are compared for all six models. The models are built using open-source deep learning frameworks namely, Tensorflow and Keras.


LSTM Recurrent Neural Networks outperform the other two networks. Moreover, the final LSTM model has significantly lower MSE scores
compared to polynomial regression model and Feed Forward model.

### Dataset Details
The data we used comes from a Yelp data set made available by Yelp for the purpose of the Yelp Dataset Challenge. In particular dataset contains the following data:

● 1.6M reviews and 500K tips by 366K users for 61K businesses

● 481K business attributes, e.g., hours, parking availability, ambience.

● Social network of 366K users for a total of 2.9M social edges.

● Aggregated check-ins over time for each of the 61K businesses 

Businesses reviewed in this dataset are located in the following cities around the world:

● U.K.: Edinburgh

● Germany: Karlsruhe

● Canada: Montreal and Waterloo

● U.S.: Pittsburgh, Charlotte, Urbana-Champaign, Phoenix, Las Vegas, Madison

### Results

Metrics for models trained on original text:

| Model     | Training MSE      | Training MAE  | Testing MSE         | Testing MAE |
|-----------|-------------------|---------------|---------------------|-------------|
| Polynomial| 0.07568786        | 0.1806582     | 0.07472405          | 0.1803489   |
| FNN       | 0.004712816       | 0.04524369    | 0.004732792         | 0.04516283  |
| RNN(LSTM) | 0.00465645        | 0.04533052    | 0.004682693         | 0.0453195   |


All accuracy and Loss graphs can be found in the **Accuracy_and_Loss_graphs** folder.

**Note:** This project was created as my course project during my Masters' degree at Northeastern University, Seattle, USA. I created this along with my teammates: Sachin Kumar ([@sachin301194](https://github.com/sachin301194)), Liangzi Zhang ([@LiangziZhang](https://github.com/LiangziZhang?tab=repositories)), and Yiqun Liu ([@liu-yiqun](https://github.com/liu-yiqun)).
