# Sensors dataset

## Summary

Generated dummy data for two sensors in different data formats. The Notebook used to generate the data is `_generator.ipynb`.

## Variables

### Sensor A

1. `TIME`: Date and time in format `YYYY-MM-DD HH:MM:SS` (string).
2. `TEMP`: Temperature (numeric).
3. `HUM`: Humidity (numeric).

Example data:

```
TIME;TEMP;HUM
2020-01-01 14:00:00;20.1;40.0
2020-01-01 14:00:01;20.2;39.8
```
### Sensor B

1. `TS`: Timestamp as epoch time (integer)
2. `CO2`: CO2 concentration (numeric)
3. `NO2`: NO2 concentration (numeric)

Example data:

```
TS|CO2|NO2
1577887200|602.200|1.973
1577887260|599.917|2.270
```

