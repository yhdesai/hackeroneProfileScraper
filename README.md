## Hackerone Profile Scraper

This is my :spaghetti: code to scrape all the profiles from hackerone.com

### Description

This python code has two functions:

* `get_users_handles()` will fetch all the handles of the **USERS** from `https://hackerone.com/sitemap/`.
 
* `crawl_userprofiles()` will fetch the stored handles and scrape the following data from `https://hackerone.com/{handle}`

| # | Name |
|---|---|
| 1 | id |
| 2 | identifier  |
| 3 | username  |
| 4 | name  |
| 5 | intro_html  |
| 6 | reputation  |
| 7 | signal_  |
| 8 | impact  |
| 9 | signal_percentile  |
| 10 | impact_percentile  |
| 11 | rank  |
| 12 | created_at  |
| 13 | location  |
| 14 | website  |
| 15 | bio  |
| 16 | profile_picture  |
| 17 | bugcrowd_handle  |
| 18 | github_handle  |
| 19 | gitlab_handle  |
| 20 | linkedin_handle  |
| 21 | twitter_handle  |
| 22 | resolved_report_count  |

* both functions will store the data in MySQL database in two separted tables

| Tables |
| --- |
| handles |
| profiles |


### Note

* Import **h1crawler.sql**.
* Change your Mysql server credentials in **config.py** before running the script.




