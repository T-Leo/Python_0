def slr():
    try:
        wrk_hrs = float(input('enter the amount of hours- '))
        pmnt_rate = float(input('enter the payment rate- '))
        extra = float(input('enter the bonus- '))
        slr = wrk_hrs * pmnt_rate + extra
        print(f'salary is-  {slr}')
    except ValueError:
        return print('invalid input')


slr()
