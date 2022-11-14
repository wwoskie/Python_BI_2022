def output_name_maker(output_file_prefix): # makes names both for failed and passed reads files
    output_passed_file = f'{output_file_prefix}_passed.fastq'
    output_failed_file = f'{output_file_prefix}_failed.fastq'
    return output_passed_file, output_failed_file

def fastq_writer(output_passed_file, output_failed_file, output, save_filtered, is_filtered):#writes reads to two different files by condition
    if not is_filtered:
        with open(output_passed_file, 'a') as output_passed_file:
            output_passed_file.write(output)
    elif save_filtered and is_filtered:
        with open(output_failed_file, 'a') as output_failed_file:
            output_failed_file.write(output)

def bounds_maker(bounds): # creates bounds if numeric (not list or tuple is passed)
    if type(bounds) == int or type(bounds) == float:
        return [0, bounds]
    else:
        return bounds

def gc_content(seq): # retuns GC content of a a given seq
    return (seq.upper().count('G') + seq.upper().count('C')) / len(seq) * 100

<<<<<<< HEAD
def bounds_checker(val_to_check, bounds): # checks if value (length and GC content here, but can be possibly reused) is in range
=======
def bounds_checker(val_to_check, bounds):#checks if value (length and GC content here, but can be possibly reused) is in range
>>>>>>> 1544a8eb4e27156f7aeb8adef926218ecf1e54de
    return bounds[0] <= val_to_check <= bounds[1]

def quality_estimator(quality): # translates ASII symbols to q_score
    q_score_lst = []
    for q in list(quality):
        q_score = ord(q) - 33
        q_score_lst.append(q_score)
    mean_q = sum(q_score_lst) / len(q_score_lst)
    return mean_q

def quality_checker(mean_q, quality_threshold): # checks if quality is in range
    if mean_q >= quality_threshold:
        return True
    else:
        return False

def main(input_fastq, # main body function
         output_file_prefix, 
         gc_bounds = [0, 100], 
         length_bounds = [0, 2**32], 
         quality_threshold = 0, 
         save_filtered = False):
    
    gc_bounds = bounds_maker(gc_bounds) # checks and converts borders into a range if nesessary 
    length_bounds = bounds_maker(length_bounds)
    
    with open(input_fastq) as input_file:
        current_read = [input_file.readline().strip() for _ in range(4)]

        if len(current_read) == 4: # starts operating with read when it's fully parced
            seq = current_read[1].strip() # save seq and quality as we are going to operate with them later, strip is important here!
            quality = current_read[3].strip()

            is_filtered = not(bounds_checker(gc_content(seq), gc_bounds) and # condition to define whether read will be filtered or not
                              bounds_checker(len(seq), length_bounds) and 
                              quality_checker(quality_estimator(quality), quality_threshold))

            output_passed_file, output_failed_file = output_name_maker(output_file_prefix) # define names for output files
            fastq_writer(output_passed_file, output_failed_file, ''.join(current_read), save_filtered, is_filtered) # call fastq_writer

            current_read = [] # making empty list for next read

# main('test_data/test.fastq', 'test_data/test_file', save_filtered=True, gc_bounds=62.67, length_bounds=[0, 35])