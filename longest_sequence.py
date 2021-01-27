import sys

def main(argv):

    # Check argument count
    if len(argv) != 2:
        print("Incorrect argument count. Specify input file.")
        sys.exit(1)

    else:

        # Attempt to open and read from file
        try:
            with open(argv[1]) as infile:
                text = infile.read()

        except FileNotFoundError:
            print("Could not open file.")
            sys.exit(2)

    # Store data here
    sequence = list()
    longest_sequence = list()

    for word in text.split():

        # Add first word from text to list
        # Assign last letter of word to current marker
        if len(sequence) == 0:
            sequence.append(word)
            last_char = word[-1]
        
        # If there is a word in list
        else:

            # If current last letter = last letter being tracked,
            # add the current word to list
            if word[-1] == last_char:
                sequence.append(word)

            else:
                
                # If current sequence is longer than longest so far,
                # replace the longest with current and clear current
                if len(sequence) > len(longest_sequence):
                    longest_sequence = sequence.copy()

                # Clear current sequence, add new word and reassign last char
                sequence.clear()
                last_char = word[-1]
                sequence.append(word)

    length = len(longest_sequence)
    longest_sequence = ' '.join(longest_sequence)
    print(f'The longest sequence of consecutive words ending with the same letter from {argv[1]} is: "{longest_sequence}".\n length: {length}')


if __name__ == "__main__":
    main(sys.argv) 