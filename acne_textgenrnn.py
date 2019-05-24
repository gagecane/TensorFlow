from textgenrnn import textgenrnn
import tensorflow as tf
import numpy as np


path_to_file = "C:\\Users\\gagec\\Documents\\Code\\Docker\\out.txt"

# You can use train_on_texts with context labels as well by providing
# a list of context labels of the same size as the texts.
#
# In [ ]:
# texts = ['Never gonna give you up, never gonna let you down',
#             'Never gonna run around and desert you',
#             'Never gonna make you cry, never gonna say goodbye',
#             'Never gonna tell a lie and hurt you']
#
# context_labels = ['Verse 1', 'Verse 1', 'Verse 2', 'Verse 2']
#
# textgen.reset()
# textgen.train_new_model(texts, context_labels=context_labels, max_length=5,
#                         gen_epochs=5, num_epochs=10)

textgen = textgenrnn()
textgen.train_from_file(path_to_file, num_epochs=100)
textgen.generate()
