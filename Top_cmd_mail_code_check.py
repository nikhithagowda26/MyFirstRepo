from github import Github
import os

filename_to_upload = 'shellgithub.py' #my previous script name

file_content = open(filename_to_upload,'r').readlines()#reading the file from my system
content_str = ''
for val in file_content:#converting the list to string
    content_str+=val
file1 = open('githubtoken.txt','r').readlines() # reading github token
token = os.getenv('GITHUB_TOKEN', file1[0])
g = Github(token)
repo = g.get_repo("nikhithagowda26/MyFirstRepo") #username and repo access
create_file = repo.create_file(path='Top_cmd_mail_code_check.py',message='Trying to upload the file',content=str(content_str))