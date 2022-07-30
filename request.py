class Request:
    def __init__(self, from_: str, to: str, amount: int, product: str):
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.product = product

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
