def input_temperature(temp_str: str) -> int:
    try: 
        temp_int = int(temp_str)
    except ValueError: 
        print("Caught input_temperature error: invalid literal for int() with base 10: 'abc'")
    else: 
        print(f"Temperature is now {temp_int}°C")
        return temp_int
    return 0

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    input_temperature("25")
    print()
    print("Input data is 'abc'")
    input_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()