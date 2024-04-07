times=('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico',
       'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
       'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense',
       'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('='*150)
print('Lista de Times do Barsileirão 2019: {}'.format(times))
print('='*150)
print('Os primeiro 5 colocados foram: ', times[0:5])
print('='*150)
print('Os 4 Rebaixados foram: ', times[-4:])
print('='*150)
print('A lista de times em ordem alfabética é: {}'. format(sorted(times)))
print('='*150)
print('A Chapecoense terminou em {}º Colocado.'.format(times.index('Chapecoense')))
print('='*150)