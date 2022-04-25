# Problem Set 4A
# Name: Aloisio Valério Jr.
# Collaborators:
# Time Spent: x:xx started 9:30

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []

    if len(sequence) == 1:
        return [sequence]
    else:
        first_char = sequence[0]
        permutations_of_rest = get_permutations(sequence[1:])

        for word in permutations_of_rest:
            for i in range(len(word)+1):
                permutations.append(word[0:i] + first_char + word[i:])
        return permutations


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    print('----------------')

    base_case = 'a'
    print('Input:', base_case)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(base_case))

    print('----------------')

    two_letter_case = 'ab'
    print('Input:', two_letter_case)
    print('Expected Output:', ['ab','ba'])
    print('Actual Output:', get_permutations(two_letter_case))

    

