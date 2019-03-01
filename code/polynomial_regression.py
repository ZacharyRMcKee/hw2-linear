import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class PolynomialRegression():
    def __init__(self, degree):
        """
        Implement polynomial regression using sklearn's PolynomialFeatures from
        scikit-learn and LinearRegression from sklearn. 
        
        This class takes as input "degree", which is the degree of the polynomial 
        used to fit the data. For example, degree = 2 would fit a polynomial of the 
        form:

            ax^2 + bx + c
        
        You will implement this with sklearn. The documentation is here for the
        relevant functions is here:

        https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
        https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    
        The internal representation of this class is up to you. Read each function
        documentation carefully to make sure the input and output matches so you can
        pass the test cases.

        Usage:
            import numpy as np
            
            x = np.random.random(100)
            y = np.random.random(100)
            learner = PolynomialRegression(degree = 1)
            learner.fit(x, y) # this should be pretty much a flat line
            predicted = learner.predict(x)

            new_data = np.random.random(100) + 10
            predicted = learner.predict(new_data)
            # confidence compares the given data with the training data
            confidence = learner.confidence(new_data)

        Args:
            degree (int): Degree of polynomial used to fit the data.
        """
        self.degree = degree
        raise NotImplementedError()
    
    def fit(self, features, targets):
        """
        Fit the given data using a polynomial. The degree is given by self.degree,
        which is set in the __init__ function of this class. The goal of this
        function is fit features, a 1D numpy array, to targets, another 1D
        numpy array using a combination of linear_model and PolynomialFeatures
        from scikit-learn. 
        
        Internally, you should save the model and the data used for training.
        The data used for training will be used to compute the confidence of
        the predictions.


        Args:
            features (np.ndarray): 1D array containing real-valued inputs.
            targets (np.ndarray): 1D array containing real-valued targets.
        Returns:
            None (saves model and training data internally)
        """
        raise NotImplementedError()

    def predict(self, features):
        """
        Given features, a 1D numpy array, use the trained model to predict target 
        estimates. Call this after calling fit.

        Args:
            features (np.ndarray): 1D array containing real-valued inputs.
        Returns:
            predictions (np.ndarray): Output of saved model on features.
        """
        raise NotImplementedError()

    def confidence(self, features):
        """
        Given features, compute the confidence of the trained model on the input
        features. The confidence is computed by comparing the features to
        the features used for training. The idea is to use the distance between
        the features used for training and the features used at test time. If the
        test features are far from the training features, the confidence is low.
        Use the following formula to compute confidence of a single input feature x':

            confidence(x') = 1 / min(||X - x'||)

        This is the minimum distance between the the training data X and the test
        point x'. The inverse of this distance is the confidence the model has for
        the test point x'. 

        """
        raise NotImplementedError()

    def visualize(self, features, targets):
        """
        This function should produce a single plot containing a scatter plot of the
        features and the targets, and the polynomial fit by the model should be
        graphed on top of the points.

        DO NOT USE plt.show() IN THIS FUNCTION.

        Args:
            features (np.ndarray): 1D array containing real-valued inputs.
            targets (np.ndarray): 1D array containing real-valued targets.
        Returns:
            None (plots to the active figure)
        """
        raise NotImplementedError()