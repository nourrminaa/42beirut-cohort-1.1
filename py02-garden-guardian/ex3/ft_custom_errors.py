class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def check_health(self) -> None:
        if self.age > 10:
            raise PlantError(f"The {self.name} is wilting!")


def check_tank(liters: int) -> None:
    if liters < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    tomato = Plant("tomato", age=15)

    print("\nTesting PlantError...")
    try:
        tomato.check_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_tank(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        tomato.check_health()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        check_tank(2)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
