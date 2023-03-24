import os
import re
import sys

EXPECTED_COUNT = 8000
PNG_PATTERN = r'^(\d{1,4})\.png$'
JSON_PATTERN = r'^(\d{1,4})\.json$'

def check_directory(directory):
    png_files = set()
    json_files = set()
    count = 0
    for file_name in os.listdir(directory):
        if os.path.basename(__file__) == file_name:
            # ignore the script file itself
            continue
        if file_name.endswith('.png'):
            match = re.match(PNG_PATTERN, file_name)
            if match:
                index = int(match.group(1))
                if 0 <= index < 4000:
                    png_files.add(index)
                    count += 1
                else:
                    print(f'Invalid PNG file index: {file_name}')
            else:
                print(f'Invalid PNG file name format: {file_name}')
        elif file_name.endswith('.json'):
            match = re.match(JSON_PATTERN, file_name)
            if match:
                index = int(match.group(1))
                if 0 <= index < 4000:
                    json_files.add(index)
                    count += 1
                else:
                    print(f'Invalid JSON file index: {file_name}')
            else:
                print(f'Invalid JSON file name format: {file_name}')
    if count != EXPECTED_COUNT:
        print(f'Expected {EXPECTED_COUNT} files, found {count} files')
        if len(png_files) != 4000:
            missing_png_files = set(range(4000)).difference(png_files)
            print(f'Missing PNG files: {missing_png_files}')
        if len(json_files) != 4000:
            missing_json_files = set(range(4000)).difference(json_files)
            print(f'Missing JSON files: {missing_json_files}')
    elif png_files != json_files:
        print('Mismatch between PNG and JSON files')
    else:
        print('Files are correct')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <directory>')
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f'{directory} is not a directory')
        sys.exit(1)
    check_directory(directory)
