def count_vowels(a):
    vowels = "aeiouAEIOU"
    count = 0

    for i in a:
        if i in vowels:
            count += 1

    return count
