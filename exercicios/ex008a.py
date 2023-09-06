v = float(input('Digite uma medida em metros: '))
print('{} metros é igual a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(v, (v/1000), (v/100), (v/10), (v*10), (v*100), (v*1000)))
