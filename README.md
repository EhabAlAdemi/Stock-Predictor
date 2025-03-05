# Data Collection & Preparation
Historical stock data from 2009 to August 2024 was collected for training and testing purposes for Intel, Apple, and Nvidia. From:
#### Apple's Stock Data: https://www.investing.com/equities/apple-computer-inc-historical-data
#### Nvidia's Stock Data: https://www.investing.com/equities/nvidia-corp-historical-data
#### Intel's Stock Data: https://www.investing.com/equities/intel-corp-historical-data
A large dataset was preprocessed and used as the training dataset. A new column in each titled "Label" was created as the target variable, which returns a boolean value: 1 if the stock’s closing price increases by more than 2% over two business days, or 0 if it doesn't. The Excel formula used was:
#### Excel Formula: IF((B4-B2)/B2>0.02,1,0)
#### in which 
#### B4= the closing stock price of two days in advance
####        B2= the closing stock price of today
A second dataset, covering stock data from September 1st to 14th, 2024, was created to serve as the testing dataset. This recent data allows for the evaluation of the models on new, unseen information.


# Model Selection Rationale
**1. Support Vector Machine (SVM)**  
SVM was selected for its effectiveness in binary classification problems, such as predicting whether a stock price will rise or not (the "Label" being 1 or 0). SVM works by finding the optimal hyperplane that separates data points of different classes, making it ideal for distinguishing between stock movements that show a 2% increase versus those that don’t. SVM's ability to handle complex, high-dimensional data patterns ensures that it can effectively process the historical stock data, which may contain nonlinear relationships between features.

**2. Random Forest**  
Random Forest was chosen due to its robustness and high accuracy in classification tasks, particularly when dealing with large datasets like stock market data. It is an ensemble learning method that builds multiple decision trees during training and outputs the class that is the mode of the classes of the individual trees. This model is well-suited for handling noisy data, which is often the case with stock prices that fluctuate unpredictably. Additionally, Random Forest’s ability to handle overfitting better than single decision trees ensures that it provides more reliable predictions.

**3. Logistic Regression**  
Logistic Regression was selected for its simplicity and interpretability in binary classification tasks. It estimates the probability that a given input belongs to a specific class (in this case, whether the stock price will rise by 2% or not). Logistic Regression assumes a linear relationship between the input features and the log-odds of the target variable, making it a good baseline model. It is computationally efficient and provides quick, interpretable results, which is useful for analyzing stock market trends where the goal is often to gain insights into the factors driving price changes.

Each model was chosen for its strengths in classification tasks: SVM for its precision in separating classes with complex patterns, Random Forest for its robustness and accuracy with noisy data, and Logistic Regression for its simplicity and ease of interpretation. Together, these models provide a well-rounded approach to predicting stock price movements.

# Testing and Evaluation
The testing dataset, which includes data from the first two weeks of September 2024, was used to evaluate the models. By analyzing the performance of each model on this fresh dataset, the project assesses how well the predictions hold up in real-time market conditions. The comparative evaluation of the SVM, Random Forest, and Logistic Regression models will help in determining the most reliable predictor for stock price movements among the three companies.


