"""
blockchain.py
-------------
Core logic module for Project 1: Building a Mini-Blockchain
"""

import hashlib
import time
import json


def sha256(raw_string: str) -> str:
    return hashlib.sha256(raw_string.encode("utf-8")).hexdigest()


class Block:
    def __init__(self, index: int, data: dict, prev_hash: str, difficulty: int = 4):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self._mine()

    def _compute_hash(self) -> str:
        block_content = (
            str(self.index)
            + str(self.timestamp)
            + json.dumps(self.data, sort_keys=True)
            + self.prev_hash
            + str(self.nonce)
        )
        return sha256(block_content)

    def _mine(self) -> str:
        target = "0" * self.difficulty

        while True:
            candidate = self._compute_hash()

            if candidate.startswith(target):
                print(
                    f"Block {self.index} mined"
                    f" | Nonce: {self.nonce}"
                    f" | Hash: {candidate[:20]}..."
                )
                return candidate

            self.nonce += 1

    def __repr__(self):
        return (
            f"\n--- Block {self.index} ---\n"
            f"Timestamp : {self.timestamp}\n"
            f"Data      : {self.data}\n"
            f"Prev Hash : {self.prev_hash[:20]}...\n"
            f"Nonce     : {self.nonce}\n"
            f"Hash      : {self.hash[:20]}...\n"
        )


class Blockchain:
    def __init__(self, difficulty: int = 4):
        self.difficulty = difficulty
        self.chain = []
        print("=== Initializing Blockchain ===\n")
        self._create_genesis_block()

    def _create_genesis_block(self):
        print("Mining Genesis Block...")
        genesis = Block(
            index=0,
            data={"sender": "GENESIS", "receiver": "GENESIS", "amount": 0},
            prev_hash="0",
            difficulty=self.difficulty,
        )
        self.chain.append(genesis)

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: dict) -> Block:
        new_block = Block(
            index=len(self.chain),
            data=data,
            prev_hash=self.get_last_block().hash,
            difficulty=self.difficulty,
        )
        self.chain.append(new_block)
        return new_block

    def validate_chain(self) -> bool:
        print("\n=== Running Chain Validation ===\n")

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current._compute_hash():
                print(f"[COMPROMISED] Block {i}: data was tampered with.")
                return False

            if current.prev_hash != previous.hash:
                print(f"[COMPROMISED] Block {i}: chain link is broken.")
                return False

        print("[VALID] All blocks pass validation.\n")
        return True

    def display_chain(self):
        print("\n=== Chain State ===")
        for block in self.chain:
            print(block)