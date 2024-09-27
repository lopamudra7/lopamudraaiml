import pandas as pd

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

# Sample usage
if __name__ == "__main__":
    # Load dataset from a CSV file
    file_path = 'your_dataset.csv'  # Update this to your actual CSV file path
    df = load_data(file_path)

    if df is not None:
        # Show dataset details
        show_dataset_info(df)

        # Export the dataset to a new CSV file
        export_path = 'exported_dataset.csv'  # Specify the export file path
        export_data(df, export_path)
