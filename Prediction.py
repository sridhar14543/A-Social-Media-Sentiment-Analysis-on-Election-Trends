import pandas as pd

# Create sample data
data = {
    "User": ["@user1", "@user2", "@user3", "@user4", "@user5","@user6","@user7"],
    "Comment": [
        "I think this leader is doing a great job!",
        "The government has failed us again.",
        "Not sure who deserves my vote this time.",
        "This party’s new policies are impressive!",
        "Everything is getting worse day by day.",
        "The Government is well supported for sports.",
        "The chief minister work Good for tamilnadu."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("election_comments.csv", index=False)
print("Dataset created successfully!")
print(df)
import pandas as pd

# Read dataset
df = pd.read_csv("election_comments.csv")

# Clean text
df["Cleaned_Comment"] = df["Comment"].str.lower()
df["Cleaned_Comment"] = df["Cleaned_Comment"].str.replace(r"[^a-zA-Z\s]", "", regex=True)

print("cleaned data ready!")
print(df)

# Save cleaned file
df.to_csv("cleaned_election_comments.csv", index=False)
import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned dataset
df = pd.read_csv("cleaned_election_comments.csv")

# Simple rule-based sentiment tagging
positive_words = ["great", "impressive", "good", "support", "happy"]
negative_words = ["failed", "worse", "bad", "angry", "corrupt"]

def get_sentiment(text):
    text = str(text)
    if any(word in text for word in positive_words):
        return "POSITIVE"
    elif any(word in text for word in negative_words):
        return "NEGATIVE"
    else:
        return "NEUTRAL"

df["Sentiment"] = df["Cleaned_Comment"].apply(get_sentiment)

# Save final data
df.to_csv("final_sentiment_data.csv", index=False)
print("entiment analysis completed!")
print(df)

# Plot sentiment results
sentiment_counts = df["Sentiment"].value_counts()
plt.bar(sentiment_counts.index, sentiment_counts.values, color=["green", "red", "gray"])
plt.title("Public Sentiment on Election Trends (2025)")
plt.xlabel("Sentiment Type")
plt.ylabel("Number of Comments")
plt.show()
import pandas as pd

# Create sample data
data = {
    "User": ["@user1", "@user2", "@user3", "@user4", "@user5"],
    "Comment": [
        "I think this leader is doing a great job!",
        "The government has failed us again.",
        "Not sure who deserves my vote this time.",
        "This party’s new policies are impressive!",
        "Everything is getting worse day by day."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("election_comments.csv", index=False)
print(" Dataset created successfully!")
print(df)
import pandas as pd

# Read dataset
df = pd.read_csv("election_comments.csv")

# Clean text
df["Cleaned_Comment"] = df["Comment"].str.lower()
df["Cleaned_Comment"] = df["Cleaned_Comment"].str.replace(r"[^a-zA-Z\s]", "", regex=True)

print(" Cleaned data ready!")
print(df)

# Save cleaned file
df.to_csv("cleaned_election_comments.csv", index=False)
import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned dataset
df = pd.read_csv("cleaned_election_comments.csv")

# Simple rule-based sentiment tagging
positive_words = ["great", "impressive", "good", "support", "happy"]
negative_words = ["failed", "worse", "bad", "angry", "corrupt"]

def get_sentiment(text):
    text = str(text)
    if any(word in text for word in positive_words):
        return "POSITIVE"
    elif any(word in text for word in negative_words):
        return "NEGATIVE"
    else:
        return "NEUTRAL"

df["Sentiment"] = df["Cleaned_Comment"].apply(get_sentiment)

# Save final data
df.to_csv("final_sentiment_data.csv", index=False)
print(" Sentiment analysis completed!")
print(df)

# Plot sentiment results
sentiment_counts = df["Sentiment"].value_counts()
plt.bar(sentiment_counts.index, sentiment_counts.values, color=["green", "red", "gray"])
plt.title("Public Sentiment on Election Trends (2025)")
plt.xlabel("Sentiment Type")
plt.ylabel("Number of Comments")
plt.show()