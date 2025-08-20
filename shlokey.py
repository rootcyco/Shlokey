import json
import sys

# Load dictionaries
def load_json(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file} not found.")
        sys.exit(1)

pali_dict = load_json(r"C:/Users/LENOVO/Desktop/Shlokey/pali.json")
brahmi_dict = load_json(r"C:/Users/LENOVO/Desktop/Shlokey/brahmi.json")

# Reverse dictionaries for decryption
pali_to_eng_dict = {v: k for k, v in pali_dict.items()}
brahmi_to_pali_dict = {v: k for k, v in brahmi_dict.items()}

# English to Pali conversion
def english_to_pali(text):
    words = text.lower().split()
    pali_translation = [pali_dict.get(word, word) for word in words]
    return " ".join(pali_translation)

# Pali to Brahmi conversion
def pali_to_brahmi(text):
    brahmi_translation = "".join([brahmi_dict.get(char, char) for char in text])
    return brahmi_translation

# Brahmi to Pali conversion
def brahmi_to_pali(text):
    pali_translation = "".join([brahmi_to_pali_dict.get(char, char) for char in text])
    return pali_translation

# Pali to English conversion
def pali_to_english(text):
    words = text.split()
    english_translation = [pali_to_eng_dict.get(word, word) for word in words]
    return " ".join(english_translation)

# Encryption Process
def encrypt():
    text = input("\nEnter English text to encrypt: ")
    pali_text = english_to_pali(text)
    brahmi_text = pali_to_brahmi(pali_text)
    print(f"\n🔒 Encrypted (Brahmi): {brahmi_text}")

# Decryption Process
def decrypt():
    text = input("\nEnter Brahmi text to decrypt: ")
    pali_text = brahmi_to_pali(text)
    english_text = pali_to_english(pali_text)
    print(f"\n🔓 Decrypted (English): {english_text}")

def asciiart():
    print("""
 ⠀                                                              
             .#@#   =-          *@%:               .%*      
             @::=  --          @::=.               #.       
            @      @:         @                   @         
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
     =@@@%.-@      @@        .@                  :@         
    ** -@@:-@      @@ =@@@@@+.@  **   :@@@#. .#  :@         
   .@%%#.. -@@@@@@ @@ =@...@@.@ :@@@ :@-*@@  @.  :@         
   #@@@@@% -@:  #@=@@ =@ . :@.@*-:@# @@@#   :@   :@         
       :@@.-@   -@=@@ =@ = .@.@@@@%   %%    %@@--@@         
     ...:% -@   =@-@@ =@   .@.@  :@@ #@*::# .@@@=:@         
   .@@@@%  -@  .@@ @@ =@@@@@@.@   %@ +@@@%       :@         
           -@      @@        .@  #@           :  :@         
           :+      #@*+.      + .            -@@##.         
                    *##*                      *@%          
    """)
    
# CLI Menu
def main():
    asciiart()
    while True:
        print("\n🔐 Shlokey - Cryptography Tool")
        print("1. Encrypt (English → Brahmi)")
        print("2. Decrypt (Brahmi → English)")
        print("3. Exit")
        choice = input("\nChoose an option: ")
        if choice == "1":
            encrypt()
        elif choice == "2":
            decrypt()
        elif choice == "3":
            print("\nExiting... 🔚")
            sys.exit(0)
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
