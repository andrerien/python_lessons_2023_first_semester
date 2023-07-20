contatos = {
    'Marcos': '99999-9999',
    'Maria': '99999-9998',
}

# Adicionando novo elemento

contatos['Pedro'] = '99999-9997'
contatos['Marcos'] = '99999-9996'

contatos.pop('Maria', "Contato não encontrado!")

#try:
    #del contatos['Marcos']
#except:
    #print('Contato não encontrado')

print(contatos.pop('Maria', "Contato não encontrado!"))

#print(contatos)
#print(contatos['Pedro'])
print(contatos.get('Pedra', 'Contato não encontrado!'))

#print("Marcos" in contatos)

for key, value in contatos.items():
    print(key+':', value)