class NoMostCommonThree(Exception):
    """Custom exception for cases where the three most common letters are not found."""

def most_common_three(sentence):
    """Return the three most common letters from the given sentence.

    Args:
    sentence (str): The input sentence.

    Returns:
    list: A list containing the three most common letters.

    Raises:
    NoMostCommonThree: If any of the most common letters have a count of 0.
    """
    # Initialise dictionary to store letter occurances
    occurrences = {chr(i): 0 for i in range(97, 123)}	# ASCII values for lowercase alphabets
    
    # Loop through each letter in the sentence, ignoring spaces and case
    for letter in sentence.replace(" ", "").lower():
        occurrences[letter] += 1

    # Sort the letter occurrences in descending order
    occurences_sorted = {
	k: v for k, v in sorted(occurrences.items(), key=lambda item: item[1], reverse=True)
    }

    # Collect the counts of the three most common letters
    result = []
    for i in range(3):
        result.append(list(occurences_sorted.keys())[i])
        
        # Check if any of the most common letters have a count of 0
        if occurences_sorted.get(list(occurences_sorted.keys())[i]) == 0:
            raise NoMostCommonThree

    return result

print(most_common_three('the month today is April not June'))
