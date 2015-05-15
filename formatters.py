def print_wrapped_column(my_str, letters_per_line):
    letter_count = 0
    current_line = ""
    for idx, word in enumerate(my_str.split(' ')):
        letter_count += len(word)
        if letter_count > letters_per_line:
            print current_line
            current_line = ""
            letter_count = len(word)
        current_line = current_line + " %s" % word
        if idx == len(my_str.split(' ')) - 1:
            print current_line.strip()
