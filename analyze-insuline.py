import re

# Read the content of the .txt file
with open('preproinsulin-seq.txt', 'r') as file:
    content = file.read()

# Convert the content to lowercase
content_lower = content.lower()

# Remove the word "ORIGIN" from the content
content_without_origin = content_lower.replace("origin", "")

# Use regex to extract the lowercase protein sequence
matches = re.findall(r'([a-z]+)', content_without_origin)

# Join the matches to form the cleaned sequence
cleaned_sequence = ''.join(matches)

# Check if the cleaned sequence has exactly 110 characters
if len(cleaned_sequence) == 110:
    # Print the amino acids 1–24 characters of the cleaned sequence
    amino_acids_1_24 = cleaned_sequence[:24]
    print("Insulin-seq:", amino_acids_1_24)
    print("Number of characters:", len(amino_acids_1_24))

    # Check if the first 24 characters are exactly 24 characters
    if len(amino_acids_1_24) == 24:
        print("The first 24 characters are okay.")
    else:
        print("Error: The first 24 characters are not 24 characters.")

    # Save amino acids 1–24 to lsinsulin-seq-clean.txt
    with open('lsinsulin-seq-clean.txt', 'w') as ls_file:
        ls_file.write(amino_acids_1_24)
        print("Saved amino acids 1–24 to lsinsulin-seq-clean.txt.")

    # Print the amino acids 25–54 characters of the cleaned sequence
    amino_acids_25_54 = cleaned_sequence[24:54]
    print("Binsulin-seq:", amino_acids_25_54)
    print("Number of characters:", len(amino_acids_25_54))

    # Check if the next 30 characters are exactly 30 characters
    if len(amino_acids_25_54) == 30:
        print("The next 30 characters are okay.")
    else:
        print("Error: The next 30 characters are not 30 characters.")

    # Save amino acids 25–54 to binsulin-seq-clean.txt
    with open('binsulin-seq-clean.txt', 'w') as binsulin_file:
        binsulin_file.write(amino_acids_25_54)
        print("Saved amino acids 25–54 to binsulin-seq-clean.txt.")

    # Print the amino acids 55–89 characters of the cleaned sequence
    amino_acids_55_89 = cleaned_sequence[54:89]
    print("Cinsulin-seq:", amino_acids_55_89)
    print("Number of characters:", len(amino_acids_55_89))

    # Check if the next 35 characters are exactly 35 characters
    if len(amino_acids_55_89) == 35:
        print("The next 35 characters are okay.")
    else:
        print("Error: The next 35 characters are not 35 characters.")

    # Save amino acids 55–89 to cinsulin-seq-clean.txt
    with open('cinsulin-seq-clean.txt', 'w') as cinsulin_file:
        cinsulin_file.write(amino_acids_55_89)
        print("Saved amino acids 55–89 to cinsulin-seq-clean.txt.")

    # Print the amino acids 90–110 characters of the cleaned sequence
    amino_acids_90_110 = cleaned_sequence[89:110]
    print("Ainsulin-seq:", amino_acids_90_110)
    print("Number of characters:", len(amino_acids_90_110))

    # Check if the last 21 characters are exactly 21 characters
    if len(amino_acids_90_110) == 21:
        print("The last 21 characters are okay.")
    else:
        print("Error: The last 21 characters are not 21 characters.")

    # Save amino acids 90–110 to ainsulin-seq-clean.txt
    with open('ainsulin-seq-clean.txt', 'w') as ainsulin_file:
        ainsulin_file.write(amino_acids_90_110)
        print("Saved amino acids 90-110 to ainsulin-seq-clean.txt.")
else:
    print("Error: The cleaned sequence does not have 110 characters. Expected 110, got", len(cleaned_sequence))
