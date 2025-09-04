# Remove:

# ORIGIN

# The numbers (1, 61)

# The double slashes //

# All spaces and line breaks

file1 = open('preproinsulin-seq.txt', 'r')
print(f'{file1}')

# Save this as: preproinsulin-seq-clean.txt
file2 = "preproinsulin-seq-clean.txt"
# vim preproinsulin-seq-clean.txt 
# Create and write new text file 
with open(file2, 'w') as file:
    for line in file1:
        if "ORIGIN" in line:
            continue
        elif "//" in line:
            continue
        elif line[0].isdigit():
            continue
        else:
            # Remove all spaces and line breaks
            clean_line = line.replace(" ", "").replace("\n", "").replace("1", "")
            file.write(clean_line)
print(f'{file2}') 

file1.close()


# Extract subsequences (insulin components) 
# Signal peptide (lsinsulin): amino acids 1–24 output malwmrllpllallalwgpdpaaaf
# Save in lsinsulin-seq-clean.txt → should be 24 characters.
file3 = "lsinsulin-seq-clean.txt"
with open(file3, 'w') as file:
    # Iterate and get the first 24 characters from file2 = "preproinsulin-seq-clean.txt"
    for i, char in enumerate(open(file2).read()):
        if i < 25:
            file.write(char)
    print(f'{file}')        
print(f'{file3}')

