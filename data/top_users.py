"""Find users with more than 20 visits.
Run:
$ python users_20.py user-visits_msweb.data > user-visits_msweb.out
"""

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopUsers(MRJob):

    def mapper(self, line_no, line):
        """Extracts the user"""
        cell = csv_readline(line)
        if cell[0] == 'V':
            yield cell[3], 1

    def reducer(self, user, visit_counts):
        """Sumarizes the visit counts by adding them together.  If total visits
        is more than 20, yield the results"""
        total = sum(visit_counts)
        if total > 20:
            yield user, total

if __name__ == '__main__':
    TopUsers.run()
