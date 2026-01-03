import datetime
import random

class Transaction:
    """
    Represents a single transaction.
    """
    def __init__(self, transaction_id, user_id, amount, transaction_type="DEBIT"):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.transaction_type = transaction_type  # DEBIT or CREDIT
        self.timestamp = datetime.datetime.now()
        self.status = "PENDING"  # PENDING, COMPLETED, FAILED

    def validate(self):
        if self.amount <= 0:
            return False
        if self.transaction_type not in ["DEBIT", "CREDIT"]:
            return False
        return True

    def complete(self):
        self.status = "COMPLETED"

    def fail(self):
        self.status = "FAILED"

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "type": self.transaction_type,
            "timestamp": self.timestamp.isoformat(),
            "status": self.status
        }

class TransactionManager:
    """
    Handles multiple transactions and provides reporting features.
    """
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        if transaction.validate():
            self.transactions.append(transaction)
            return True
        else:
            transaction.fail()
            self.transactions.append(transaction)
            return False

    def process_all(self):
        for txn in self.transactions
