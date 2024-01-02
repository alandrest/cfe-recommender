
"""
Params:
    return_X_y: bool, default=False
        If True, returns (data, target) instead of Bunch object
    as_frame: bool, default=False
        If True, the data is a pandas DataFrame including
        columns with appropriate dtypes (numeric).
        The target is a pandas DataFrame or Series depending
        on the number of target columns.
    scaled: bool, default=True
        If True, the feature variables are mean centered and scaled by the standard deviation
        times the square root of n_samples. If False, raw data is returned for the feature variables.

Returns:
    data: Bunch
    (data, target): tuple if return_X_y=True
        data:ndarray 2D array of shape (n_samples, n_features)
        target:ndarray of shape (n_samples,) containing the target samples

Bunch = dictionary-like objectm with the following attributes:
        data: [ndarray, pd.Dataframe], shape=(150, 4)
              if as_frame=True: it is pd.Dataframe
        target: [ndarray, Series], shape=(150,)
        feature_names: List[str] = list of dataset columns (target is not included)
        target_names: List[str] = List of target classes values
        frame: pd.DataFram, shape=(150, 5)
                only present of as_frame=True.
                contains data and target
        DESCR: str
        filename: str
            The path to the location of the data.
"""

"""
Iris plants dataset (classification)
Source: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris

Data Set Characteristics:
    Number of instances:        150
    Classes:                    3
    Samples per class:          50
    Samples total:              150
    Dimensionality:             4
    Features:                   real, positive
    Targets:                    3 string values
    Missing Attribute Values:   None
    Class Distribution:         33.3% for each of 3 classes.
    Notes:                      This is perhaps the best known database
                                to be found in the pattern recognition literature
                                One class is linearly separable from the other 2;
                                the latter are NOT linearly separable from each other.
Params:
    return_X_y: bool, default=False
    as_frame: bool, default=False
        
Returns:
    data: Bunch 
    (data, target): tuple if return_X_y=True                
"""


"""
data:Bunch (8)
    data: ndarray, shape(150,4)
    target: ndarray, shape(150,)
    feature_names: List[str] = ['sepal length (cm)', 
                                'sepal width (cm)', 
                                'petal length (cm)', 
                                'petal width (cm)']
    target_names: List[str] = array(['setosa', 
                                     'versicolor', 
                                     'virginica'], dtype='<U10')

    frame: None
    DESCR: str ...
    filename: str = 'iris.csv'        
"""
def load_iris_1():
    from sklearn.datasets import load_iris
    data = load_iris()

"""
data: tuple 
    data[0]: ndarray, shape=(150, 4)
    data[1]: ndarray, shape(150,)
    __len__ = 2
"""
def load_iris_2():
    from sklearn.datasets import load_iris
    data = load_iris(return_X_y=True)

"""
data: tuple 
    data[0]: ps.Dataframe, shape=(150, 4)
        data[0].columns: (target is not included):
                    ['sepal length (cm)', 'sepal width (cm)', 
                    'petal length (cm)', 'petal width (cm)'],
    data[1]: Series, shape(150,)
        data[1].name='target'
    __len__ = 2
"""
def load_iris_3():
    from sklearn.datasets import load_iris
    data = load_iris(return_X_y=True, as_frame=True)

"""
Diabetes dataset (regression)
Source: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes
Data Source: https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html
Data Set Characteristics:
    Num of instances:           442
    Num of attrs:               First 10 columns are numeric predictive values
    Target:                     Column 11 is a quantitative measure of disease progression one year after baseline
    Dimensionality:             10
    Features:                   real, -.2 < x < .2
    Targets:                    integer 25 - 346
    ??Missing Attribute Values:   None
    ??Class Distribution:         33.3% for each of 3 classes.
    Notes:                      Each of 10 feature variables have been mean centered and 
                                scaled by the standard deviation times the square root of
                                n_samples (i.e. the sum of squares of each column totals 1).
Params:
    return_X_y: bool, default=False        
    as_frame: bool, default=False        
    scaled: bool, default=True
        
Returns:
    data: Bunch 
    (data, target): tuple if return_X_y=True
               
"""


"""
data:Bunch (8)
    data: ndarray, shape(442, 10)
    target: ndarray, shape(442,)
    feature_names: List[str] = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
    target: ndarray, shape(442,), dtype: float64, values: integer [25, 346]
    frame: None
    DESCR: str ...
"""
def load_diabetis_1():
    from sklearn.datasets import load_diabetes
    data = load_diabetes()


###################### Digits ########################
# Source:

####################### Linnerud ########################
# Source:

###################### Breast cancer ########################
# Source:


