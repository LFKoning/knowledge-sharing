# Banking dataset

## Summary

The data is related with direct marketing campaigns (phone calls) of a Portuguese
banking institution. The classification goal is to predict if the client will subscribe
to a term deposit (variable y).

## Variables

The dataset contains the following variables:

### Related to client:

1. `age`: age in years (numeric)
2. `job`: type of job (categorical)
3. `marital` : marital status (categorical)
4. `education`: level of education(categorical)
5. `default`: has credit in default? (categorical)
6. `housing`: has housing loan? (categorical)
7. `loan`: has personal loan? (categorical)

### Related to the last contact of the current campaign:

8. `contact`: contact communication type (categorical)
9. `month`: last contact month of year (categorical)
10. `day_of_week`: last contact day of the week (categorical)
11. `duration`: last contact duration, in seconds (numeric)

*Note: `duration` is not known prior to contacting the client; so `duration = 0` means
`y = 0`. Therefore `duration` should not be included for prediction.*

### Other attributes:

12. `campaign`: number of contacts performed during this campaign and for this client (numeric)
13. `pdays`: number of days passed after the client was last contacted for a previous campaign (numeric)
14. `previous`: number of contacts performed before this campaign and for this client (numeric)
15. `poutcome`: outcome of the previous marketing campaign (categorical)

### Social and economic context:

16. `emp.var.rate`: employment variation rate - quarterly indicator (numeric)
17. `cons.price.idx`: consumer price index - monthly indicator (numeric)
18. `cons.conf.idx`: consumer confidence index - monthly indicator (numeric)
19. `euribor3m`: euribor 3 month rate - daily indicator (numeric)
20. `nr.employed`: number of employees - quarterly indicator (numeric)

## Source

Downloaded from: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing

## Reference

[Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict
the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31,
June 2014