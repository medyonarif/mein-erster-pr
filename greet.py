"""Ein winziges Begrüßungsskript."""


def greet(name: str) -> str:
    """Gibt eine Begrüßung für den übergebenen Namen zurück."""
    return f"Hallo, {name}!"


if __name__ == "__main__":
    print(greet("Welt"))
