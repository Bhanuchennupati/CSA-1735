import itertools

def solve_cryptarithmetic(puzzle):
    # Extract unique letters from the puzzle
    letters = set(char for word in puzzle for char in word)
    
    # Filter out letters that start a word (no leading zeros)
    leading_letters = {word[0] for word in puzzle if len(word) > 1}
    
    # Generate all possible digit permutations for the unique letters
    for perm in itertools.permutations(range(10), len(letters)):
        # Skip permutations that assign 0 to a leading letter
        if any(perm[letters.index(char)] == 0 for char in leading_letters):
            continue
        
        # Map letters to digits in the current permutation
        digit_map = dict(zip(letters, perm))
        
        # Convert words to numbers based on digit_map
        numbers = [int(''.join(str(digit_map[char]) for char in word)) for word in puzzle[:-1]]
        result = sum(numbers)
        expected_result = int(''.join(str(digit_map[char]) for char in puzzle[-1]))
        
        # Check if the current permutation satisfies the puzzle
        if result == expected_result:
            return digit_map
    
    return None

if __name__ == "__main__":
    puzzle = ["SEND", "MORE", "MONEY"]
    solution = solve_cryptarithmetic(puzzle)
    
    if solution:
        print("Solution found:")
        for char, digit in sorted(solution.items()):
            print(f"{char}: {digit}")
    else:
        print("No solution found.")
