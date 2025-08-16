import random

#funcion para seleccionar las opciones del juego
def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ').lower()

    if not user_option in options:
      return None, None
    
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    return user_option, computer_option

# Función para validar las reglas
def check_rules(user_option, computer_option, user_wins, computer_wins):
    
    if user_option == computer_option:
        print('Empate!')
        return user_wins, computer_wins
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
            return user_wins, computer_wins
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
            return user_wins, computer_wins
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
            return user_wins, computer_wins
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
            return user_wins, computer_wins
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
            return user_wins, computer_wins
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1
            return user_wins, computer_wins

def run_game():

    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        user_option, computer_option = choose_options()

        if user_option != None :

            user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

            if user_wins == 2 :
                print(f"juego terminado gana el jugador {user_wins} a {computer_wins} contra la computadora")
                break
            elif computer_wins == 2 :
                print(f"juego terminado gana la computadora {computer_wins} a {user_wins} contra el Juagador")
                break
            
            rounds += 1
        else:
            print("Selecciones una opción valida por favor")
            continue



run_game()