from requests import get, post

count = 0

try:
    url = input('URL/Domínio a ser testado: ')
    url = url if url.startswith(('http://', 'https://')) else 'http://'+url
    
    option = int(input('Digite:\n\t0: Usar método GET (padrão)\n\t1: Usar método POST'))
    option = option if option in (0, 1) else 0

    while (True):
        if option == 0:
            req = get(url)
        elif option == 1:
            req = post(url)
        print('Pressione CTRL+C para cancelar')
        print('Requisição #: ' + str(count))
        print('Status: ' + str(req.status_code))
        print('Demonstração do body retornado: ' + str(req.text[0:50]))
        count+=1
except KeyboardInterrupt:
    print('Saindo')
    exit(0)
except ValueError:
    print('Digite valores dos tipos esperados')
    exit(1)
except Exception as e:
    print('Erro: '+str(e))
    exit(1)
