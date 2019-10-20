class SortClass:
    def __init__(self, *argv):
        self.algo_language = {"C": None, "Java": None, "Python": None}
        self.input = list(argv)

    def show_sort_arr(self):
        raise Exception("show_sort_arr is not implemented in SortClass")

    def sort_arr_object(self):
        raise Exception("sort_arr_object is not implemented in SortClass")

    def show_complexity(self):
        raise Exception("show_complexity is not implemented in SortClass")

    def ceate_algo(self):
        raise Exception("create_algo is not implemented in SortClass")

    def switcher_algo_language(self):
        raise Exception("switcher_algo_language is not implemented in SortClass")
