class Auto:
    def __init__(self, rekisterinumero, merkki, malli):
        self.rekisterinumero = rekisterinumero
        self.merkki = merkki
        self.malli = malli

    def __str__(self) -> str:
        # Merkkijonoja voi yhdistää plus-merkillä
        teksti = "Auto: " + self.merkki + " " + \
            self.malli + " (" + self.rekisterinumero + ")"

        # tai f-stringillä:
        teksti = f"Auto: {self.merkki} {self.malli} ({self.rekisterinumero})"

        return teksti


volkkari = Auto("ABC-123", "Volkswagen", "Golf")
saab = Auto("XYZ-456", "Saab", "En tiiä")
opel = Auto("XXX-123", "Opel", "Astra")


print(volkkari)
print(saab)
print(opel)
