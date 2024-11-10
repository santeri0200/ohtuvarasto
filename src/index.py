from varasto import Varasto


# pylint: disable=too-many-statements
def main():
    piimaa = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Piimävarasto: {piimaa}")
    print(f"Olutvarasto: {olutta}")

    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print("Piimä setterit:")
    print("Lisätään 50.7")
    piimaa.lisaa_varastoon(50.7)
    print(f"Piimävarasto: {piimaa}")
    print("Otetaan 3.14")
    piimaa.ota_varastosta(3.14)
    print(f"Piimävarasto: {piimaa}")

    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Piimävarasto: {piimaa}")
    print("piimaa.lisaa_varastoon(-666.0)")
    piimaa.lisaa_varastoon(-666.0)
    print(f"Piimävarasto: {piimaa}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Piimävarasto: {piimaa}")
    print("piimaa.otaVarastosta(-32.9)")
    saatiin = piimaa.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Piimävarasto: {piimaa}")


if __name__ == "__main__":
    main()
