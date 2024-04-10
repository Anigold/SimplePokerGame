from ..backend.Components.Components import Card

class ANSITerminal:

    def __init__(self) -> None:
        self.COLORS = {
            "HEADER": "\033[95m",
            "BLUE": "\033[94m",
            "GREEN": "\033[92m",
            "RED": "\033[91m",
            "ENDC": "\033[0m",
        }

    def color_text(self, text: str, color: str) -> str:
        return f'{self.COLORS[color]}{text}{self.COLORS['ENDC']}'
    
    def get_card_string(self, card: Card) -> None:
        return 
