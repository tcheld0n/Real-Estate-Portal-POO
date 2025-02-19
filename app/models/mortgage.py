class Mortgage:
    def __init__(self, loan_amount, annual_rate, years):
        self.loan_amount = loan_amount  # Valor total do empréstimo
        self.annual_rate = annual_rate  # Taxa anual em porcentagem
        self.months = years * 12  # Converte anos para meses
        self.monthly_payment = self.calculate_monthly_payment()

    def calculate_monthly_payment(self):
        # Fórmula para calcular o valor da parcela mensal de uma hipoteca
        rate = self.annual_rate / 100 / 12  # Converter taxa anual para mensal
        if rate == 0:
            return self.loan_amount / self.months  # Sem juros, o valor é dividido pelos meses
        return (self.loan_amount * rate) / (1 - (1 + rate) ** -self.months)

    def __str__(self):
        return f"Parcela mensal: R${self.monthly_payment:.2f}"
