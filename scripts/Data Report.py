#Data Reporter

def generate_data_report(csv_path):
    df = pd.read_csv(csv_path)
    print("Summary:\n")
    print(df.describe(include='all'))
    df[label_column].value_counts().plot(kind='bar', title='Class Distribution').figure.savefig('class_distribution.png')

# generate_data_report('data.csv')