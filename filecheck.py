import sys
import pathlib
import re
import argparse
import logging
from tqdm import tqdm

PNG_PATTERN = r'^(\d{1,4})\.png$'
JSON_PATTERN = r'^(\d{1,4})\.json$'

def check_directory(directory: str, num_nfts: int) -> None:
    png_files = set()
    json_files = set()
    count = 0
    files = [f for f in pathlib.Path(directory).glob('*') if f.is_file() and f.suffix in ['.png', '.json']]
    with tqdm(total=len(files), desc='Checking files') as pbar:
        for file_path in files:
            file_name = file_path.name
            if file_name.endswith('.png'):
                match = re.match(PNG_PATTERN, file_name)
                if match:
                    index = int(match.group(1))
                    if 0 <= index < num_nfts:
                        png_files.add(index)
                        count += 1
                    else:
                        logging.error(f'Invalid PNG file index: {file_name}')
                else:
                    logging.error(f'Invalid PNG file name format: {file_name}')
            elif file_name.endswith('.json'):
                match = re.match(JSON_PATTERN, file_name)
                if match:
                    index = int(match.group(1))
                    if 0 <= index < num_nfts:
                        json_files.add(index)
                        count += 1
                    else:
                        logging.error(f'Invalid JSON file index: {file_name}')
                else:
                    logging.error(f'Invalid JSON file name format: {file_name}')
            pbar.update(1)

    if count != num_nfts * 2:
        logging.error(f'Expected {num_nfts * 2} files, found {count} files')
        if len(png_files) != num_nfts:
            missing_png_files = set(range(num_nfts)).difference(png_files)
            logging.error(f'Missing PNG files: {missing_png_files}')
        if len(json_files) != num_nfts:
            missing_json_files = set(range(num_nfts)).difference(json_files)
            logging.error(f'Missing JSON files: {missing_json_files}')
    elif png_files != json_files:
        logging.error('Mismatch between PNG and JSON files')
    else:
        logging.info('Files are correct')

def main() -> None:
    parser = argparse.ArgumentParser(description='Check NFT files')
    parser.add_argument('num_nfts', type=int, help='Number of NFTs')
    parser.add_argument('directory', type=str, help='Directory containing NFT files')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()

    if not pathlib.Path(args.directory).is_dir():
        logging.error(f'{args.directory} is not a directory')
        sys.exit(1)

    log_level = logging.INFO if not args.verbose else logging.DEBUG
    logging.basicConfig(filename='nft_check.log', level=log_level, format='%(levelname)s:%(message)s')

    check_directory(args.directory, args.num_nfts)

if __name__ == '__main__':
    main()

