import requests
import os
import subprocess
import sys

username = 'USERNAME HERE'
api_key = 'API KEY HERE'


def make_remote_repository(repository_name, username, api_key):
    request = requests.post('https://api.github.com/user/repos', json={'name': repository_name, 'private': 'true'}, auth=(username, api_key))

    if request.ok:
        print(f'Repo Creation Successful.')
    else:
        print(f'Got Status Code: {request.status_code}, Please Investigate')
        print(request.text)

    create_local_git_repository(repository_name, username)


def create_local_git_repository(repository_name, username):
    if sys.platform == 'darwin':
        print('System is Mac')
        home_directory = os.path.expanduser('~').split('/')[-1]
        if not os.path.exists(f'/Users/{home_directory}/Code Projects'):
            os.mkdir(f'/Users/{home_directory}/Code Projects')
        local_repository_path = f'/Users/{home_directory}/Code Projects/{repository_name}'
        os.mkdir(local_repository_path)
    elif sys.platform == 'linux':
        print('System is Linux')
        home_directory = os.path.expanduser('~').split('/')[-1]
        if not os.path.exists(f'/home/{home_directory}/Code Projects'):
            os.mkdir(f'/home/{home_directory}/Code Projects')
        local_repository_path = f'/home/{home_directory}/Code Projects/{repository_name}'
        os.mkdir(local_repository_path)
    elif sys.platform == 'win32':
        print('System is Windows')
        home_directory = os.path.expanduser('~').split('/')[-1]
        if not os.path.exists(f'C:/Users/{home_directory}/Code Projects'):
            os.mkdir(f'C:/Users/{home_directory}/Code Projects')
        local_repository_path = f'C:/Users/{home_directory}/Code Projects/{repository_name}'
        os.mkdir(local_repository_path)
    else:
        raise Exception('Could not recognise local OS.')

    subprocess.check_call(['git', 'init'], cwd=local_repository_path)
    with open(f'{local_repository_path}/README.md', 'w') as f:
        f.close()
    subprocess.check_call(['git', 'add', 'README.md'], cwd=local_repository_path)
    subprocess.check_call(['git', 'commit', '-m', 'Initial Commit'], cwd=local_repository_path)
    subprocess.check_call(['git', 'remote', 'add', 'origin', f'https://github.com/{username}/{repository_name}.git'],
                          cwd=local_repository_path)
    subprocess.check_call(['git', 'push', '-u', 'origin', 'master'], cwd=local_repository_path)


if __name__ == '__main__':
    make_remote_repository(sys.argv[1], username, api_key)
