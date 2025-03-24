nome = str(input('Qual seu nome? '))
idade = int(input('Qual sua idade? '))

if (idade<16) 
    voto = 'Nao precisa votar'

elif (idade == 16 | idade > 65) 
    voto = 'Voto não obrigatorio'

else:
    voto = 'Voto obrigatorio'


print(f'De acordo com a sua idade, {nome} voce {voto}.')