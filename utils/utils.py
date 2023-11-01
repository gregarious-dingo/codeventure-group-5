class Utils:
    @staticmethod
    def display_str(str):
        str = f"| {str} |"
        print(len(str) * "-")
        print(str)
        print(len(str) * "-")

    @staticmethod
    def invalid_input():
        Utils.display_str("Invalid input! Please select another option: ")