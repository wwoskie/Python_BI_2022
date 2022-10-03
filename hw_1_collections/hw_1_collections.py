nucl_comp_dct = {'RNA':{'A':'U', 'U':'A', 'G':'C', 'C':'G', 'a':'u', 'u':'a', 'g':'c', 'c':'g'}, 
                 'DNA':{'A':'T', 'T':'A', 'G':'C', 'C':'G', 'a':'t', 't':'a', 'g':'c', 'c':'g'}}

def is_seq_legit(seq):
    if set(seq).issubset(nucl_comp_dct['RNA']) and not set(seq).issubset(nucl_comp_dct['DNA']):
        return True, 'RNA'
    elif not set(seq).issubset(nucl_comp_dct['RNA']) and set(seq).issubset(nucl_comp_dct['DNA']):
        return True, 'DNA'
    elif ('u' in seq.lower() and 't' in seq.lower()) or (not set(seq).issubset(nucl_comp_dct['RNA']) and not set(seq).issubset(nucl_comp_dct['DNA'])):
        return False, 'invalid_alphabet'
    else:
        return True, 'DNA'

def reverse(seq):
    print('Reversing...')
    return(seq[::-1])

def transcribe(seq):
    print('Transcribing...')
    print(is_seq_legit(seq))

def complement(seq):
    print('You look pretty today! UwU')
    print(is_seq_legit(seq))

def reverse_complement(seq):
    print('You look ugly today! -_-')
    print(is_seq_legit(seq))

valid_command_dct = {'transcribe':transcribe, 'reverse':reverse, 
                     'complement':complement, 'reverse complement':reverse_complement}

command = str(input('Enter command: '))

while command != 'exit':
    if command in valid_command_dct:
        seq = str(input('Enter seq: '))
        while not is_seq_legit(seq)[0]:
            print('Your sequence has invalid alphabet. Please, eneter a new sequence')
            seq = str(input('Enter seq: '))
        print(valid_command_dct[command](seq))
    else:
        print('Seems like an invalid command. Please, enter valid command!')

    command = str(input('Enter command: '))

print('See you next time!')
    