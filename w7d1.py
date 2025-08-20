
# ESERCIZIO BASE
# creiamo una lista_a con delle parole di cui calcolare la lunghezza 
lista_a = ["ciao","sceicco","lavoratore","bartolini"]

# creiamo una lista_b vuota, alla quale aggiungieremo la lunghezza delle parole in lista_a
lista_b = []

# creiamo un ciclo for in cui diciamo che per ogni parola dentro la lista_a venga aggiunta la lunghezza della parola nella lista_b
for parola in lista_a:
   lista_b.append(len(parola))

# stampiamo la lista_b
print(lista_b)




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ESERCIZIO FACOLTATIVO

# importiamo le librerie per generare lettere/numeri casuali e per i caratteri ascii
import random
import string

# creiamo due variabili con solo caratteri alfanumerici e una con alfanumerici e ascii assieme
alfanumerici = string.ascii_letters + string.digits
tutti_ascii = alfanumerici + string.punctuation

# definiamo una funzione per la generazione delle password che preveda una lunghezza di tipo intero e il charset di tipo stringa e che restituisca una stringa
# creiamo la lista password e facciamo in modo con un ciclo for che la libreria random scelga una lettera casuale e la inserisca nella lista [password]
# usiamo poi la funzione join per levare le virgole dalla lista e farla diventare un unico blocco di testo
def generate_password(lenght:int, charset:str) -> str:
    password = []
    for i in range(0, lenght):
        letter = random.choice(charset)
        password.append(letter)

    return ''.join(password)

# facciamo scegliere all'utente se vuole una password semplice o complessa, se complessa generera' 20 caratteri presi dalla variabile 'tutti_ascii'
# nel caso scegliesse semplice generiamo una password con 8 caratteri alfanumerici
scelta = input("complessa o semplice? C/S: ")
if scelta.lower() == "c":
    password = generate_password(20, tutti_ascii)

elif scelta.lower() == "s":
    password = generate_password(8, alfanumerici)

else:
    print("Riprova, sarai piu' fortunato!")

# stampiamo il risultato
print(password)




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ESERCIZIO SUPER FACOLTATIVO PER ECCEDENZA DI TEMPO E CURIOSITA' PERSONALE:
# Creare un mini-server che accetta connessioni sulla porta 8888 e riceve delle parole.
# il miniserver risponde con la lunghezza della parola ricevuta.


# importiamo socket per creare il mini-server, uso 'as so' per non dover riscirivere completamente 'socket'
import socket as so

# impostiamo il server address e la porta dalla quale poterci connettere
SRV_ADDR = '127.0.0.1'
SRV_PORT = 8888

# impostiamo la rete su un ipv4 con 'af_inet' e metodo di trasmissione dati come TCP grazie al comando 'sock_stream'
# diciamo che il nostro address e la porta che abbiamo scelto prima sono l'indirizzo ipv4 e la porta tcp per la connessione
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))

# mettiamo il mini server in attesa di connessione
s.listen(1)

# ora creiamo un ciclo while che permetta la connessione grazie a 's.accept' e che ci restituisca "client connesso e l'ip del client"
# facciamo in modo che la connesssione riceva 1024 byte e che decodifichi quello che riceve restituendo cio' che viene scritto
# facciamo in modo che risponda con una stringa dove scrive la lungezza della parola che viene scritta
while True:
    connection, address = s.accept()
    print("client connesso", address)

    data = connection.recv(1024)
    word = data.decode()
    print("parola ricevuta:", word)

    response = str(len(word))
    connection.sendall(response.encode())

    connection.close()