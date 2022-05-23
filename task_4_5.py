from task_4_3 import currency_rates

def main(argv):
    program, *args = argv

    request_date, currency_value = currency_rates(args[0])
    print(currency_value, request_date)

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))