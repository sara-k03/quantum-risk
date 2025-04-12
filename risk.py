from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  
import numpy as np

# TWO PLAYER RISK
# Each player starts with 5 troops in each territory 

def rng( lower, upper ):
    numValues = upper - lower + 1
    numQubits = int( np.ceil( np.log2( numValues ) ) )

    # Ensure at least 1 qubit
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

# Quantum Dice
def quantum_dice():
    return rng( 1, 6 )

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


# SO FAR:
# - Quantum Dice 
# - Random territory assignment

# Game Loop
def play_risk():
    print("⚔️ Welcome to Quantum Risk! ⚔️")
    
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
    

play_risk()