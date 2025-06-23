class Cores:
    """
    Paleta de cores da interface do aplicativo.

    Centraliza as definições de cores usadas na interface, facilitando a manutenção
    e garantindo consistência visual no projeto.
    """

    # Paleta principal (tons de verde)
    VERDE_ESCURO      = "#2e7d32"
    VERDE_MEDIO       = "#43a047"
    VERDE_CLARO       = "#d4f5d0"
    VERDE_PLACEHOLDER = "#6fa36f"
    BORDAS_INPUT      = "#a5d6a7"

    # Cores auxiliares
    AZUL         = "#333ecc"
    VERMELHO     = "#bd0000"
    BRANCO       = "#ffffff"
    CINZA_TEXTO  = "#4f4f4f"
    CINZA_SOMBRA = "#929292"

    @staticmethod
    def rgb(hex_str: str) -> tuple:
        """
        Converte uma cor em hexadecimal para o formato RGB.

        Args:
            hex_str (str): Cor no formato hexadecimal (ex: "#ffffff").

        Returns:
            tuple[int, int, int]: Tupla com os valores RGB correspondentes.
        """
        hex_str = hex_str.lstrip("#")
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
