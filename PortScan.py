while True:

    import socket


    ip = input("Digite o IP ou endereço: ")


    input_str = input("Insira as portas separadas por vírgula: ")


    port_str_list = input_str.split(',')


    ports = [int(port) for port in port_str_list]


    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.6)
    
        code = client.connect_ex((ip, port))


        if code == 0:
            print(port ,"\033[32mOPEN\033[0m")
        else:
            print(port ,"\033[91mCLOSE\033[0m")
    print ("Scan finalizado com sucesso")


    while True:
        cont = input("Você deseja fazer outro Scan? [s/n]: ").lower()
        if cont in ["s", "n"]:
            break
        print("Por favor, digite 's' para sim ou 'n' para não.")

    if cont == "n":
        print("Fim do programa!")
        break
    print()


