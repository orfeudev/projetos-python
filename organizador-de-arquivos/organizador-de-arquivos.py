import os
from tkinter.filedialog import askdirectory


diretorio = askdirectory(title='Selecione uma pasta')

# Lista todos os arquivos presentes no diretório
lista_arquivos = os.listdir(diretorio)

# usa um dicionário para definir as categorias
locais = {
    "imagens": [".png", ".jpeg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "mp4": [".mp4"],
    "instaladores": ['.exe'],
    "arquivos python": ['.py','.ipynb'],
    "arquivos zipados": ['.zip']
}


for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(arquivo)  
    for pasta in locais:
        if extensao in locais[pasta]:  
            caminho_pasta = os.path.join(diretorio, pasta) 
            if not os.path.exists(caminho_pasta):  
                os.mkdir(caminho_pasta)  # Cria a pasta se ela não existir
            
            # realoca o arquivo para a pasta
            os.rename(os.path.join(diretorio, arquivo), os.path.join(caminho_pasta, arquivo))
