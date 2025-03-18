max_term_val = 10000

def fibonacci():
    curr_val = 0
    next_val = 1
    while curr_val <= max_term_val:
        print(curr_val)
        next_term_val = curr_val + next_val
        curr_val = next_val
        next_val = next_term_val


fibonacci()