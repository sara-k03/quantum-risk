from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  
import numpy as np
from GUI.GameWindow import launch_gui

# SIMPLIFIED, TWO-PLAYER QUANTUM RISK
# Each player starts with 5 troops in each territory 

def rng( lower, upper ):
    numValues = upper - lower + 1
    numQubits = int( np.ceil( np.log2( numValues ) ) )

    # Ensure at least 1 qubit - this was added because of the random territory assignment
    numQubits = max(numQubits, 1)

    # create quantum circuit 
    qc = QuantumCircuit( numQubits )
    
    # apply hadamard gates
    for i in range( numQubits ):
        qc.h(i)

    # measure all qubits 
    qc.measure_all()
    
    # Aer simulator 
    backend = AerSimulator()

    # Run simulator with multiple shots 
    result = backend.run( qc, shots = 1 ).result()
    counts = result.get_counts()
    counts_iterator = iter( counts.items() )

    # Extract the first key-value pair from the iterator
    measured_bin = int(next(counts_iterator)[0], 2) 
    measured_int = lower + ( measured_bin % ( upper - lower + 1 ) )
    
    return measured_int 

# Quantum dice
def quantum_dice_no_tie():
    while True:
        attacker_roll = rng(1, 6)
        defender_roll = rng(1, 6)

        if attacker_roll != defender_roll:
            return attacker_roll, defender_roll
        
def attack_phase(player):
    enemy = [p for p in players if p != player][0]

    print("\nChoose a territory to ATTACK FROM:")
    valid_attack_from = [terr for terr in player_territories[player] if territories[terr]['troops'] > 1]
    
    if not valid_attack_from:
        print("No available territories to attack from.")
        return
    
    for i, terr in enumerate(valid_attack_from):
        print(f"{i}: {terr} (Troops: {territories[terr]['troops']})")
    
    idx_from = int(input("Enter number: "))
    attacking_territory = valid_attack_from[idx_from]

    print("\nChoose a territory to ATTACK:")
    valid_targets = [terr for terr in player_territories[enemy]]
    for i, terr in enumerate(valid_targets):
        print(f"{i}: {terr} (Troops: {territories[terr]['troops']})")
    
    idx_to = int(input("Enter number: "))
    defending_territory = valid_targets[idx_to]

    # Use tie-proof quantum dice
    attacker_roll, defender_roll = quantum_dice_no_tie()

    print(f"\n🎲 Quantum Dice Results:")
    print(f"{player} rolled: {attacker_roll}")
    print(f"{enemy} rolled: {defender_roll}")

    if attacker_roll > defender_roll:
        territories[defending_territory]["troops"] -= 1
        print(f"{enemy} loses 1 troop in {defending_territory}.")
    else:  # No tie possible, so this covers defender_roll > attacker_roll
        territories[attacking_territory]["troops"] -= 1
        print(f"{player} loses 1 troop in {attacking_territory}.")

    # Check if defender has no troops left
    if territories[defending_territory]["troops"] <= 0:
        print(f"{enemy} lost {defending_territory}! {player} captures it.")
        territories[defending_territory]["owner"] = player
        territories[defending_territory]["troops"] = 1  # Leave 1 troop behind
        territories[attacking_territory]["troops"] -= 1  # Move one troop in

        player_territories[player].append(defending_territory)
        player_territories[enemy].remove(defending_territory)

# Players list
players = ["PLAYER A", "PLAYER B"]

territories = {
    "North America": {"owner": None, "troops": 0},
    "Europe": {"owner": None, "troops": 0},
    "Asia": {"owner": None, "troops": 0},
    "South America": {"owner": None, "troops": 0},
    "Australia": {"owner": None, "troops": 0},
    "Africa": {"owner": None, "troops": 0}
}

player_territories = {player: [] for player in players}
player_troops = {player: 0 for player in players}

# Assign territories in superposition
# Quantum territory assignment
available_territories = list(territories.keys())

# Assign 3 territories to each player using quantum randomness
for player in players: 
    for i in range(3):
        # Quantum selection of territory
        idx = rng(0, len(available_territories) - 1)
        selected_terr = available_territories[ idx ]
        available_territories.remove(selected_terr)
                
        territories[selected_terr]["owner"] = player
        territories[selected_terr]["troops"] = 5  # Start with 5 troops
        player_territories[player].append(selected_terr)
        player_troops[player] += 5

# Checks if someone has won
def check_winner():
    for player in players:
        total_troops = sum(territories[terr]['troops'] for terr in player_territories[player])
        if total_troops == 0:
            winner = [p for p in players if p != player][0]
            return winner
    return None

# Game Loop
def play_risk():
    print("⚔️ Welcome to Quantum Risk! ⚔️")

    round_tracker = 0

    while ( True ):
        round_tracker += 1
        print(f"\nROUND {round_tracker}")

        for player in players:
            print(f"\n{player}'s TURN: ")
            
            # display territories
            print("\nEveryone's Territories:")
            for terr, data in territories.items():
                print(f"- {terr}: {data['owner']} (Troops: {data['troops']})")
            
            # display this player's territories
            print("\nYour Territories:")
            for terr in player_territories[player]:
                print(f"- {terr} (Troops: {territories[terr]['troops']})")

            while True:
                choice = input("Press enter to attack, or type 'x' to open GUI: ")
                if choice == "":
                    break
                if choice.lower() == 'x':
                    launch_gui(player_territories, territories)
                else:
                    print("Invalid input.")

            # Attack sequence
            attack_phase(player)
        
        # A player wins when the other player has lost all their troops
        winner = check_winner() 
        if winner:
            print(f"\n🏆 {winner} WINS THE GAME! 🏆")
            return
        
        to_continue = input("Do you want to continue? y/n: ")
        if ( to_continue == "n" ):
            return
    

play_risk()