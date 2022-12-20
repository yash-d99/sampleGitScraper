import requests
from bs4 import BeautifulSoup

page = requests.get('https://github.com/trending')
#print(page)

soup = BeautifulSoup(page.text, 'html.parser')

repo = soup.find(class_="position-relative container-lg p-responsive pt-6")
repo_list = repo.parent.find_all(class_='h3 lh-condensed')

print(len(repo_list))

for repo in repo_list:
    #print(repo)
    full_repo_name = repo.find('a').text.split('/')
    developer = full_repo_name[0].strip()
    repo_name = full_repo_name[1].strip()
    print('Developer name:' , developer)
    print('Repo name:', repo_name)

repo = soup.find(class_="position-relative container-lg p-responsive pt-6")
repo_list_star = repo.find_all(class_='f6 color-fg-muted mt-2')
print(len(repo_list_star))
for repo in repo_list_star:
    num_stars = repo.find('a').text.strip()
    print('Stars: ', num_stars)
