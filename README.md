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

* Create the **handles** and **profiles** tables:
```sql
CREATE TABLE `handles` (
  `id` int(11) NOT NULL,
  `resource_identifier` varchar(800) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `profiles` (
  `id` int(11) NOT NULL,
  `identifier` varchar(800) DEFAULT NULL,
  `username` varchar(800) DEFAULT NULL,
  `name` varchar(800) DEFAULT NULL,
  `intro_html` varchar(800) DEFAULT NULL,
  `reputation` varchar(800) DEFAULT NULL,
  `signal_` varchar(800) DEFAULT NULL,
  `impact` varchar(800) DEFAULT NULL,
  `signal_percentile` varchar(800) DEFAULT NULL,
  `impact_percentile` varchar(800) DEFAULT NULL,
  `rank` varchar(800) DEFAULT NULL,
  `created_at` varchar(800) DEFAULT NULL,
  `location` varchar(800) DEFAULT NULL,
  `website` varchar(800) DEFAULT NULL,
  `bio` varchar(800) DEFAULT NULL,
  `profile_picture` varchar(800) DEFAULT NULL,
  `bugcrowd_handle` varchar(800) DEFAULT NULL,
  `github_handle` varchar(800) DEFAULT NULL,
  `gitlab_handle` varchar(800) DEFAULT NULL,
  `linkedin_handle` varchar(800) DEFAULT NULL,
  `twitter_handle` varchar(800) DEFAULT NULL,
  `resolved_report_count` varchar(800) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

```
* Change your Mysql server credentials in **config.py** before running the script.
* Install all the requirements `pip3 install -r requirements.txt`.




