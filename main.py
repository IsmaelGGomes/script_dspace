import os
import re

def exclude_items(diretorio, handle_count):
    # prefixo handle que inicia 
    handle_modified = f"123456789/{handle_count}"
    
    with open(diretorio, 'w', encoding='utf-8') as f:
        f.write(handle_modified)

def index(diretorio_base):
    """ print("Ex: E:/caminho/collection")
    diretorio_base = input("Insira o endereco da Collection: ")
    aa = 'E:/Dspace/todas_colections/collection_113' """
    qtd_pastas = contar_pastas(diretorio_base)
    
    handle_count = int(input("\nInicio contagem Handle: "))
    collection = input("\nCollection destino: ")
    
    for item in range(qtd_pastas):
        item += 1
        handle_count += 1
        diretoriofinal = f"{diretorio_base}/{item}"
        print(f"Handle: {handle_count}")
        diretorio_handle = diretoriofinal + "/handle"
        diretorio_collection = diretoriofinal + "/collections"
        exclude_items(diretorio_handle,handle_count)
        
        arquivo = open(diretorio_collection, 'w')
        arquivo.write(collection)
    else:
        print ("Finalizado")


def substituir_nome_arquivo(caminho_arquivo, nova_string,quantidade_caracteres):

    print(f"Nome arquivo: {nova_string}")
    diretorio_new = caminho_arquivo + "/contents"
    with open(diretorio_new, 'r',encoding='utf-8') as f:
        linhas = f.readlines()

    with open(diretorio_new, 'w',encoding='utf-8') as f:
        for linha in linhas:
            # Encontra todas as ocorrências de nomes de arquivos .pdf na linha
            padrao = rf".{{{quantidade_caracteres}}}\.pdf" 
            matches = re.findall(padrao, linha)
            
            for match in matches:
                # Substitui a parte antes do .pdf pelo novo prefixo
                print(f"PDF: {match}")
                nova_linha = linha.replace(match, nova_string)
                f.write(nova_linha)
            else:
                if re.findall("license.txt", linha):
                    f.write(linha)
            
def contar_caracteres_pdf(diretorio):

    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".pdf"):
            nome_arquivo = os.path.basename(arquivo)
            quantidade_caracteres = len(nome_arquivo) - 4
    """ print(f"Qtd: {quantidade_caracteres}") """
    substituir_nome_arquivo(diretorio, nome_arquivo,quantidade_caracteres)

def contar_pastas(caminho_pasta):
    try:
        # Listar os conteúdos da pasta
        conteudos = os.listdir(caminho_pasta)

        # Filtrar apenas os diretórios (pastas)
        pastas = [item for item in conteudos if os.path.isdir(os.path.join(caminho_pasta, item))]

        return len(pastas)
    except FileNotFoundError:
        print(f"A pasta '{caminho_pasta}' não foi encontrada.")
        return 0

def init_main():
    print("Ex: E:/caminho/collection")
    diretorio_pdfs = input("Insira o endereco da Collection: ")
    
    qtd_pastas = contar_pastas(diretorio_pdfs)
    
    for item in range(qtd_pastas):
        item += 1
        print(f"Pasta: {item}")
        diretoriofinal = f"{diretorio_pdfs}/{item}"
        contar_caracteres_pdf(diretoriofinal)
    else:
        index(diretorio_pdfs)


init_main()