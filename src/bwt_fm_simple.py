import bwt_fm_interface as bfi


class BwtFmSimple(bfi.BwtFmInterface):
    def __init__(self, text, suffix_array_file=None, bwt_file=None):
        """
        Constructor for BwtFmSimple.
        Parse suffix array and BWT from files. If those files are None, build BWT and suffix array.
        Count the number of each char and build first column. Build b_rank.\n
        Parameters:
            text: String, required
            suffix_array_file: String, default = None
            bwt_file: String, default = None
        """
        super().__init__(text, suffix_array_file=suffix_array_file, bwt_file=bwt_file)

        self._b_rank = self._build_b_rank()

    def _build_suffix_array(self):
        """
        Parse suffix array from suffix_array_file. If suffix_array_file is None, build suffix array.
        """
        if self._suffix_array_file == None:
            suffix_matrix = sorted([(self._text[i:], i) for i in range(len(self._text))])
            return list(map(lambda suffix_index: suffix_index[1], suffix_matrix))
        else:
            with open(self._suffix_array_file, "r") as file:
                return[int(x) for x in file.read().split(' ')]
                
    def _build_b_rank(self):
        """
        Returns b-rank for all the characters at BWT.
        """
        counts = dict()
        ranks = []
        for c in self._bwt:
            if (c not in counts):
                counts[c] = 0
            ranks.append(counts[c])
            counts[c] += 1
        return ranks

    def _get_b_rank(self, bwt_index):
        """
        Returns b-rank for a character at bwt_index at BWT.
        """
        return self._b_rank[bwt_index]

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
        first = last = None
        for i in range(start, end+1):
            if self._bwt[i] == c:
                first = i
                break
        if first == None:
            return None
        for i in range(end, start-1, -1):
            if self._bwt[i] == c:
                last = i
                break
        if last == None:
            return None
        return (self._left_mapping(first), self._left_mapping(last))
