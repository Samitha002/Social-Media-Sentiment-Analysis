import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

engine = create_engine('mysql+pymysql://root:Root123@localhost/social_media_db')

df = pd.read_sql("SELECT * FROM social_media_sentiment_500_rows", engine)

print(f"Total rows loaded: {len(df)}")

if not df.empty:

    plt.figure(figsize=(10, 6))


    sns.countplot(data=df, x='sentiment', palette='Set2')

    plt.title('Social Media Sentiment Analysis Result')
    plt.xlabel('Sentiment Type')
    plt.ylabel('Number of Tweets')

    plt.show()
else:
    print("Table-la data illa, Table name-ah check pannunga!")