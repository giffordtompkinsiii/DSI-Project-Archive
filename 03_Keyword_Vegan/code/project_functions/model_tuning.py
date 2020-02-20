from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix

def condenser(sparse_matrix):
    return sparse_matrix.toarray()

condenser_tr = FunctionTransformer(condenser, accept_sparse=True, validate=False)

def build_pipeline(transformer, classifier):
    pipeline = Pipeline([
        ('vec',transformer),
        ('condenser', condenser),
        ('classifier',classifier)
    ])
    print(f"Pipeline steps: {pipeline.steps}")
    return pipeline


def build_gridsearch(transformer, classifier):    
    pipeline = build_pipeline(transformer, classifier)
    gridsearch = GridSearchCV(estimator=pipeline,
                              param_grid=pipe_params,
                              scoring='accuracy',
                              verbose=4,
                              n_jobs=4,
                              cv=3)
    return gridsearch

def parse_performance(model, X, y):
    '''
    This function takes in a model, evaluates the testing data and spits out the
    confusion matrix values as well as the sensitivity and specificity.

    Parameters
    ----------
    model : pipeline object
        The pipeline object that is getting evaluated.
    X : np.array
        Features being used to fit the `model`
    y: np.array
        Target variable being used to fit the `model`.

    Returns
    -------
    sens: float
        Sensitivity of the fitted `model`.
    spec: float
        Specificity of the fitted `model`.
    (tn, fp, fn, tp): np.matrix
        the elements of the confusion matrix.
    
    Example
    -------
    sens, spec, (tn, fp, fn, tp) = parse_performance(model, X, y)
    '''
    y_preds = model.predict(X)
    
    tn, fp, fn, tp = confusion_matrix(y, y_preds).ravel()
    
    sens = (tp / (tp + fn))
    spec = (tn / (tn + fp))
    
    # print(f"Model Score: {model.score(X,y)}")
    # print(f"Model sensitivity: {sens}")
    # print(f"Model specificity: {spec}")
    return sens, spec, (tn, fp, fn, tp)


def run_evaluate_grid(grid, X_train, X_test, y_train, y_test):
    model = {}
    t_0 = time.time()
    print(f"Fitting model: {t_0}")
    grid.fit(X_train, y_train)
    print(f"Model fit: {time.time()-t_0}")
    
    model['steps'] = [type(step) for _,step in grid.estimator.steps]
    model['best_cross_val'] = grid.best_score_
    model['best_params'] = grid.best_params_
    model['train_score'] = grid.score(X_train, y_train)
    model['test_score'] = grid.score(X_test, y_test)
    model['sensitivity'],model['specificity'],model['confusion_matrix'] = parse_performance(grid, X_test, y_test)
    model['runtime'] = time.time() - t_0
    
#     with open('../datasets/model_scores.csv', 'a') as f:
#         model.to_csv(f, header=False, index=False)
#     print(f"Model with Testing Score: {model['test_score']} appended to model scores.")
    
    return model