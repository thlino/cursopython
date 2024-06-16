
#criar uma lista e troca opçao maça por morango e adicionar um item no final da lista


frutas = [ 'banana', 'maça', 'uva','manga' ]

print(frutas)

### essa forma conseguimos troca o item da lista usando idex 

frutas[1] = ('morango')
print(frutas)

### usar os metodos que ja existem no python 

frutas.append('abacate')
print(frutas)
##  esse metodo insira um idex e objeto na lista 
frutas.insert( 4, 'laranja')
print(frutas)