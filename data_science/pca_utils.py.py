import numpy as np

# import pandas as pd
import matplotlib.pyplot as plt


#
# PCA
#


def remove_outliers_iqr(df, attributes, factor=1.5):
    # pca aux function
    df_no = df.copy()

    for var in attributes:
        if np.issubdtype(df[var].dtype, np.number):
            q1 = df_no[var].quantile(0.25)
            q3 = df_no[var].quantile(0.75)
            iqr = q3 - q1

            low_limit = df[var] >= q1 - (iqr * factor)
            upper_limit = df[var] <= q3 + (iqr * factor)

            df_no = df_no.loc[(low_limit) & (upper_limit), :]

    outliers = df.shape[0] - df_no.shape[0]
    print(f"{outliers} outliers detected and removed from the dataset.")

    return df_no


def show_explained_variance(data_pca):
    # pca aux function
    plt.rcParams["figure.figsize"] = [12, 6]
    f, (ax1, ax2) = plt.subplots(1, 2)

    cum_exp_var = sum(data_pca.explained_variance_ratio_)

    print(f"Cummulative Variace Explained:{round(100*cum_exp_var,1)}%")
    ax1.set_title("Explained Proportion Variance ")
    ax1.plot(data_pca.explained_variance_ratio_, "o")
    ax2.set_title("Explained Variance")
    ax2.plot(data_pca.explained_variance_, "o")


def apply_pca_for_dataframe(dataframe, target_columns=[], variance_threshold=0):

    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler

    df_no = remove_outliers_iqr(
        dataframe, dataframe.drop(columns=target_columns), factor=1.5
    )

    X = df_no.drop(columns=target_columns)
    y = df_no[target_columns]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )

    standard_scaler = StandardScaler()
    X_train = standard_scaler.fit_transform(X_train)
    X_test = standard_scaler.transform(X_test)

    if variance_threshold == 0:
        pca = PCA()
        pca.fit(X_train)
    else:
        pca = PCA(n_components=variance_threshold)
        X_train_pca = pca.fit_transform(X_train)
        X_test_pca = pca.transform(X_test)

    show_explained_variance(pca)

    if variance_threshold != 0:
        return X_train_pca, X_test_pca


#
#
# Factor analysis
#
# noqa: E501 from https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html
# and
# https://www.datacamp.com/community/tutorials/introduction-factor-analysis
# https://factor-analyzer.readthedocs.io/en/latest/factor_analyzer.html
# https://buildmedia.readthedocs.org/media/pdf/factor-analyzer/latest/factor-analyzer.pdf


def adequacy_test(df):

    # Bartlett’s Test
    from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

    chi_square_value, p_value = calculate_bartlett_sphericity(df)
    print(chi_square_value, p_value)
    # low p-value means that the test is statistically significant

    # Kaiser-Meyer-Olkin (KMO) Test
    # measures the suitability of data for factor analysis
    # KMO estimates the proportion of variance among all the observed variable
    # KMO values range between 0 and 1
    # Value of KMO less than 0.6 is considered inadequate

    from factor_analyzer.factor_analyzer import calculate_kmo

    kmo_all, kmo_model = calculate_kmo(df)
    print("kmo_model", kmo_model)


def choosing_the_number_of_factors(df):

    # Kaiser criterion and scree plot
    from factor_analyzer import FactorAnalyzer

    fa = FactorAnalyzer()
    fa.analyze(df, 25, rotation=None)
    # Check Eigenvalues
    ev, v = fa.get_eigenvalues()
    print(ev)

    # if 6 factors have larger eigenvalues than 1, then we select only 6 factors

    plt.scatter(range(1, df.shape[1] + 1), ev)
    plt.plot(range(1, df.shape[1] + 1), ev)
    plt.title("Scree Plot")
    plt.xlabel("Factors")
    plt.ylabel("Eigenvalue")
    plt.grid()
    plt.show()


def factor_analysis(df):

    from factor_analyzer import FactorAnalyzer

    fa = FactorAnalyzer()
    fa.analyze(df, 6, rotation="varimax")

    print(fa.loadings)
    # if one factor has no high factor loading for any variables, then
    # factor count shoud be lowered

    # Get variance of each factors
    print(fa.get_factor_variance())


def factor_analysis_for_dataset(X):

    from sklearn.decomposition import FactorAnalysis

    transformer = FactorAnalysis(n_components=7, random_state=0)
    X_transformed = transformer.fit_transform(X)

    return X_transformed
