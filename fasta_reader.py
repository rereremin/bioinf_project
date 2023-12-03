import os

def read_fasta(file_name:str) -> list:
    '''
    Функция читает fasta формат файлов 
    и выводит список последовательностей днк или 
    аминокислот.

    Аргументы:
    - file_name (str): имя fasta файла 
    '''
    fasta_seqs = []
    with open(os.path.join('bioinf_project', file_name), mode='r') as fasta:
        lines = fasta.readlines()
        for line in lines:
            if not line.startswith('>'):
                fasta_seqs.append(line.strip('\n'))

    return fasta_seqs



