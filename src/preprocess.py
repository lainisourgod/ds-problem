import pandas as pd

if __name__ == "__main__":
    # read data
    train_df = pd.read_csv("./data/problem_train.csv", low_memory=False)
    test_df = pd.read_csv("./data/problem_test.csv", low_memory=False)
    train_labels_df = pd.read_csv("./data/problem_labels.csv")

    # drop na
    train_col_counts = train_df.describe(include="all").loc["count"]
    test_col_counts = test_df.describe(include="all").loc["count"]

    train_na_cols = train_col_counts[train_col_counts == 0].index.to_series()
    test_na_cols = test_col_counts[test_col_counts == 0].index.to_series()
    all_na_cols = pd.concat((train_na_cols, test_na_cols)).values

    train_df = train_df.drop(columns=all_na_cols)
    test_df = test_df.drop(columns=all_na_cols)

    train_df.to_csv("./data/train.csv")
    test_df.to_csv("./data/test.csv")
