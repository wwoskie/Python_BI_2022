print('''Hi! I'm a python script that can work with a given RNA or DNA sequence. 
For some reason I run in terminal and require manual input. Hope you will have at least some fun playing around with me)))0))0)

Here's what I can do and understand:

exit — завершение исполнения программы
transcribe — напечатать транскрибированную последовательность
reverse — напечатать перевёрнутую последовательность
complement — напечатать комплементарную последовательность
reverse complement — напечатать обратную комплементарную последовательность

At least try to have some fun!
''')

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

def reverse(seq, nucl_type=None):
    print('Reversing...')
    return(seq[::-1])

def transcribe(seq, nucl_type):
    print('Transcribing...')
    while nucl_type != 'DNA':
        print('Your sequence is not DNA. Please, enter a new sequence')
        seq = input('Enter seq: ')
        nucl_type = is_seq_legit(seq)[1]
    return seq.replace('T', 'U').replace('t', 'u')

def complement(seq, nucl_type):
    print('Complementing...')
    print('You look pretty today!')
    seq = list(seq)
    outseq = []
    for letter in seq:
        outseq.append(nucl_comp_dct[nucl_type][letter])
    return ''.join(outseq)


def reverse_complement(seq, nucl_type):
    print('Reverse complementing...')
    print('You look pretty today!'[::-1])
    return reverse(complement(seq, nucl_type), nucl_type)

valid_command_dct = {'transcribe':transcribe, 'reverse':reverse, 
                     'complement':complement, 'reverse complement':reverse_complement}

command = input('Enter command: ')

while command != 'exit':
    if command in valid_command_dct:
        seq = input('Enter seq: ')
        while not is_seq_legit(seq)[0]:
            print('Your sequence has invalid alphabet. Please, enter a new sequence')
            seq = input('Enter seq: ')
        nucl_type = is_seq_legit(seq)[1]
        print(valid_command_dct[command](seq, nucl_type))
    else:
        print('Seems like an invalid command. Please, enter valid command!')

    command = input('Enter command: ')

print('See you next time!')