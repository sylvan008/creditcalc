# Credit calc

**Учебный проект**. Рассчитывает месячный платёж для дифференцированного кредита. Либо один из трёх параметров для
аннуитетного кредита: сумму займа, ежемесячный платёж, количество месяцев для погашения займа. В обоих случаях
показывает переплату по кредиту.

## Параметры запуска

Скрипт запускает через терминал.
```
python creditcalc.py
```
Для получения справки по параметрам запуска добавьте флаг `-h` или `--help`.
```
python creditcalc.py --help
```
Допустимые параметры:
- `--type` - устанавливает тип займа: **diff**, **annuity**. **Обязательный параметр**.
- `--interest` - процентная ставка по кредиту, указывает без знака **%**. **Обязательный параметр**.
- `--principal` - основная сумма займа.
- `--payment` - ежемесячная выплата по займу. Не указывает если тип расчёта **diff**.
- `--periods` - количество месяцев для погашения займа.

**Пример 1**. Рассчёт дифференцированного кредита.
```
python creditcalc.py --type=diff --interest=7.8 --principal=500000 --periods=6
```
Выведет в консоль следующее:
```
Month 1: payment is 86584
Month 2: payment is 86042
Month 3: payment is 85500
Month 4: payment is 84959
Month 5: payment is 84417
Month 6: payment is 83875
Overpayment = 11377
```

Для расчёта одного из параметров кредита типа **annuity**, не указывайте его в параметрах запуска.

**Пример 2**. для расчёт количества месяцев для погашения кредита, укажите сумму займа, ежемесячный платёж,
процентную ставку.
```
python creditcalc.py --type=annuity --interest=10 --principal=800000 --payment=12000
```
Вывод в консоли:
```
It will take 8 years and 2 months to repay this loan!
Overpayment = 376000
```