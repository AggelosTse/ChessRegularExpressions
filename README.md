# Chess PGN Data Extraction

## Overview

Extracting data from PGN (Portable Game Notation) files of chess games using regular expressions. There are separate scripts for extracting data from single PGN games and from larger files containing multiple games. Unit tests are provided to ensure the accuracy of the data extraction process.


## Scripts

1.my_re_functions.py: This script extracts data from a single PGN game using regular expressions.

2.test_my_re_functions.py: This file contains unit tests to validate the functionality of my_re_functions.py.

3.erotima1.py: This script extracts data from a file containing some PGN games using regular expressions.

4.erotima2.py: This script extracts data from a file containing multiple PGN games using regular expressions. (54000)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AggelosTse/ChessRegularExpressions.git

2. Use these commands:

    ```bash
   python3 my_re_functions.py
   python3 test_my_re_functions.py
   python3 erotima1.py
   python3 erotima2.py 