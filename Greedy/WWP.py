class WWP:
    @staticmethod
    def run_wwp(input_sequence, maximum=6):
        line = ""
        words = input_sequence.split(" ")
        for word in words:
            if len(line + word) < maximum:
                line += "{0} ".format(word)
            elif len(line + word) == maximum:
                line += word
                print(line)
                line = ""
            else:
                print(line)
                line = ""
                line += "{0} ".format(word)
        if len(line) > 0:
            print(line)
            line = ""
