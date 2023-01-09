def valida_frase(frase):
    frase_tolkiens=frase.split(" ")
    erros=0

    print(frase_tolkiens)
    tolkiens_validos=0

    for tolkien in frase_tolkiens:
        erros=0
        for caracter in tolkien:
            if caracter in "0123456789_" or caracter.isupper():
                erros+=1
                continue
            if caracter in".!?,":
                if caracter!=tolkien[-1]:
                    erros+=1
                    continue

        if tolkien.count("-")>1 or tolkien[0]=="-" or tolkien[-1]=="-" or erros>0:
            continue
        else:
            tolkiens_validos+=1

    return tolkiens_validos

frase = "!isto quase p0d3 -ha faca-me ha- 55 mamão! -Fim-"
print(valida_frase(frase))


