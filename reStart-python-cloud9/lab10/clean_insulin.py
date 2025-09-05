# Remove:

# ORIGIN

# The numbers (1, 61)

# The double slashes //

# All spaces and line breaks

main_file = open("preproinsulin-seq.txt", 'r')

# print(file.read())
# Save this as: preproinsulin-seq-clean.txt
# vim preproinsulin-seq-clean.txt 
# Create and write new text file 
with open("preproinsulin-seq-clean.txt", 'w') as file:
    for line in main_file:
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
            # print(file=file)
main_file.close()

file1 = open("preproinsulin-seq-clean.txt", 'r')
print(file1.read())

# Extract subsequences (insulin components) 
# Signal peptide (lsinsulin): amino acids 1–24 output malwmrllpllallalwgpdpaaaf
# Save in lsinsulin-seq-clean.txt → should be 24 characters.
with open("lsinsulin-seq-clean.txt", 'w') as file1:
    # Iterate and get the first 24 characters from file2 = "preproinsulin-seq-clean.txt"
    for i, char in enumerate(open("preproinsulin-seq-clean.txt").read()):
        if i < 25:
            file1.write(char)
print(f'{len(open("lsinsulin-seq-clean.txt").read())} characters written to lsinsulin-seq-clean.txt')
file1.close()


# In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as binsulin-seq-clean.txt.
# In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.
with open('binsulin-seq-clean.txt', 'w') as file1:
    for i, char in enumerate(open("preproinsulin-seq-clean.txt").read()):
        if 24 < i < 55:
            file1.write(char)
print(f'{len(open("binsulin-seq-clean.txt").read())} characters written to binsulin-seq-clean.txt')

# In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as cinsulin-seq-clean.txt.
# In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.
with open('cinsulin-seq-clean.txt', 'w') as file1:
    for i , char in enumerate(open("preproinsulin-seq-clean.txt").read()):
        if 54 < i < 90:
            file1.write(char)
print(f'{len(open("cinsulin-seq-clean.txt").read())} characters written to cinsulin-seq-clean.txt')
file1.close()


# In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as ainsulin-seq-clean.txt.
# In ainsulin-seq-clean.txt, save amino acids fy that y90–110. Veriour file has 21 characters.
with open('ainsulin-seq-clean.txt', 'w') as file1:
    for i, char in enumerate(open("preproinsulin-seq-clean.txt").read()):
        if 89 < i < 111:
            file1.write(char)
print(f'{len(open("ainsulin-seq-clean.txt").read())} characters written to ainsulin-seq-clean.txt')
file1.close()
