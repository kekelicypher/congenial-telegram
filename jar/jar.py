class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{self.size * "🍪"}"

    def deposit(self, n):
        if (self._size + n) > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar1 = Jar(10)
    jar1.deposit(5)
    print(jar1.size)
    print(jar1.capacity)
    print(jar1)


if __name__ == "__main__":
    main()
