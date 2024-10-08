import pandas as pd
import numpy as np
from scipy import stats

# Function to load a dataset from a CSV file
def load_data(file_path):
    try:
        # Read the dataset into a pandas DataFrame
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to save the dataset to a CSV file
def export_data(df, output_path):
    try:
        # Save the DataFrame to a CSV file
        df.to_csv(output_path, index=False)
        print(f"Data successfully exported to {output_path}")
    except Exception as e:
        print(f"Error exporting data: {e}")

# Function to display dataset information
def show_dataset_info(df):
    if df is not None:
        # Display number of rows and columns
        print("Number of rows and columns:", df.shape)

        # Display first 5 rows of the dataset
        print("\nFirst 5 rows of the dataset:")
        print(df.head())

        # Display the size of the dataset
        print("\nSize of the dataset (total elements):", df.size)

        # Display the number of missing values in each column
        print("\nNumber of missing values in each column:")
        print(df.isnull().sum())

        # Display summary statistics (sum, mean, min, max) for numerical columns
        print("\nSummary statistics (numerical columns):")
        print("Sum:\n", df.sum(numeric_only=True))
        print("Mean (average):\n", df.mean(numeric_only=True))
        print("Min values:\n", df.min(numeric_only=True))
        print("Max values:\n", df.max(numeric_only=True))

# Function to handle missing values
def handle_missing_values(df):
    # Display missing value count
    print("\nMissing values before handling:")
    print(df.isnull().sum())

    # Option 1: Fill missing values with the mean (for numerical columns)
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Option 2: Fill missing values with the mode (for categorical columns)
    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)

    # Option 3: Drop rows with missing values (if desired)
      df.dropna(inplace=True)

    # Display missing value count after handling
    print("\nMissing values after handling:")
    print(df.isnull().sum())
    return df

# Function to handle outliers using the Z-score method
def handle_outliers(df):
    # Detecting outliers using the Z-score method for numerical columns
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
    outliers = (z_scores > 3)  # Z-score > 3 is considered an outlier

    # Option 1: Remove rows with outliers
    df_no_outliers = df[(z_scores < 3).all(axis=1)]
    print("\nOutliers removed. New dataset shape:", df_no_outliers.shape)

    # Option 2: Cap outliers (for example, capping at 95th percentile)
    for col in df.select_dtypes(include=[np.number]).columns:
        upper_limit = df[col].quantile(0.95)
        lower_limit = df[col].quantile(0.05)
        df[col] = np.where(df[col] > upper_limit, upper_limit, df[col])
        df[col] = np.where(df[col] < lower_limit, lower_limit, df[col])

    return df_no_outliers  # You can choose which dataframe to return

# Sample usage
if __name__ == "__main__":
    # Load dataset from a CSV file
    file_path = 'your_dataset.csv'  # Update this to your actual CSV file path
    df = load_data(file_path)

    if df is not None:
        # Show dataset details before preprocessing
        show_dataset_info(df)

        # Handle missing values
        df = handle_missing_values(df)

        # Handle outliers
        df = handle_outliers(df)

        # Show dataset details after preprocessing
        print("\nDataset details after preprocessing:")
        show_dataset_info(df)

        # Export the processed dataset to a new CSV file
        export_path = 'processed_dataset.csv'  # Specify the export file path
        export_data(df, export_path)
