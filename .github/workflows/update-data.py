name: Update Table from RSS

on:
  schedule:
    - cron: '*/1 * * * *'  # Runs every minute

jobs:
  update-table:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          pip install feedparser
          pip install pandas
        env:
          PIP_DEFAULT_TIMEOUT: 120

      - name: Fetch data from RSS
        run: |
          python .github/workflows/update_data.py
        env:
          MINDFULL: ${{ secrets.MINDFULL }}

      - name: Commit and push data to GitHub repo
        run: |
          git config --global user.email "actions@github.com"
          git config --global user.name "GitHub Actions"
          git add data.csv
          git commit -m "Update data from RSS"
          git push
        env:
          MINDFULL: ${{ secrets.MINDFULL }}
