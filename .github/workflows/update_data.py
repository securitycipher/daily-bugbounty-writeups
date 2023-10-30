import feedparser
import pandas as pd

# Replace 'YOUR_RSS_FEED_URL' with the URL of the RSS feed
rss_url = 'https://medium.com/feed/tag/bug-bounty'

# Parse the RSS feed
data = feedparser.parse(rss_url)

# Create a list to store the data
data_list = []

# Iterate through the entries in the RSS feed
for entry in data.entries:
    # Extract the data you want and add it to the list
    title = entry.title
    link = entry.link
    # Add more fields as needed

    data_list.append([title, link])

# Create a Pandas DataFrame from the data
data_df = pd.DataFrame(data_list, columns=['Title', 'Link'])

# Save the data to a CSV file
data_df.to_csv('data.csv', index=False)
