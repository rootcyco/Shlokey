# Shlokey - Cryptography Tool

## Overview
Shlokey is a simple command-line cryptography tool that encrypts English text into Brahmi script via Pali language and decrypts Brahmi text back to English. It uses dictionary mappings stored in JSON files to facilitate the conversions.

## Features
- Convert **English text to Brahmi** (Encryption)
- Convert **Brahmi text back to English** (Decryption)
- Intermediate conversion steps:
  - English → Pali
  - Pali → Brahmi
  - Brahmi → Pali
  - Pali → English

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x

## Setup
1. Clone or download the repository:
   ```bash
   git clone https://github.com/rootcyco/shlokey.git
   cd shlokey
   ```
2. Place the required JSON files (`pali.json` and `brahmi.json`) in the same directory as the script.
3. Install any required dependencies (if applicable).

## Usage
Run the script using:
```bash
python shlokey.py
```

### Encryption
1. Choose option **1** in the menu.
2. Enter the English text.
3. The encrypted text in **Brahmi script** will be displayed.

### Decryption
1. Choose option **2** in the menu.
2. Enter the Brahmi script text.
3. The decrypted text in **English** will be displayed.

### Exiting the Tool
- Choose option **3** to exit the program.

## File Structure
```
|-- shlokey/
    |-- shlokey.py             # Main script
    |-- pali.json              # English to Pali dictionary
    |-- brahmi.json            # Pali to Brahmi dictionary
    |-- README.md              # Documentation
```

## Error Handling
- If JSON files are missing, the script will display an error message and exit.
- If a word or character is not found in the dictionaries, it remains unchanged.
- Invalid menu selections prompt the user to enter a correct option.

## Future Improvements
- Expand the dictionaries for better word coverage.
- Implement a GUI version for easier usability.
- Add support for additional languages and scripts.

## Contribution Guidelines
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author
Omega- CyCo

For any queries, feel free to reach out at https://github.com/rootcyco.

Enjoy using **Shlokey** for secure and interesting text transformations!

