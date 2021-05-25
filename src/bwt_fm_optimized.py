import bwt_fm_interface as bfi


class BwtFmOptimized(bfi.BwtFmInterface):
    def __init__(self, text, suffix_array_factor, tally_factor, suffix_array_file, bwt_file=None):
        """
        Constructor for BwtFmOptimized.
        Parse suffix array and BWT from files. If those files are None, build BWT and suffix array.
        Count the number of each char and build first column.
        Downsamle suffix array with given suffix_array_factor. Build tally matrix with given tally_factor.\n
        Parameters:
            text: String, required
            suffix_array_factor: Int, required
            tally_factor: Int, required
            suffix_array_file: String, default = None
            bwt_file: String, default = None
        """
        super().__init__(text, suffix_array_factor, tally_factor, suffix_array_file, bwt_file)

        self._tally = self._build_tally()

    def _build_suffix_array(self):
        """
        Build suffix array with given suffix_array_factor.
        """
        with open(self._suffix_array_file, "r") as file:
            return [int(position) for index, position in enumerate(file.read().split(' ')) if index % self._suffix_array_factor == 0]

    def _build_tally(self):
        """
        Builds tally matrix with given tally_factor. Count b-rank of each character.
        Returns a 2D array of every i-th b-rank for each character, where i represents tally factor.
        """
        current_count = dict()
        tally = dict()
        for c in self._counts_per_char:
            if c != '$':
                current_count[c] = 0
                tally[c] = []
        for i, c in enumerate(self._bwt):
            if c != '$':
                current_count[c] += 1
            if i % self._tally_factor == 0:
                for c in current_count:
                    tally[c].append(current_count[c])
        return tally

    def _get_b_rank(self, bwt_index):
        """
        Returns b-rank for a character at bwt_index at BWT.
        """
        c = self._bwt[bwt_index]
        if c == '$':
            return 0
        return self._get_tally_rank(c, bwt_index) - 1

    def _get_tally_rank(self, c, bwt_index):
        """
        Returns tally rank for a character at bwt_index at BWT, for a range defined by tally_factor.
        """
        tally_index = bwt_index // self._tally_factor
        c_count = self._tally[c][tally_index]
        current_index = tally_index * self._tally_factor + 1
        while (current_index <= bwt_index):
            if self._bwt[current_index] == c:
                c_count += 1
            current_index += 1
        return c_count

    def _find_predecessors_in_range(self, c, start, end):
        """
        Find character c in a range (start, end).\n
        Parameters:
            c: String, required
            start: Int, required
            end: Int, required
        """
        if c == '$' or c not in self._counts_per_char:
            return None
        start_tally = self._get_tally_rank(c, start - 1) if start != 0 else 0
        end_tally = self._get_tally_rank(c, end)
        c_count = end_tally - start_tally
        if c_count == 0:
            return None
        else:
            first_b_rank = start_tally
            last_b_rank = end_tally - 1
            return (self._get_first_column_index(c, first_b_rank), self._get_first_column_index(c, last_b_rank))
