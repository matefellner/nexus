

#
#
# Class imbalance
#
#


def imbalanced_learning_undersampling(df, target_column):

    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import make_pipeline
    from sklearn.metrics import classification_report
    from imblearn.under_sampling import RandomUnderSampler
    from imblearn.pipeline import make_pipeline as make_pipeline_imb

    X = df.drop(columns=[target_column])
    y = df[[target_column]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )

    # without balancing, see f1-score
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))

    # with balance, f1 will increase
    model = make_pipeline_imb(
        TfidfVectorizer(), RandomUnderSampler(), MultinomialNB()
    )  # noqa: E501
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))


def smote_oversampling(df, target_column):

    import smote_variants as sv
    from sklearn.model_selection import train_test_split

    X = df.drop(columns=[target_column])
    y = df[[target_column]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
    # printing the number of samples before smote

    print("majority class: %d" % np.sum(y == 0))
    print("minority class: %d" % np.sum(y == 1))

    # The oversampling is carried out by instantiating
    # any oversampler implemented in the package and calling the sample function.
    oversampler = sv.distance_SMOTE()
    X_samp, y_samp = oversampler.sample(X, y)

    # printing the number of samples
    print("majority class: %d" % np.sum(y_samp == 0))
    print("minority class: %d" % np.sum(y_samp == 1))

    return X_samp, y_samp


def regression_imbalance(df, target_column):

    from sklearn.model_selection import train_test_split
    from reg_resampler import resampler
    from imblearn.over_sampling import SMOTE

    num_bins = None  # to specify!

    X = df.drop(columns=[target_column])
    y = df[[target_column]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )

    rs = resampler()
    # You might recieve info about class merger for low sample classes
    # Generate classes
    Y_classes = rs.fit(X_train, target=y_train, bins=num_bins)
    # Create the actual target variable

    # Create a smote (over-sampling) object from imblearn
    smote = SMOTE(random_state=27)

    # Now resample
    final_X, final_Y = rs.resample(smote, X_train, Y_classes)


#
#
# weighted accuracy
#
#


def weighted_acc():
    from sklearn.metrics import balanced_accuracy_score, accuracy_score

    y_true = [0, 1, 0, 0, 1, 0, 1, 1, 1, 1]
    y_pred = [0, 1, 0, 0, 0, 1, 1, 1, 1, 1]

    sample_weights = [10, 1, 1, 1, 10, 1, 0.5, 0.5, 0.5, 0.5]
    weights_by_class = [1 if y == 1 else 1000 for y in y_true]

    print(
        "with some weights: {:.2f}".format(
            balanced_accuracy_score(y_true, y_pred, sample_weight=sample_weights)
        )
    )
    print("without weights: {:.2f}".format(balanced_accuracy_score(y_true, y_pred)))
    print(
        "with class weights in balanced accuracy score: {:.2f}".format(
            balanced_accuracy_score(y_true, y_pred, sample_weight=weights_by_class)
        )
    )
    print(
        "with class weights in accuracy score: {:.5f}".format(
            accuracy_score(y_true, y_pred, sample_weight=weights_by_class)
        )
    )

    class_sizes = [sum((1 for y in y_true if y == x)) / len(y_true) for x in (0, 1)]
    weights_by_class_manually_balanced = [
        w / class_sizes[y] for w, y in zip(weights_by_class, y_true)
    ]

    print(
        "with class weights in accuracy score (manually balanced): {:.5f}".format(
            accuracy_score(
                y_true, y_pred, sample_weight=weights_by_class_manually_balanced
            )
        )
    )

    # with some weights: 0.58
    # without weights: 0.79
    # with class weights in balanced accuracy score: 0.79
    # with class weights in accuracy score: 0.75012
    # with class weights in accuracy score (manually balanced): 0.7500

    ################

    from sklearn.model_selection import GridSearchCV, StratifiedKFold
    from sklearn.linear_model import LogisticRegression

    x_train = None  # custom data
    y_train = None  # custom data

    lr = LogisticRegression(solver="newton-cg")

    # Setting the range for class weights
    weights = np.linspace(0.0, 0.99, 200)

    # Creating a dictionary grid for grid search
    param_grid = {"class_weight": [{0: x, 1: 1.0 - x} for x in weights]}

    # Fitting grid search to the train data with 5 folds
    gridsearch = GridSearchCV(
        estimator=lr,
        param_grid=param_grid,
        cv=StratifiedKFold(),
        n_jobs=-1,
        scoring="f1",
        verbose=2,
    ).fit(x_train, y_train)

    return gridsearch

    #############

    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html

    #############

    # https://kiwidamien.github.io/custom-loss-vs-custom-scoring.html

    from sklearn.metrics import make_scorer
    import numpy as np
    from sklearn.linear_model import RidgeCV

    def mean_abs_error(y_true, y_predict):
        return np.abs(np.array(y_true) - np.array(y_predict)).mean()

    mean_abs_scorer = make_scorer(mean_abs_error, greater_is_better=False)

    rcv = RidgeCV(alphas=0.1, scoring=mean_abs_scorer, cv=5).fit(x_train, y_train)

    return rcv