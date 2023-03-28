# Metaplex CM Assets Folder Checker

Getting errors in your Assets folder when tryign to upload a Candy Machine? 

This script is a tool to verify the correctness of your Assets folder when uploading with Candy Machine from Metaplex. The script checks whether your Assets folder contains the correct number of PNG and JSON files and their filenames follow a specific naming convention.

## Getting Started

### Prerequisites

This script requires `Python 3.6` or above and the following packages:

```
pathlib
re
argparse
logging
tqdm
```

To install the packages run the following command:

`pip install pathlib re argparse logging tqdm`


### Installing

1. Clone the repository to your local machine:

`git clone https://github.com/xjbar/Metaplex-CM-Assets-Folder-Checker.git`

2. Change into the cloned directory:

`cd <repository>`

### Usage

To run the script, open a terminal in the cloned repository directory and run the following command:

`python nft_checker.py <num_nfts> <directory> [-v]`

Arguments:

+ `<num_nfts>`: The total number of NFTs.
+ `<directory>`: The directory containing the PNG and JSON files to be checked.
+ `-v` or `--verbose`: Optional flag to enable verbose output.

### Example

`python nft_checker.py 100 /path/to/assets/folder -v`

### Details

The script checks whether the specified directory contains the correct number of PNG and JSON files and their filenames follow the following naming conventions:

+ PNG files: {index}.png, where index is a number between 0 and <num_nfts>-1.
+ JSON files: {index}.json, where index is a number between 0 and <num_nfts>-1.

If the number or the format of the files does not match the expected values, the script will output an error message and tell you what files are missing or wrong. If everything is correct, the script will output a success message.

### Contributing
Contributions are welcome! Please submit a pull request if you have any improvements or bug fixes to the script. M
essage on Discord `@ xjbar#3020` or Twitter `@ xjbarnft`

### License
This project is licensed under the MIT License
