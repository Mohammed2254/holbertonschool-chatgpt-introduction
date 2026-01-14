class Checkbook:
    def __init__(self):
        """
        Function Description:
        ---------------------
        Initializes a new Checkbook instance with a balance of 0.0.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        ---------------------
        Deposits a specified positive amount into the checkbook and prints the new balance.
        If the amount is non-positive, prints an error message.

        Parameters:
        -----------
        amount : float
            The amount of money to deposit.

        Returns:
        --------
        None
        """
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
        ---------------------
        Withdraws a specified positive amount from the checkbook if sufficient funds exist.
        Prints an error message if funds are insufficient or if the amount is non-positive.

        Parameters:
        -----------
        amount : float
            The amount of money to withdraw.

        Returns:
        --------
        None
        """
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
        ---------------------
        Prints the current balance of the checkbook.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
    ---------------------
    Runs the interactive checkbook program where the user can deposit,
    withdraw, check balance, or exit.
    Handles invalid inputs gracefully without crashing.

    Parameters:
    -----------
    None

    Returns:
    --------
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
