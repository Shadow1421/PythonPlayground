# # DNA Analysis
# # In this project, we’ll use many of the concepts you’ve learned throughout the Python course in order to do some DNA analysis for a crime investigation.

# # The scenario:

# # A spy deleted important files from a computer. There were a few witnesses at the scene of the crime, but no one is sure who exactly the spy was. Three possible suspects were apprehended based on surveillance video. Each suspect had a sample of DNA taken from them. The computer’s keyboard was also swabbed for DNA evidence and, luckily, one small DNA sample was successfully retrieved from the computer’s keyboard.

# # Given the three suspects’ DNA and the sample DNA retreived from the keyboard, it’s up to you to figure out who the spy is!

# # The project should have methods for each of the following:

# # Given a file, read in the DNA for each suspect and save it as a string
# # Take a DNA string and split it into a list of codons
# # Iterate through a suspect’s codon list to see how many of their codons match the sample codons
# # Pick the right suspect to continue the investigation on

# Descriptive answer
# To complete the DNA analysis for the crime investigation project, you can follow the steps outlined below:

# 1. Read in the DNA for each suspect from a file and save it as a string:
#    - Create a function to read the DNA data from a file.
#    - Open the file and read its contents.
#    - Save the DNA data for each suspect as a string.

# 2. Split the DNA string into a list of codons:
#    - Create a function to split a DNA string into a list of codons.
#    - Use string slicing or regular expressions to divide the DNA string into groups of three characters.
#    - Append each codon to a list.

# 3. Iterate through a suspect's codon list to count matching codons:
#    - Create a function to compare a suspect's codon list with the sample codon list.
#    - Iterate through each codon in the suspect's list and check if it matches the corresponding codon in the sample list.
#    - Keep track of the count of matching codons.

# 4. Pick the right suspect to continue the investigation:
#    - Compare the counts of matching codons for each suspect.
#    - Identify the suspect with the highest count of matching codons as the potential spy.
#    - Provide the result or further investigate the potential spy based on the count of matching codons.

# By implementing these methods, you will be able to read the DNA data, split it into codons, compare the codons, and determine the most likely suspect in the crime investigation.

# Read DNA data from a file and save it as a string
def read_dna_file(file_name):
    print(file_name)
    with open(file_name, 'r') as file:
        dna_data = file.read().replace('\n', '')
    return dna_data

# Split DNA string into a list of codons
def split_codons(dna_string):
    codons = [dna_string[i:i+3] for i in range(0, len(dna_string), 3)]
    return codons

# Compare suspect's codons with sample codons and count matching codons
def count_matching_codons(suspect_codons, sample_codons):
    matching_count = 0
    for suspect_codon, sample_codon in zip(suspect_codons, sample_codons):
        if suspect_codon == sample_codon:
            matching_count += 1
    return matching_count

# Pick the suspect with the highest count of matching codons
def identify_spy(suspect_data, sample_data):
    sample_codons = split_codons(sample_data)
    suspects = {}
    for suspect_name, suspect_dna in suspect_data.items():
        suspect_codons = split_codons(suspect_dna)
        matching_count = count_matching_codons(suspect_codons, sample_codons)
        suspects[suspect_name] = matching_count

    # Find the suspect with the highest count of matching codons
    spy = max(suspects, key=suspects.get)
    return spy

# Example usage
if __name__ == '__main__':
    suspect_data = {
        'Suspect 1': read_dna_file('DNA-assessment/suspect1.txt'),
        'Suspect 2': read_dna_file('DNA-assessment/suspect2.txt'),
        'Suspect 3': read_dna_file('DNA-assessment/suspect3.txt')
    }

    sample_data = ['GTA','GGG','CAC']

    spy = identify_spy(suspect_data, sample_data)
    print("The spy is:", spy)
