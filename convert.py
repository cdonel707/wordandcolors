def letter_to_number(letter):
    """Convert a letter to its corresponding number (a=1, b=2, etc.) and multiply by 9.84"""
    return (ord(letter.lower()) - ord('a') + 1) * 9.84

def combine_values(values):
    """Combine values and handle overflow at 256"""
    total = sum(values)
    while total >= 256:
        total -= 256
    return total

def word_to_rgb(word):
    # Convert each letter to its numerical value
    numbers = [letter_to_number(letter) for letter in word if letter.isalpha()]
    
    # Initialize RGB values
    rgb = [0, 0, 0]
    
    # Group letters by their RGB position (0=R, 1=G, 2=B)
    for i, value in enumerate(numbers):
        rgb_position = i % 3
        
        # If this is a subsequent pass (i >= 3), combine with existing value
        if i >= 3:
            rgb[rgb_position] = combine_values([rgb[rgb_position], value])
        else:
            rgb[rgb_position] = value

    return tuple(int(x) for x in rgb)  # Convert float values to integers

def main():
    while True:
        word = input("Enter a word (or 'quit' to exit): ")
        
        if word.lower() == 'quit':
            break
            
        rgb = word_to_rgb(word)
        hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb)
        print(f"RGB values for '{word}': R={rgb[0]}, G={rgb[1]}, B={rgb[2]}")
        print(f"Hex color: {hex_color}")
        print(f"View color details: https://www.colorhexa.com/{hex_color[1:]}")  # Remove the # from hex_color

if __name__ == "__main__":
    main()
