from finance_calculator import FinanceCalculator


def main():
    calc = FinanceCalculator()

    # Пример использования
    calc.add_income(2000)
    calc.add_expense(750)
    calc.add_income(500)
    calc.add_expense(300)

    print("==== Finance Calculator!!! ====")
    print(f"Current balance: {calc.get_balance()}")


if __name__ == "__main__":
    main()
