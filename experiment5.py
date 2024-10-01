def basic_overview(df):
    print("Basic Info of the Data:")
    print(df.info())
    
    print("\nShape of the Data (Rows, Columns):", df.shape)
    
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    print("\nSummary Statistics (Numerical columns):")
    print(df.describe())
    
    print("\nMissing Values in each column:")
    print(df.isnull().sum())

basic_overview(df)

# Check missing values percentage in each column
def missing_values(df):
    print("\nPercentage of Missing Values:")
    missing_percentage = (df.isnull().sum() / len(df)) * 100
    print(missing_percentage)

# Call the missing values check
missing_values(df)

# Check and convert data types if necessary
def convert_data_types(df):
    # Example: convert a date column to datetime
    # df['date_column'] = pd.to_datetime(df['date_column'])

    # Convert categorical columns to category type if needed
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype('category')
        
    print("\nData types after conversion:")
    print(df.dtypes)

# Call the data type conversion function
convert_data_types(df)

import matplotlib.pyplot as plt
import seaborn as sns

# Plot distribution of numerical features
def plot_numerical_distribution(df):
    numerical_columns = df.select_dtypes(include='number').columns
    
    for col in numerical_columns:
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        
        plt.show()

# Call the plot function to visualize numerical distributions
plot_numerical_distribution(df)

# Plot frequency of categorical features
def plot_categorical_distribution(df):
    categorical_columns = df.select_dtypes(include='category').columns
    
    for col in categorical_columns:
        plt.figure(figsize=(8, 4))
        sns.countplot(data=df, x=col)
        plt.title(f'Frequency of {col}')
        plt.xticks(rotation=45)
        plt.show()

# Call the function to visualize categorical distributions
plot_categorical_distribution(df)

# Correlation heatmap for numerical features
def correlation_analysis(df):
    plt.figure(figsize=(10, 8))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

# Call correlation function to visualize
correlation_analysis(df)

# Detect outliers using IQR
def detect_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))
    
    print("Outliers in the dataset (True indicates outlier):")
    print(outliers)

# Call outlier detection
detect_outliers(df)

# Example of feature engineering
def feature_engineering(df):
    # Example: create a new feature from an existing column
    # df['new_feature'] = df['existing_column'] ** 2

    # Example: binning a numerical column
    # df['binned_feature'] = pd.cut(df['numerical_column'], bins=[0, 10, 20, 30], labels=['Low', 'Medium', 'High'])
    
    print("New features added to the dataset (if applicable):")
    print(df.head())

# Call feature engineering if needed
feature_engineering(df)

# Save the processed data
export_data(df, "processed_data.csv")
