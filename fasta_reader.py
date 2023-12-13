import os

def read_fasta(file_name:str) -> str:
    '''
    Функция читает fasta формат файлов 
    и выводит последовательность днк/рнк или 
    аминокислот.

    Аргументы:
    - file_name (str): имя fasta файла 
    '''
    with open(os.path.join(os.getcwd(), file_name), mode='r') as fasta:
        lines = fasta.readlines()
        for line in lines:
            if not line.startswith('>'):
                return line.strip('\n')

    


