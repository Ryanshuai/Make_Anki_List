# def make_pure_word_list(word_set):
#     cigencizhui_root = Cigencizhui_Root()
#     with open('pure_word_list.txt', 'w', encoding='utf-8') as f:
#         ordered_input_word_list = cigencizhui_root.put_word_list_in_order(word_set)
#         for word in ordered_input_word_list:
#             print(word)
#             f.write(word)
#             f.write('\n')


def make_anki_word_image_list(word_set):
    with open('./output/anki_word_image_list.txt', 'w', encoding='utf-8') as f:
        final_word_list = word_set
        print('ordered_input_word_list: ', len(final_word_list))
        for word in final_word_list:
            word = word.strip()
            line = word
            for i in range(1, 11):
                line += "\\<img src=\"{}.jpg\" />".format("word_" + word + str(i))
            f.write(line)
            f.write('\n')


def make_gre_synonym_image_list(word_set):
    with open(word_set, 'r', encoding='utf-8') as f:
        word_list = f.read().splitlines()

    with open('./output/GRE_anki_same.txt', 'w', encoding='utf-8') as f:
        for word in word_list:
            word = word.strip()
            if len(word) == 0:
                continue
            print(word)
            if '\u4e00' <= word[0] <= '\u9fff':
                now_class = word
            else:
                line = word
                for i in range(1, 11):
                    line += "\\<img src=\"{}.jpg\" />".format(word + str(i))
                line += "\\" + now_class
                f.write(line)
                f.write('\n')


def make_anki_delete_list(word_set):
    with open('./output/anki_delete_list.txt', 'w', encoding='utf-8') as f:
        for word in word_set:
            word = word.strip()
            line = word
            line += '\\_____'
            f.write(line)
            f.write('\n')


if __name__ == '__main__':
    input_txt = "./word_list_txt/TOEFL_红宝书.txt"

    word_set = set()
    with open(input_txt, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            word_set.add(word)

    make_anki_word_image_list(word_set)
