from pathlib import Path

path = Path('C:/Users/User/Downloads')


def parse_folder(path):
    files = []
    folders = []
    for dir in path.iterdir():
        if dir.is_dir():
            folders.append(dir.name)
        elif dir.is_file():
            files.append(dir.name)

    return files, folders


print(parse_folder(path)[0])
print(parse_folder(path)[1])
