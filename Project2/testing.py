from Sort import Sort, Modified_Sort
c = Sort([1, 3, 2, 0, 3, 2])
# c.SortSelection()
# print(c.show())
#
# c.SortBubble()
# print(c.show())
#
# c.SortInsertion()
# print(c.show())

# c = Sort([1, 3, 2, 0, 3, 2])
# n = Modified_Sort([1, 3, 2, 0, 3, 2], 0, 3)

# n.SortBubble()
# print(n.show())

# n.SortInsertion()
# print(n.show())

# n.SortSelection()
# print(n.show())


class Qustion:
     def __init__(self, s1, s2):
         self.text = s1
         self.answer = s2


# new_sentences = Qustion()

sentences = [
    {'text': 'Algorithms: SortBubble, SortInsertion, SortSelection:', 'answer1': 'SortBubble',
     'answer2': 'SortInsertion', 'answer3': 'SortSelection'},
    {'text': 'Enter a start of sorting: ', 'answer': list(Modified_Sort.__init__().sorting_from)},
    {'text': 'Enter a start of sorting: ', 'answer': list(Modified_Sort.__init__().sorting_to)},
    {'text': 'Processing that up....', 'answer': ''},
    {'text': 'Here is your list sorted:',  'answer': f'{Modified_Sort.list}'},

]

sentence_bank = []
for sentence in sentence_bank:
    sentence_text = sentence['text']
    sentence_answer = sentence['answer']
    new_sentences = Qustion(sentence_text, sentence_answer)
    sentence_bank.append(new_sentences)

