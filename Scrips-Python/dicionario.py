Pessoa = {'Nome': 'Frederico', 'Profissao': 'Técnico em Informárica', 'Idade': 41}
print(Pessoa['Nome'])
Pessoa['Profissao'] = 'Analista de sistemas'
print(Pessoa['Profissao'])


class Pessoa:
    pass

Objeto = Pessoa()
Objeto.nome = 'Frederico'
Objeto.emprego = 'Tecnico'
Objeto.idade = 41

print(Objeto.__dict__)
