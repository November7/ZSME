class T:
    def __init__(self):
        self.value = 42

    def __str__(self):
        return f"T with value {self.value}"
    

if __name__ == "__main__":
    t = T()
    print(f'{t = }')

