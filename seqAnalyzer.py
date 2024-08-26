from Bio.Seq import Seq

# Defining input function for users to input the "DNA Strings."
def input_sequences():
    sequences = []
    while True:
        seq = input("Enter a DNA sequence (or type 'exit' to finish):")
        if seq.lower() == 'exit':
            break
        else:
            sequences.append(seq)

    return sequences


# calculating GC content
def gc_content(sequences):
        gc = [
            (seq.count('G') + seq.count('C')) / len(seq) * 100 if 
            len(seq) > 0 else 0
            for seq in sequences
        ]

        return gc


# Mutation detection functionality
def mut_detect(s1, s2):
    mutations = []
    min_length = min(len(s1), len(s2))
    for i in range(min_length):
        if s1[i] != s2[i]:
            mutations.append((i, s1[i], s2[i])) # (position, base in s1, s2)

    return mutations

def print_bold(text):
    print(f'\033[1m{text}\033[0m')


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
            

if __name__ == "__main__":
    main()

#print(input_sequences())
