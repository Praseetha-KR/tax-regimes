# Tax Regimes Comparison

Compares Indian Tax regimes of 2019 & 2020 and suggest which one has the lowest tax.


### Sample Usage

```shell
In [1]: from tax_regimes import lowest

In [2]: tax = lowest(1234567, 1500000, 35000, 74000)

In [3]: tax.total_tax
Out[3]: 113997

In [4]: tax.YEAR
Out[4]: 2019

In [5]: print(tax.tabular())
Out[5]: 

2019 Tax Regime:
+--------------------+--------------------------------+
| Gross Income       | 1234567                        |
+--------------------+--------------------------------+
| Deductions         | 80C (upto 150000):      150000 |
|                    | 80D (upto 25000):       25000  |
|                    | 24(b) (upto 75000):     74000  |
+--------------------+--------------------------------+
| Tax Rate for Slabs | (0-250000) NIL                 |
|                    | (250000-500000) @5%            |
|                    | (500000-1000000) @20%          |
|                    | (1000000-∞) @30%               |
+--------------------+--------------------------------+
| Income Tax         | 109613                         |
+--------------------+--------------------------------+
| Cess@4%            | 4384                           |
+--------------------+--------------------------------+
| Total Tax          | 113997                         |
+--------------------+--------------------------------+
```

Or, for interactive version:
```shell
In [1]: from tax_regimes import lowest_via_cli

In [2]: lowest_via_cli()

Indian Tax Regime Comparison
(All units are in INR)

Enter income: 1234567
Enter expenses under section 80C (investments & payments): 1500000
Enter expenses under section 80D (health insurance): 35000
Enter expenses under section 24(b) (housing loan): 74000

2019 Tax Regime:
+--------------------+--------------------------------+
| Gross Income       | 1234567                        |
+--------------------+--------------------------------+
| Deductions         | 80C (upto 150000):      150000 |
|                    | 80D (upto 25000):       25000  |
|                    | 24(b) (upto 75000):     74000  |
+--------------------+--------------------------------+
| Tax Rate for Slabs | (0-250000) NIL                 |
|                    | (250000-500000) @5%            |
|                    | (500000-1000000) @20%          |
|                    | (1000000-∞) @30%               |
+--------------------+--------------------------------+
| Income Tax         | 109613                         |
+--------------------+--------------------------------+
| Cess@4%            | 4384                           |
+--------------------+--------------------------------+
| Total Tax          | 113997                         |
+--------------------+--------------------------------+


2020 Tax Regime:
+--------------------+------------------------+
| Gross Income       | 1234567                |
+--------------------+------------------------+
| Deductions         | 80C:    NA             |
|                    | 80D:    NA             |
|                    | 24(b):  NA             |
+--------------------+------------------------+
| Tax Rate for Slabs | (0-250000) NIL         |
|                    | (250000-500000) @5%    |
|                    | (500000-750000) @10%   |
|                    | (750000-1000000) @15%  |
|                    | (1000000-1250000) @20% |
|                    | (1250000-1500000) @25% |
|                    | (1500000-∞) @30%       |
+--------------------+------------------------+
| Income Tax         | 121913                 |
+--------------------+------------------------+
| Cess@4%            | 4876                   |
+--------------------+------------------------+
| Total Tax          | 126789                 |
+--------------------+------------------------+



Result:
+-------------------+----------+
| Lowest Tax Regime | ✨2019✨ |
+===================+==========+
| Tax to be paid    | 113997   |
+-------------------+----------+
```

