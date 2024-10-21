import pandas as pd
from sklearn.utils import resample

def balance_classes(df, column):
    each_category_count = df[column].value_counts().to_list()
    categories_name = df[column].unique()
    number_category = df[column].nunique()

    if number_category == 2:
        majority_classes = df[column].value_counts().max()
        minority_classes = df[column].value_counts().min()
        class_majority_class = df[column].value_counts().idxmax()
        class_minority_class = df[column].value_counts().idxmin()

        if majority_classes >= 2 * minority_classes:
            # Downsample majority class
            df_majority = df[df[column] == class_majority_class]
            df_minority = df[df[column] == class_minority_class]

            df_majority_downsampled = resample(df_majority, replace=False, n_samples=len(df_minority), random_state=42)

            df = pd.concat([df_majority_downsampled, df_minority])

    elif number_category > 2:
        # Multi-class case: Balance classes by downsampling majority classes
        majority_class = df[column].value_counts().idxmax()
        majority_count = df[column].value_counts().max()

        balanced_dfs = []

        # Loop through each class
        for element in range(len(each_category_count)):
            class_name = categories_name[element]
            class_count = each_category_count[element]

            # Identify the minority class to balance against
            class_minority_classess = df[column].value_counts().idxmin()  # Define the minority class

            # If the class count is more than twice the size of the smallest class, downsample it
            if class_count >= 2 * df[column].value_counts().min():
                df_majority = df[df[column] == class_name]
                df_minority = df[df[column] == class_minority_classess]

                df_majority_downsample = resample(df_majority, replace=False, n_samples=len(df_minority), random_state=42)
                balanced_dfs.append(df_majority_downsample)
            else:
                balanced_dfs.append(df[df[column] == class_name])

        # Concatenate all balanced dataframes
        df = pd.concat(balanced_dfs)

    return df
