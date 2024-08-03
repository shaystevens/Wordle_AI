# Wordle AI Project

This project automates the process of playing the popular Wordle game using Selenium and Edge. The program can play Wordle efficiently by implementing web scraping techniques and automation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- Microsoft Edge browser
- Microsoft Edge WebDriver
- Selenium library

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/shaystevens/Wordle_AI.git
   cd Wordle_AI
   ```
2. Install required Python packages:
    ```bash
    pip install selenium
    ```
3. Download the Microsoft Edge WebDriver that matches your Edge browser [version](https://support.microsoft.com/en-us/microsoft-edge/find-out-which-version-of-microsoft-edge-you-have-c726bee8-c42e-e472-e954-4cf5123497eb) from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

4. Add msedgedriver.exe to C:\webdriver
    ```bash
    cd \
    mkdir webdriver
    move msedgedriver.exe C:\webdriver
    ```


## Usage

1. Navigate to project directory.
   ```bash
   cd Wordle_AI
   ```

2. Run main scirpt.
   ```bash
   python main.py
   ```

### Additional flags
* `--quiet` (bool) If True, suppresses output to the console. Defaults to False.
* `--start_word` (str) The starting word to use. Defaults to None.

## Algorithm
This project uses letter frequency analysis along with weighting the index positions of the letter.

### Word Score formula
$$
Score(W) = U*\sum_{i=0}^{n} (F(W_i) * P(W_i, i))
$$

$ W $ - Represents the word

$ U $ - The number of unique letters in the word.

$ F(W_i) $ - Function that calculates the frequency score for the letter in the word.

$ P(W_i, i) $ - Function that calculates the positioning score of the letter at it's index.

## License

This project is licensed under the terms of the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.