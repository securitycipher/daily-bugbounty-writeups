import feedparser
from github import Github
import os

# RSS feed URL
rss_url = "https://medium.com/feed/tag/bug-bounty"

# Retrieve the GitHub token from the environment variable
github_token = os.environ['GITHUB_TOKEN']

# GitHub repository info
repo_name = "securitycipher/daily-bugbounty-writeups"

# Fetch RSS feed
feed = feedparser.parse(rss_url)
specific_data = feed.entries[0].title  # Replace this with your data extraction logic

# Connect to GitHub
g = Github(github_token)
repo = g.get_repo(repo_name)

# Create a new file and commit the data
file_path = "data.txt"
repo.create_file(file_path, "Updated data", specific_data, branch="main")
