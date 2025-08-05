from pydantic import BaseModel, field_validator, ValidationError


class AgeValidator(BaseModel):
    """Pydantic model to validate age input"""
    age: int

    @field_validator("age")
    @classmethod
    def age_in_range(cls, v):
        if v < 1 or v > 120:
            raise ValueError("Out of range. Please enter a number between 1 and 120.")
        return v


def get_valid_age():
    """Keep prompting user until valid age input is provided"""
    while True:
        try:
            # Get user input
            user_input = input("Enter your age (1–120): ").strip()
            
            # Handle empty input
            if not user_input:
                print("Invalid input. Please enter a valid number.")
                continue
            
            # Convert to integer (handles 'abc' case)
            age_int = int(user_input)
            
            # Validate using Pydantic (handles '150' case)
            validator = AgeValidator(age=age_int)
            
            # Valid input (handles '25' case)
            print(f"Valid input. Your age is {validator.age}.")
            return validator.age
            
        except ValueError as e:
            # Handle both int conversion and range validation errors
            if "invalid literal for int()" in str(e):
                print("Invalid input. Please enter a valid number.")
            else:
                print(str(e))
        except ValidationError:
            print("Invalid input. Please enter a valid number.")


def main():
    """Main function to run the age validator"""
    get_valid_age()


if __name__ == "__main__":
    main()
