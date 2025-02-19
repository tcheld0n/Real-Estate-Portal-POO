class MortgageCalculator:
    def __init__(self, annual_rate, months):
        self.annual_rate = annual_rate  # Taxa anual em porcentagem
        self.months = months  # Quantidade de meses
        self.monthly_payment = self.calculate_monthly_payment()

    def calculate_monthly_payment(self):
        # Fórmula para calcular o valor da parcela mensal de uma hipoteca
        rate = self.annual_rate / 100 / 12  # Converter taxa anual para mensal
        if rate == 0:
            return 0  # Caso a taxa de juros seja 0%, o valor é simplesmente o empréstimo dividido pelos meses
        return (self.loan_amount * rate) / (1 - (1 + rate) ** -self.months)

    def set_loan_amount(self, loan_amount):
        self.loan_amount = loan_amount  # Define o valor do empréstimo (hipoteca)
        self.monthly_payment = self.calculate_monthly_payment()  # Recalcula a mensalidade

    def __str__(self):
        return f"Parcela mensal: R${self.monthly_payment:.2f}"