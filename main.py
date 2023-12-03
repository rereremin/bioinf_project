from global_alignment import global_alignment_dna as gad
from global_alignment_aminoacid import global_alignment_aminoacids as gaa
from fasta_reader import read_fasta 

DNA_AlPHABET = {
    'A', 'T', 'G', 'C'
}

AMINOACID_ALPHABET = {
    "A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"
}

def is_dna(sequence:str) -> bool:
    '''
    Проверка на ДНК. Функция возвращает
    булевое значение.
    '''
    seq = set([item for item in sequence])
    return seq <= DNA_AlPHABET

def is_protein(sequence:str) -> bool:
    '''
    Проверка на аминокислотную последовательность. 
    Функция возвращает булевое значение.
    '''
    seq = set([item for item in sequence])
    return seq <= AMINOACID_ALPHABET


def alignment(seq_1:str, seq_2:str) -> tuple:
    '''
    Выравнивание осуществляется по алгоритму
    Нидлмана-Вунша как ДНК последовательностей, так и
    аминокислотных с использованием таблицы BLOSUM62.

    Аргументы:
    - seq_1 (str): первая последовательность (ДНК/аминокислоты) 
    - seq_2 (str): вторая последовательность (ДНК/аминокислоты) 

    Return:
    tuple: две выравненные последовательности

    Пример использования:
    ATCCCCCTGC      ATCCC--CCTGC
                ->  
    ATCCCGGCCT      ATCCCGGCCT--
    '''
    if is_dna(seq_1) and is_dna(seq_2):
        aligned_seq_1, aligned_seq_2 = gad(seq_1, seq_2)[0], gad(seq_1, seq_2)[1]
    elif is_protein(seq_1) and is_protein(seq_2):
        aligned_seq_1, aligned_seq_2 = gaa(seq_1, seq_2)[0], gaa(seq_1, seq_2)[1]
    else:
        raise ValueError('Incorrect input sequencies!')
    
    return aligned_seq_1, aligned_seq_2

fasta_name = input()
s1, s2 = read_fasta(fasta_name)[0], read_fasta(fasta_name)[1]

aligned_s1, aligned_s2 = alignment(s1, s2)[0], alignment(s1, s2)[1]
print(aligned_s1)
print(aligned_s2)