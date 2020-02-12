from config import * 
from string import ascii_lowercase
import requests
import json
import sys
import MySQLdb as mdb


class h1crawler():
    def __init__(self, host, user, passwd, db):
        try:
            self.con = mdb.connect(host, user, passwd, db)
            self.cur = self.con.cursor()
        except mdb.Error as e:
            print (e)
            sys.exit(1)


    def get_users_handles(self):
        for c in ascii_lowercase:
            handle_url = str(base_url)+"sitemap?first="+str(c)
            try:
                response = requests.get(handle_url, headers=headers)
            except requests.exceptions.RequestException as e:
                print(e)
                sys.exit(1)
            data = response.json()
            for user in data['users']:
                resourceIdentifier = user['username']
                print(resourceIdentifier)
                sql="""INSERT INTO handles (resource_identifier) VALUES (%s)"""
                self.cur.execute(sql, (resourceIdentifier,))
                self.con.commit()
    
    def crawl_user_profiles(self):
        sql = """ SELECT resource_identifier from handles """
        self.cur.execute(sql)
        result = self.cur.fetchall()
        for res in result:
            try:
                ident = res[0]
                profile_url = str(base_url)+"graphql"
                schema={"operationName":"UserProfilePage",
                "variables":{"resourceIdentifier":ident},
                "query":"query UserProfilePage($resourceIdentifier: String!) {  me {    id    username    ...ReputationMetricsMe    ...UserProfileSubheaderMe    __typename  }  user(username: $resourceIdentifier) {    id    username    name    intro_html    ...ReputationMetricsUser    ...UserProfileSubheaderUser    ...UserProfileCardUser    ...CreditsUser    ...BadgesUser    ...ReviewUser    __typename  }}fragment ReputationMetricsMe on User {  id  username  __typename}fragment ReputationMetricsUser on User {  id  reputation  signal  impact  signal_percentile  impact_percentile  rank  username  __typename}fragment UserProfileSubheaderMe on User {  id  username  __typename}fragment UserProfileSubheaderUser on User {  id  username  __typename}fragment UserProfileCardUser on User {  id  created_at  location  website  bio  name  username  profile_picture(size: large)  bugcrowd_handle  github_handle  gitlab_handle  linkedin_handle  twitter_handle  cleared  __typename}fragment CreditsUser on User {  id  username  resolved_report_count  thanks_item_count: thanks_items {    total_count    __typename  }  __typename}fragment BadgesUser on User {  id  username  badges(first: 3) {    edges {      awarded_at      node {        id        name        image_path        __typename      }      __typename    }    __typename  }  __typename}fragment ReviewUser on User {  id  public_reviews(first: 5) {    edges {      node {        id        public_feedback        team {          id          name          handle          __typename        }        __typename      }      __typename    }    __typename  }  __typename}"}
                try:
                    response = requests.post(profile_url, headers=headers, json=schema)
                except requests.exceptions.RequestException as e:
                    print(e)
                    sys.exit(1)
                profile_data = response.json()
                user_obj = profile_data['data']['user']
                identifier = profile_data['data']['user']['id']
                username= profile_data['data']['user']['username']
                name= profile_data['data']['user']['name']

                if 'intro_html' not in user_obj:
                    intro_html = None
                else:
                    intro_html= profile_data['data']['user']['intro_html']
                if 'reputation' not in user_obj:
                    reputation= None
                else:
                    reputation= profile_data['data']['user']['reputation']
                if 'signal' not in user_obj:
                    signal_= None
                else:
                    signal_= profile_data['data']['user']['signal']
                if 'impact' not in user_obj:
                    impact= None
                else:
                    impact= profile_data['data']['user']['impact']
                if 'signal_percentile' not in  user_obj:
                    signal_percentile= None
                else:
                    signal_percentile= profile_data['data']['user']['signal_percentile']
                if 'impact_percentile' not in user_obj:
                    impact_percentile= None
                else:
                    impact_percentile= profile_data['data']['user']['impact_percentile']
                if 'rank' not in user_obj:
                    rank= None
                else:
                    rank= profile_data['data']['user']['rank']
                created_at= profile_data['data']['user']['created_at']
                if 'location' not in user_obj:
                    location= None
                else:
                    location= profile_data['data']['user']['location'].encode('utf8')
                if 'website' not in user_obj:
                    website= None
                else:
                    website= profile_data['data']['user']['website']
                if 'bio' not in user_obj:
                    bio= None
                else:
                    bio= profile_data['data']['user']['bio']
                if 'profile_picture' not in user_obj:
                    profile_picture= None
                else:
                    profile_picture= profile_data['data']['user']['profile_picture']
                if 'bugcrowd_handle' not in user_obj:
                    bugcrowd_handle= None
                else:
                    bugcrowd_handle= profile_data['data']['user']['bugcrowd_handle']
                if 'github_handle' not in user_obj:
                    github_handle= None
                else:
                    github_handle= profile_data['data']['user']['github_handle']
                if 'gitlab_handle' not in user_obj:
                    gitlab_handle= None
                else:
                    gitlab_handle= profile_data['data']['user']['gitlab_handle']
                if 'linkedin_handle' not in user_obj:
                    linkedin_handle= None
                else:
                    linkedin_handle= profile_data['data']['user']['linkedin_handle']
                if 'twitter_handle' not in user_obj:
                    twitter_handle= None
                else:
                    twitter_handle= profile_data['data']['user']['twitter_handle']
                if 'resolved_report_count' not in user_obj:
                    resolved_report_count= None
                else:
                    resolved_report_count= profile_data['data']['user']['resolved_report_count']
                sql="""INSERT INTO profiles (identifier,username,name,intro_html,reputation,signal_,impact,signal_percentile,impact_percentile,rank,created_at,location,website,bio,profile_picture,bugcrowd_handle,github_handle,gitlab_handle,linkedin_handle,twitter_handle,resolved_report_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                self.cur.execute(sql, (identifier,username,name,intro_html,reputation,signal_,impact,signal_percentile,impact_percentile,rank,created_at,location,website,bio,profile_picture,bugcrowd_handle,github_handle,gitlab_handle,linkedin_handle,twitter_handle,resolved_report_count))
                self.con.commit()
            except:
                pass

if __name__ == '__main__': 
    db = h1crawler(HOST, USER, PASS, DB)
    # db.get_users_handles()
    db.crawl_user_profiles()
