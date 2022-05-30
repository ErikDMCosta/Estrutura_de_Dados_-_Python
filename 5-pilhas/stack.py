from node import Node

# Inserir na Pilha -> PUSH
# Remover na Pilha -> POP
# Observar o Topo da Pilha -> PEEK

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        # Insere um elemento no topo da pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # Remove um elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        # Retorna o topo da pilha sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
