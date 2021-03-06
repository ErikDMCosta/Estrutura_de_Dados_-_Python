from node import Node

# Inserir na Fila -> PUSH
# Remover na Fila -> POP
# Observar a Fila -> PEEK

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        # Insere um elemento na fila
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):
        # Remove um elemento na fila
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")

    def peek(self):
        # Retorna um elemento na fila
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while pointer:
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()
