#
def find_grades(grades, students):
    """
    grades is a dict mapping student names to grades
    students is a list of student names

    Returns a list containing the grades for students (in same order)
    """
    return [grades[student] for student in students]

d = {'Ana': 'B', 'Matt': 'C', 'John': 'B', 'Katy': 'A'}
print(find_grades(d, ['Matt', 'Katy'])) # ['C', 'A']


def find_in_L(Ld, k):
    """
    Ld is a list of dicts
    k is an int

    Returns True if k is a key in any dicts of Ld and False otherwise
    """
    for d in Ld:
        if k in d:
            return True
    return False

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(find_in_L([d1, d2, d3], 2))   # True
print(find_in_L([d1, d2, d3], 25))  # False


def count_matches(d):
    """
    d is a dict
    Returns how many entries in d have the key equal to its value
    """
    count = 0
    for k, v in d.items():
        if k==v:
            count += 1
    return count
    # return sum(k==v for k,v in d.items())

d = {1:2, 3:4, 5:6}
print(count_matches(d))     # 0

d = {1:2, 'a':'a', 5:5}
print(count_matches(d))     # 2


def generate_word_dict(lyrics):
    """
    Return a frequency dictionary mapping str:int
    """
    lyrics = lyrics.lower()
    words = lyrics.split()
    freq = {}
    
    for word in set(words):
        if word not in freq:
            freq[word] = 0
        freq[word] += words.count(word)
    
    return freq


def get_most_frequent_word(d):
    """
    Return the word(s) that occur most often
    => a tuple (list, int) for (words_list, highest_freq)
    """
    # d = generate_word_dict(lyrics)
    words = []
    max_freq = max(d.values())

    for word, freq in d.items():
        if freq == max_freq:
            words.append(word)
    return words, max_freq
    


lyrics = "The following questions are an opportunity to reflect on key topics in in this lesson. If you can't answer a question, click on it to review the material, but keep in mind you are not expected to memorize or master this knowledge."

# print(generate_word_dict(lyrics))
d = generate_word_dict(lyrics)
# print(get_most_frequent_word(d))


def most_often_at_least(word_dict, x):
    """
    Create a frequency dictionary mapping str:int
    Let users choose "at least x times"

    Returns a list of tuples, each tuple is a (list, int) containing the list of words ordered by their frequency
    => (list, int) for (words_list, highest_freq)

    """
    words = []
    most_freq = get_most_frequent_word(word_dict)

    while most_freq[1] > x:
        most_freq = get_most_frequent_word(word_dict)
        words.append(most_freq)
        for word in most_freq[0]:
            del (word_dict[word])
    return words

print()
print(most_often_at_least(d, 2))


print("\n======== Finger Exercises =========")
# Finger Exercises
def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    keys = []
    for k, v in aDict.items():
        if v==target:
            keys.append(k)
    return sorted(keys)

# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]


def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    keys = []
    for k, v in d.items():
        if sum(v) > 0:
            keys.append(k)
    return sorted(keys)

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]