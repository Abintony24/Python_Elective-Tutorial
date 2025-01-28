def count_words(text):
    return len(text.split())

def count_sentences(text):
    punctuations = ['.', '?', '!']
    count = 0
    for char in text:
        if char in punctuations:
            count += 1
    return count if count > 0 else 1  # Ensure at least one sentence

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(word) <= 3:
        return 1

    if word[-2:] == 'es' or word[-2:] == 'ed':
        if len(word) > 2 and word[-3:] != 'les':
            word = word[:-2]
    elif word[-1:] == 'e':
        if len(word) > 1 and word[-2:] != 'le':
            word = word[:-1]

    previous_was_vowel = False
    for char in word:
        if char in vowels:
            if not previous_was_vowel:
                count += 1
            previous_was_vowel = True
        else:
            previous_was_vowel = False

    return count if count > 0 else 1  # Ensure at least one syllable

def total_syllables(text):
    total_count = 0
    for word in text.split():
        total_count += count_syllables(word)
    return total_count

def find_flesch_index(words, sentences, syllables):
    if words == 0 or sentences == 0:
        return 0
    return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

def find_grade(words, sentences, syllables):
    if words == 0 or sentences == 0:
        return 0
    return 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59

def readability_score(flesch_index):
    if flesch_index >= 90:
        return "4th Grade"
    elif flesch_index >= 50:
        return "High School"
    return "College"

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        text = file.read()

    words = count_words(text)
    sentences = count_sentences(text)
    syllables = total_syllables(text)

    flesch_index = find_flesch_index(words, sentences, syllables)
    grade = find_grade(words, sentences, syllables)

    print(f"Flesch Index : {flesch_index:.2f}")
    print(f"Grade : {grade:.2f}")
    print(f"Readability : {readability_score(flesch_index)}")
