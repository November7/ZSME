def load_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def sentences(input_text):
    txt = input_text.replace('?', '.')
    txt = txt.replace('!', '.')
    txt = txt.replace(';', '.')
    ret = txt.split('.')
    for i in range(len(ret)):
        ret[i] = ret[i].strip()
    return ret

def clearing(input_text):
    input_text = input_text.lower()
    for char in input_text:
        if (char < 'a' or char > 'z') and char != ' ':
            input_text = input_text.replace(char, '')
    return input_text

def stats(input_text,stopwords):
    word_dict = {}
    for word in input_text.split():
        if word in stopwords:
            continue
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def scoring(sentences_list, word_stats, alpha):
    sentence_scores = {}
    for sentence in sentences_list:
        words = sentence.split()
        score = 0
        for w in words:
            score += word_stats.get(w, 0)  
        n = len(words)      
        if n> 0:
            score = score / n**alpha
        sentence_scores[sentence] = score
    return sentence_scores


import matplotlib.pyplot as plt

def main():
    content = load_data(r'D:\Marcin\Source\ZSME\Examples\2025-2026 2TP\allice.txt')
    
    stopwords = {
        "the","and","is","a","to","in","of","that","it","on","for","with","as","was",
        "were","be","by","this","are","at","from","or","an","but","not","so","if",
        "then","there","their","they","you","your","i","me","my","we","our"
    }

    
    sentences_list = sentences(content)

    for i in range(len(sentences_list)):
        sentences_list[i] = clearing(sentences_list[i])
    
    # print(sentences_list)

    new_content = ''
    
    for sentence in sentences_list:
        new_content += sentence + ' '

    stats_dict = stats(new_content, stopwords)
    sorted_words = sorted(stats_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_words)

    top_words = sorted_words[0:10]
    words = [word for word, _ in top_words]
    counts = [count for _, count in top_words]   
    plt.bar(words, counts)
    plt.xlabel('Words')

    plt.ylabel('Counts')
    plt.title('Top 10')
    plt.show()

    print(stats_dict)
    with open(r'D:\Marcin\Source\ZSME\Examples\2025-2026 2TP\20260116_output.txt', 'w', encoding='utf-8') as file:
        for word, count in sorted_words:
            file.write(f'{word}: {count}\n')

    score_dict = scoring(sentences_list, stats_dict, .5)
    score_dict = dict(sorted(score_dict.items(), key=lambda item: item[1], reverse=True))
    summary = list(score_dict.keys())[:5]
    print("Summary:")
    for s in summary:
        print("-", s)


if __name__ == '__main__':
    main()