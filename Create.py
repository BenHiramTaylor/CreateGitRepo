import json
import requests
import os
import subprocess
import sys

username = 'USERNAME HERE'
api_key = 'API KEY HERE'


def makerepo(reponame):
    global username, api_key
    req = requests.post('https://api.github.com/user/repos', data=json.dumps({'name': reponame, 'private': 'true'}),
                        auth=(username, api_key))
    if req.status_code == 200 or req.status_code == 201:
        print(f'Repo Creation Successful.')
    else:
        print(f'Got Status Code: {req.status_code}, Please Investigate')
        print(req.text)
    localgit(reponame)


def localgit(reponame):
    global username
    if sys.platform == 'darwin':
        print('System is Mac')
        homedir = os.path.expanduser('~').split('/')[-1]
        if not os.path.exists(f'/Users/{homedir}/Code Projects'):
            os.mkdir(f'/Users/{homedir}/Code Projects')
        localrepo = f'/Users/{homedir}/Code Projects/{reponame}'
        os.mkdir(localrepo)
    elif sys.platform == 'linux':
        print('System is Linux')
        homedir = os.path.expanduser('~').split('/')[-1]
        if not os.path.exists(f'/home/{homedir}/Code Projects'):
            os.mkdir(f'/home/{homedir}/Code Projects')
        localrepo = f'/home/{homedir}/Code Projects/{reponame}'
        os.mkdir(localrepo)
    elif sys.platform == 'win32':
        print('System is Windows')
        homedir = os.path.expanduser('~').split('/')[-1]
        if not os.path.exists(f'C:/Users/{homedir}/Code Projects'):
            os.mkdir(f'C:/Users/{homedir}/Code Projects')
        localrepo = f'C:/Users/{homedir}/Code Projects/{reponame}'
        os.mkdir(localrepo)
    else:
        raise Exception('Could not recognise local OS.')

    subprocess.check_call(['git', 'init'], cwd=localrepo)
    with open(f'{localrepo}/README.md', 'w') as f:
        f.close()
    subprocess.check_call(['git', 'add', 'README.md'], cwd=localrepo)
    subprocess.check_call(['git', 'commit', '-m', 'Initial Commit'], cwd=localrepo)
    subprocess.check_call(['git', 'remote', 'add', 'origin', f'https://github.com/{username}/{reponame}.git'],
                          cwd=localrepo)
    subprocess.check_call(['git', 'push', '-u', 'origin', 'master'], cwd=localrepo)


if __name__ == '__main__':
    makerepo(sys.argv[1])
