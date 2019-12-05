import os

def discover(initial_path):

    extensions = [
        'img', 'jpeg', 'png', 'txt', 'mp4', 'mp3', 'xls', 'xlsx', 'doc', 'docs', 'pdf', 'thjj'
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)