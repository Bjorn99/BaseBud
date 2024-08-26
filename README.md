# BaseBud

Welcome to **BaseBud**, a Python tool designed for analyzing DNA sequences. This repository contains a simple script that allows users to input DNA sequences, calculate their GC content, and compare two sequences for mutations.

## Reason for Development

BaseBud was developed as an exercise to learn **list comprehension** in Python and to explore the implementation of Python in the field of **biology**. This project serves as a practical application of programming concepts while bridging the gap between computational techniques and biological analysis.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Liscense](#license)

## Features

- Input multiple DNA sequences.
- Calculate and display the GC content of each sequence.
- Compare two sequences to identify mutations.
- User-friendly command-line interface.

## Installation

To use BaseBud, you'll need to have Python installed on your machine and a terminal emulator. Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/Bjorn99/BaseBud.git
   cd BaseBud
   ```

2. Run the script:
- 
   ```bash
   python basebud.py
   ```

## Usage

1. Start the program by executing the script.
2. Enter DNA sequences when prompted. Type `exit` to finish inputting sequences.
3. The program will calculate and display the GC content for each sequence.
4. If you have entered at least two sequences, you can select two sequences to compare for mutations.

## Code Explanation

The BaseBud script consists of several key functions:

### Input Sequences

```python
def input_sequences():
    sequences = []
    while True:
        seq = input("Enter a DNA sequence (or type 'exit' to finish):")
        if seq.lower() == 'exit':
            break
        else:
            sequences.append(seq)

    return sequences
```
- Purpose: This function prompts the user to input DNA sequences until they type 'exit'.
- Returns: A list of entered sequences.

### Calculate GC Content

```python
def gc_content(sequences):
        gc = [
            (seq.count('G') + seq.count('C')) / len(seq) * 100 if 
            len(seq) > 0 else 0
            for seq in sequences
        ]

        return gc
```
- Purpose: This function calculates the GC content (percentage of 'G' and 'C' bases) for each sequence.
- Returns: A list of GC content percentages.

### Finding Mutations

```python
def mut_detect(s1, s2):
    mutations = []
    min_length = min(len(s1), len(s2))
    for i in range(min_length):
        if s1[i] != s2[i]:
            mutations.append((i, s1[i], s2[i])) # (position, base in s1, s2)

    return mutations

def print_bold(text):
    print(f'\033[1m{text}\033[0m')
```

- Purpose: This function mainly compares two sequences by comparing them base by base and returns the difference in base in the same exact position.

- Returns: A list of 'mutations', each represented by a tuple containing the postion and differing bases.

### Print Bold Text

```python
def print_bold(text):
    print(f'\033[1m{text}\033[0m') # ANSI escape code for bold text
```
- Purpose: This function prints text in bold for better readability in the command line.
- Remark: In some parts of the code, this function is not used. Only the ANSI escape code is used as I wanted only the result to be bold, not the whole return.

### Main Function
```python
def main():
    sequences = input_sequences()
    gc_con = gc_content(sequences)
    for seq, gc in zip(sequences, gc_con):
        print(f"Sequence: {seq}, \n \n \033[1mGC Content: {gc:.2f}%\033[0m \n")

    
    # Allowing users to compare two sequences
    if len(sequences) >= 2:
        print("\nSelect two sequences to compare:")
        for index, seq in enumerate(sequences):
            print_bold(f"{index}: {seq}")
        s1_index = int(input("Enter the index of the first sequence: "))
        s2_index = int(input("Enter the index of the second sequene: "))

        # Print the GC content of the given sequences
        gc1 = gc_con[s1_index]
        gc2 = gc_con[s2_index]
        print(f"GC content of selected sequences: {sequences[s1_index]}: \033[1mGC Content: {gc1:.2f}%\033[0m, \n{sequences[s2_index]}: \033[1mGC Content: {gc2:.2f}%\033[0m")

        mutations = mut_detect(sequences[s1_index], sequences[s2_index])

        if mutations:
            print_bold("\nMutations found:")
            for position, base1, base2 in mutations:
                print_bold(f"Position {position}: {base1} -> {base2}")
        else:
            print_bold("No mutations found between the selected sequences.")
    else:
        print_bold("Not enough sequences to compare")
```

- Purpose: This `main()` function dictates the flow of the code or the program, calling the other functions to input sequences, calculate GC content, and compare the sequences for mutations.

### Not a module

```python
if __name__ == "__main__":
    main()
```

- Purpose: `if __name__ == "__main__"` is a common idiom in Python and a condition  which allows you to specify Python code that should only execute when the script is run directly. When the script is run directly, `__name__` is set to `"__main__"`. However, if the module is imported to another script, `__name__` is set to that very module's name.