from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  
import numpy as np

# FOUR PLAYER RISK

def rng( lower, upper ):
    numValues = upper - lower + 1
    numQubits = int( np.ceil( np.log2( numValues ) ) )

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

    if measured_int < numValues:
        quantum_dice()
    
    return measured_int 

# Quantum Dice
def quantum_dice():
    return rng( 1, 6 )
    

# Assigns territory randomly  
def measure_territory():
    measured_int = rng( 1, 4 )
    players = ["Player A", "Player B", "Player C", "Player D"]
    return players[ measured_int - 1 ]

# Setting up territories
players = ["Player A", "Player B", "Player C", "Player D"]
territories = {
    "North America": None,
    "Europe": None,
    "Asia": None,
    "South America": None,
    "Australia": None,
    "Africa": None
}

# Assign territories in superposition
for territory in territories:
    territories[ territory ] = measure_territory()

# SO FAR:
# - Quantum Dice 
# - Random territory assignment

# Game Loop
def play_risk():
    print("⚔️ Welcome to Quantum Risk! ⚔️")
    print("Territories:")
    for terr, owner in territories.items():
        print(f"- {terr}: {owner}")

play_risk()