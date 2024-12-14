def main():
    s=string = "AI is important for its potential to change how we live, work and play. It has been effectively used in business \
to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a \
number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, \
such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete \
jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises \
insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will \
be important in fields ranging from education and marketing to product design."
    word_count = 1
    for i in range(len(string)):
        if string[i] == ' ':
            word_count += 1
    print("The number of words in the string is:", word_count)
    ALPHABETS_COUNT = 26
    letter_count = [0] * ALPHABETS_COUNT
    word_start = True
    SMALL_A = ord('a')
    SMALL_Z = ord('z')
    for ch in string:
        ch_value = ord(ch)          #convert character to number
        ch_value = (ch_value | 32)  #perform oring to convert capital alphabet to small alphabet
        ch = chr(ch_value)          #convert back to character to get small alphabets
        if word_start and ch_value >= SMALL_A and ch_value <= SMALL_Z:
            letter_count[ch_value - SMALL_A] += 1
            word_start = False
        if ch == ' ' or ch == '.' or ch == ',':
            word_start = True
    sum = 0
    for i in range(ALPHABETS_COUNT):
        if letter_count[i] != 0:
            sum += letter_count[i]
            print("The letter ", chr(i + SMALL_A), " appears ", letter_count[i], " times in the string.")
    print('Total words count by adding word count of individual alphabets: ', sum)

    max_length = 0
    max_word_index = 0
    count = 0
    for i in range(len(s)):
        if s[i] != ' ' and s[i] != '.' and s[i] != ',':
            count += 1
        else:
            if count > max_length:
                max_length = count
                max_word_index = i - count
            count = 0

    print("Maximum length of word is:", max_length)
    print("The word is:", s[max_word_index: max_word_index + max_length])
    sentence_count = 0
    for ch in s:
        if ch == '.':
            sentence_count += 1
    print("Total sentences:", sentence_count)

main()
