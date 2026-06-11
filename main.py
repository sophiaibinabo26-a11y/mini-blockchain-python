"""
main.py
------
Execution milestone for Project 1: Building a Mini-Blockchain
Decodelabs Industrial Training Kit | Batch 2026

Runs:
- Genesis block instantiation
- Mining 3 subsequent blocks
- Clean chain validation
- Tampering attack simulation (basic + advanced)
"""

from blockchain import Blockchain


def run():
    blockchain = Blockchain(difficulty=4)

    print("\n=== Mining 3 Blocks ===\n")
    blockchain.add_block({"sender": "Alice", "receiver": "Bob", "amount": 50})
    blockchain.add_block({"sender": "Bob", "receiver": "Charlie", "amount": 25})
    blockchain.add_block({"sender": "Charlie", "receiver": "Alice", "amount": 10})

    blockchain.display_chain()

    blockchain.validate_chain()

    print("\n=== Tampering Attack 1: Data Modification ===\n")
    print("Attacker changes Block 1: Alice -> Bob becomes Alice -> Eve\n")

    blockchain.chain[1].data = {
        "sender": "Alice",
        "receiver": "Eve",
        "amount": 50
    }

    blockchain.validate_chain()

    print("\n=== Tampering Attack 2: Hash Patch Attempt ===\n")
    print("Attacker recalculates Block 1 hash to cover tracks...\n")

    blockchain.chain[1].hash = blockchain.chain[1]._compute_hash()

    blockchain.validate_chain()

    print("\n=== End of Project 1 ===")


if __name__ == "__main__":
    run()