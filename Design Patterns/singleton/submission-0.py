class Singleton:
    _instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            cls._instance.val = None

        return cls._instance


    def getValue(self) -> str:
        return self.val

    def setValue(self, value: str):
        self.val = value
