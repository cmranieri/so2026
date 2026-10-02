import threading


class Monitor:
    """Estrutura básica de um monitor; adapte ao problema proposto."""

    def __init__(self):
        self.lock = threading.Lock()
        self.condicao = threading.Condition(self.lock)

    def operacao(self):
        with self.lock:
            raise NotImplementedError("Implemente a operação do monitor.")
