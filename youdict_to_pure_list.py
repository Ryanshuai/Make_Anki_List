def is_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


input_txt = 'youdict.xml'

with open(input_txt, encoding='utf-8') as f:
    lines = f.readlines()

new_lines = list()

# for i, line in enumerate(lines):
#     if '</item><item>' in line:
#         word = '"' + line[23:-8] + '",'
#         if not is_contain_chinese(word):
#             new_lines.append(word)

# output_txt = 'youdict.py'
# with open(output_txt, 'w', encoding='utf-8') as f:
#     f.write('youdict_word_list = [')
#     for word in new_lines:
#         f.write(word)
#         f.write('\n')
#     f.write(']')


for i, line in enumerate(lines):
    if '</item><item>' in line:
        word = line[23:-8]
        if not is_contain_chinese(word):
            new_lines.append(word)
output_txt = 'youdict.txt'
with open(output_txt, 'w', encoding='utf-8') as f:
    for word in new_lines:
        f.write(word)
        f.write('\n')
