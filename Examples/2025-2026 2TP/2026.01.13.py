def clearing(input_text):
    input_text = input_text.lower()
    input_text = input_text.replace('\n', '')
    input_text = input_text.replace('?', '.')
    input_text = input_text.replace(';', '.')
    input_text = input_text.replace('!', '.')
    for char in input_text:
        if (char < 'a' or char > 'z') and char != ' ' and char != '.':
            input_text = input_text.replace(char, '')
    return input_text 

def word_count(input_text):
    word_dict = {}
    for word in input_text.split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def remove_stopwords(input_text, stopwords):
    clear_content = ''
    for word in input_text.split():
        if word not in stopwords:
            clear_content += word + ' '
    return clear_content

def sentences(input_text):
    ret = input_text.split('.')
    for i in range(len(ret)):
        ret[i] = ret[i].strip()
    ret = [ret[i] for i in range(len(ret)) if ret[i] != '']
    return ret

def score_sentences(sentences_list, word_counts, stopwords):

    sentence_scores = {}
    for sentence in sentences_list:
        original_sentence = sentence
        sentence = clearing(sentence)
        sentence = remove_stopwords(sentence, stopwords)

        score = 0
        for word in sentence.split():
            if word in word_counts:
                score += word_counts[word]
        sentence_scores[original_sentence] = score
    return sentence_scores

def main():
    filename_in = r'D:\Marcin\Source\ZSME\Examples\2025-2026 2TP\allice.txt'
    with open(filename_in, 'r', encoding='utf-8') as file:
        content = file.read()


    original_content = content


    content = clearing(content)

    stopwords = {"the","and","is","a","to","in","of","that","it","on","for","with" }

    content = remove_stopwords(content, stopwords)

    # print(content)

    word_counts = word_count(content)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    # for word, count in sorted_words[:10]:
    #     print(f'"{word}" : {count}')    


    filename_out = r'D:\Marcin\Source\ZSME\Examples\2025-2026 2TP\out.txt'
    with open(filename_out, 'w', encoding='utf-8') as file:
        for word, count in sorted_words:
            file.write(f'{word}: {count}\n')



    from matplotlib import pyplot as plt
    top_words = sorted_words[0:10]
    words = [word for word, count in top_words]
    counts = [count for word, count in top_words]   
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Counts')
    plt.title('Top 10 Most Frequent Words')
    plt.show()

    sentences_list = sentences(original_content)


    sentence_scores = score_sentences(sentences_list, word_counts, stopwords)
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

    for sentence, score in sorted_sentences[:3]:
        print(f'{sentence}')


if __name__ == "__main__":
    main()

