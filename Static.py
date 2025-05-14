class TempConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

result = TempConverter.celsius_to_fahrenheit(25)
print(f"25 degrees Celsius is equal to {result} degrees Fahrenheit.")        