class Guitar:
    @staticmethod
    def play():
        return f"Playing the guitar"


def start_playing(ob):
    return ob.play()


g = Guitar()
print(start_playing(g))