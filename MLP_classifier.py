import warnings


class MLP_classifier:

    def __init__(self) -> None:
        pass

    """Import the required modules"""
    #from sklearn.datasets import load_iris
    from data import load_OSI
    from sklearn.neural_network import MLPClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    from sklearn.metrics import plot_confusion_matrix
    import matplotlib.pyplot as plt
    from sklearn.model_selection import GridSearchCV
    from sklearn.exceptions import ConvergenceWarning

    iris_data = load_OSI()
    X = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    y = iris_data.target

    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    warnings.filterwarnings('ignore', category=ConvergenceWarning, module='sklearn')
    sc_X = StandardScaler()
    X_trainscaled = sc_X.fit_transform(X_train)
    X_testscaled = sc_X.transform(X_test)

    """params = [
        {
            'hidden_layer_sizes' : [(9,9), (9,4), (9,1), (9,9,1)],
            'activation' : ['tanh', 'relu',  'identity', 'logistic'],
            'alpha' : [1e-5, 1e-6, 0.0001, 0.001],
            'solver' : [ 'lbfgs', 'adam', ],
            'learning_rate_init' : [ 0.001,  1e-5, 0.0001,  0.01]
        }
    ]"""
    

    #hidden_layer_sizes=(9, 9, 1), activation="relu", random_state=1
    clf = MLPClassifier(random_state=1, hidden_layer_sizes=(9, 9), activation='tanh', alpha=1e-5, solver='adam', learning_rate_init=0.001).fit(X_trainscaled, y_train)#256,128,64,32
    
    #grid = GridSearchCV(clf, param_grid=params, cv=5, scoring='accuracy')
    #grid.fit(X_train, y_train)
    #print(grid.best_params_)
    y_pred = clf.predict(X_testscaled)
    print("\nResult: ", clf.score(X_testscaled, y_test))

    fig = plot_confusion_matrix(clf, X_testscaled, y_test, display_labels=["No compra", "Compra"])#"Setosa", "Versicolor", "Virginica"
    fig.figure_.suptitle("Confusion Matrix for Shop Dataset")
    plt.show()