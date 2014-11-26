"""Find most common title words
Run:
$ python top_title_words.py user-visits_msweb.data > top_title_words.out
"""

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopTitleWords(MRJob):

    def mapper(self, line_no, line):
        cell = csv_readline(line)
        if cell[0] == 'A':
            words = cell[3].lower().split()
            for word in words:
                yield word, 1

    def reducer_count(self, word, count):
        total = sum(count)
        yield 1, (total, word)

    def reducer_sort(self, _, count_word):
      word_list = sorted(count_word, reverse=True)
      for w in word_list[:10]:
          yield w

    def steps(self):
        return [
            self.mr(mapper=self.mapper,
                    reducer=self.reducer_count),
            self.mr(reducer=self.reducer_sort)
          ]

if __name__ == '__main__':
    TopTitleWords.run()
