# auth logic
import hashlib


class Auth:
    def __init__(self, name, role, password):
        self.name = name
        self.role = role
        self.password = password
