from collections import Counter
import time


class BwtFmInterface:
    def __init__(self, text, suffix_array_factor=None, tally_factor=None, suffix_array_file=None, bwt_file=None):
        """
        Constructor for BwtFm.
        Parse suffix array and BWT from files. If those files are None, build BWT and suffix array.
        Count the number of each char and build first column.\n
        Parameters:
            text: String, required
            suffix_array_factor: Int, default = None
            tally_factor: Int, default = None
            suffix_array_file: String, default = None
            bwt_file: String, default = None
        """
        self._suffix_array_file = suffix_array_file
        self._bwt_file = bwt_file
        self._suffix_array_factor = suffix_array_factor
        self._tally_factor = tally_factor
        self._text = text + '$'

        print("Start building suffix array")
        start = time.time()
        self._suffix_array = self._build_suffix_array()
        end = time.time()
        print("Done building suffix array in", end - start, "seconds")

        print("Start building BWT")
        start = time.time()
        self._bwt = self._build_bwt()
        end = time.time()
        print("Done building BWT in", end - start, "seconds")

        self._counts_per_char = self._build_counts_per_char()
        self._first_column = self._build_first_column()


    def _build_suffix_array(self):
        pass

    def _build_bwt(self):
        """
        Builds BWT.
        Parse bwt_file if exists. If not, build BWT from suffix array.
        """
        if self._bwt_file == None:
            bwt = [self._text[suffix_start - 1] if suffix_start != 0 else '$' for suffix_start in self._suffix_array]
            return ''.join(bwt)
        else:
            with open(self._bwt_file, "r") as file:
                return file.read()

    def _build_counts_per_char(self):
        """
        Returns a count of each character in BWT.
        """
        return dict(Counter(self._bwt))

    def _build_first_column(self):
        """
        Returns an array of tuples, which represents the first column of BWT matrix.
        Each tuple represents start and end position of each characher in first column of BWT matrix.\n
        """
        first_column = {}
        total_count = 0
        for c, count in sorted(self._counts_per_char.items()):
            first_column[c] = (total_count, total_count + count)
            total_count += count
        return first_column

    def _get_b_rank(self, bwt_index):
        pass

    def _get_first_column_index(self, c, b_rank):
        """
        Returns an index (Int) of character c in the first of column in the BWT, with given b_rank.\n
        Parameters:
            c: String, required
            b_rank: Int, required
        """
        return self._first_column[c][0] + b_rank

    def _left_mapping(self, bwt_index):
        """
        Returns an index (Int) of character at bwt_index in the BWT from the first column.\n
        Parameters:
            bwt_index: Int, required
        """
        c = self._bwt[bwt_index]
        b_rank = self._get_b_rank(bwt_index)
        return self._get_first_column_index(c, b_rank)

    def _find_predecessors_in_range(self, c, range):
        pass

    def find_pattern(self, pattern):
        """
        Returns a number (Int) of occurances of the patern in the original sequence. Return None if pattern is None
        or the last character in a pattern does not exist in counts_per_char or is equal to '$'. Start from the last character.
        For each character search for the new range of predecessor occurances,
        considering the range of occurances of current character.\n
        Parameters:
            pattern: String, required
        """
        if not pattern:
            return None
        if pattern[-1] not in self._counts_per_char or pattern[-1] == '$':
            return None
        start, end = self._first_column[pattern[-1]]
        current_range = (start, end - 1)
        for c in pattern[-2::-1]:
            current_range = self._find_predecessors_in_range(c, current_range[0], current_range[1])
            if current_range == None:
                return None
        return current_range[1]-current_range[0]+1