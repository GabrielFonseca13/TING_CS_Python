def exists_word(word, instance):
    result = list()

    for i in range(len(instance)):
        file_data = instance.search(i)
        lines_with_word = {
            "palavra": word,
            "arquivo": file_data["nome_do_arquivo"],
            "ocorrencias": list(),
        }

        for line, content in enumerate(file_data["linhas_do_arquivo"]):
            if word.lower() in content.lower():
                lines_with_word["ocorrencias"].append({"linha": line + 1})

        if len(lines_with_word["ocorrencias"]) > 0:
            result.append(lines_with_word)

    return result


def search_by_word(word, instance):
    result = list()

    for i in range(0, len(instance)):
        file_data = instance.search(i)

        file_data = instance.search(i)
        lines_with_word = {
            "palavra": word,
            "arquivo": file_data["nome_do_arquivo"],
            "ocorrencias": list(),
        }

        for line, content in enumerate(file_data["linhas_do_arquivo"]):
            if word.lower() in content.lower():
                lines_with_word["ocorrencias"].append(
                    {"linha": line + 1, "conteudo": content}
                )

        if len(lines_with_word["ocorrencias"]) > 0:
            result.append(lines_with_word)

    return result
