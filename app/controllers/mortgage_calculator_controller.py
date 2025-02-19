from app.models.mortgage_calculator import MortgageCalculator

class MortgageCalculatorController:
    def __init__(self):
        self.calculations = []

    def create_calculation(self, loan_amount, annual_rate, months):
        calculator = MortgageCalculator(annual_rate, months)
        calculator.set_loan_amount(loan_amount)  # Define o valor do empréstimo
        self.calculations.append(calculator)
        return calculator

    def get_monthly_payment(self, calculator):
        return calculator.monthly_payment

    def simulate_payment(self, loan_amount, annual_rate, months):
        # Simula uma hipoteca sem criar uma instância
        calculator = MortgageCalculator(annual_rate, months)
        calculator.set_loan_amount(loan_amount)
        return calculator.monthly_payment