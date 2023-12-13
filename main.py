from global_alignment import global_alignment as ga
from global_alignment_aminoacid import global_alignment_aminoacids as gaa
from fasta_reader import read_fasta 

RNA_AlPHABET = {
    'A', 'U', 'G', 'C'
}

DNA_AlPHABET = {
    'A', 'T', 'G', 'C'
}

AMINOACID_ALPHABET = {
    "A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"
}

def is_rna(sequence:str) -> bool:
    '''
    Проверка на РНК. Функция возвращает
    булевое значение.
    '''
    seq = set([item for item in sequence])
    return seq <= RNA_AlPHABET

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
    - seq_1 (str): первая последовательность (ДНК/РНК/аминокислоты) 
    - seq_2 (str): вторая последовательность (ДНК/РНК/аминокислоты) 

    Return:
    tuple: две выравненные последовательности

    Пример использования:
    ATCCCCCTGC      ATCCC--CCTGC
                ->  
    ATCCCGGCCT      ATCCCGGCCT--
    '''
    if is_dna(seq_1) and is_dna(seq_2) or is_rna(seq_1) and is_rna(seq_2):
        aligned_seq_1, aligned_seq_2 = ga(seq_1, seq_2)[0], ga(seq_1, seq_2)[1]
    elif is_protein(seq_1) and is_protein(seq_2):
        aligned_seq_1, aligned_seq_2 = gaa(seq_1, seq_2)[0], gaa(seq_1, seq_2)[1]
    else:
        raise ValueError('Incorrect input sequencies!')
    
    return aligned_seq_1, aligned_seq_2


s1 = read_fasta('1.fasta')
s2 = read_fasta('2.fasta')

aligned_s1, aligned_s2 = alignment(s1, s2)[0], alignment(s1, s2)[1]

print(aligned_s1)
print(aligned_s2)
