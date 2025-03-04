"""Reverse the order of words in a given sentence (a string of words)."""
def reverse_words_in_sentence(sentence: str) -> str:
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed words into a new sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Example usage:
input_sentence = "Hello world this is a test"
output_sentence = reverse_words_in_sentence(input_sentence)
print(f"Original: {input_sentence}")
print(f"Reversed: {output_sentence}")
