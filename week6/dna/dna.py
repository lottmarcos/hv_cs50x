import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Incorrect inputs")
        exit()
    filename = sys.argv[1]

    with open(filename) as e:
        reader = csv.DictReader(e)
        database = list(reader)

    filename = sys.argv[2]
    with open(filename) as f:
        sequence = f.read()

    matches = {}

    for i in database[0]:
        matches[i] = (longest_match(sequence, i))

    # TODO: Check database for matching profiles
    suspect = 'No Match'
    suspect_counter = 1

    for i in range(len(database)):
        for j in matches:
            if str(matches[j]) == database[i][j]:
                suspect_counter += 1
        if suspect_counter == len(matches):
            suspect = database[i]['name']
            break
        else:
            suspect_counter = 1

    print(suspect)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
