import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content = txt_importer(path_file)
    dict_content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }

    for i in range(len(instance)):
        data = instance.search(i)
        if data == dict_content:
            return

    instance.enqueue(dict_content)
    print(dict_content, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)
    file = instance.dequeue()
    removed_file = file["nome_do_arquivo"]
    print(f"Arquivo {removed_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
