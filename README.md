# Mini-Blockchain

A ground-up implementation of a cryptographic ledger in Python. No frameworks. No abstractions. Just the raw primitives that every production blockchain is built on.

Built as Project 1 of the DecodeLabs Blockchain Industrial Training Programme, Batch 2026.

---

## What this implements

| Layer | Component | Purpose |
|---|---|---|
| Infrastructure | SHA-256 hashing | Deterministic digital fingerprinting |
| Consensus | Proof of Work mining loop | Computational cost as a Sybil resistance mechanism |
| Data | Cryptographic linked list | Append-only ledger via prev_hash chaining |
| Integrity | Dual-check validation | Detects both data tampering and structural attacks |

---

## Project structure

```
mini-blockchain/
├── blockchain.py   # sha256(), Block, Blockchain
├── main.py         # Execution, mining, validation, attack simulation
├── README.md
└── .gitignore
```

---

## Run it

```bash
python main.py
```

Standard library only. No dependencies.

---

## How the chain integrity works

Every block stores the hash of the block before it. Change anything in any block and two things break simultaneously: the stored hash no longer matches the block's recomputed hash, and the next block's `prev_hash` pointer becomes invalid. Both checks run on every validation pass.

```
Block N-1        Block N          Block N+1
[ data      ]    [ data      ]    [ data      ]
[ prev_hash ]◄───[ prev_hash ]◄───[ prev_hash ]
[ hash ─────]────►            [ hash ─────]────►
```

To rewrite any block an attacker must re-mine that block and every block after it, faster than the honest network extends the chain. This is the computational guarantee that makes the ledger immutable.

---

## Validation output

```
=== Running Chain Validation ===

  [VALID] All blocks pass dual-check. Chain integrity confirmed.

=== Tampering Attack 1: Data Modification ===

  [COMPROMISED] Block 1: data was tampered with.

=== Tampering Attack 2: Hash Patch Attempt ===

  [COMPROMISED] Block 2: chain link is broken.
```

---

## Key design decisions

`sort_keys=True` in `json.dumps()`
Ensures the JSON serialization of transaction data is deterministic across environments. Without this, key ordering varies by Python version and breaks hash reproducibility across nodes.

Nonce initialized at 0, not random
Matches the canonical PoW specification. A random start would produce non-reproducible mining benchmarks and complicate difficulty calibration in testing.

Timestamp captured at instantiation, not at hash time
The timestamp is part of the hash input. Capturing it once at `__init__` ensures the block's identity is fixed before the mining loop begins.

---

## Concepts covered

`SHA-256` `Proof of Work` `Nonce` `Genesis Block` `Hash Chaining` `Avalanche Effect` `Chain Validation` `Tamper Detection` `Immutability`

---

## Author

Sophia — Blockchain Developer in training | Technical Writer
LinkedIn: https://www.linkedin.com/in/sophia-dabaye
 [GitHub](https://github.com/YOURUSERNAME)
