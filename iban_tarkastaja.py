from stdnum import iban


def main():
    tilinumero = input("Anna IBAN- tilinumero:")
    onko_oikea_iban = iban.is_valid(tilinumero)
    if onko_oikea_iban:
        print("Antamasi tilinumero '{tilinumero}' on oikea IBAN.")
        muotoiltu = iban.format(tilinumero)
        print(f"Tilinumero muotoiltuna: {muotoiltu}")
    else:
        print(f"Antamasi tilinumero '{tilinumero}' ei ole IBAN.")


if __name__ == '__main__':
    main()
