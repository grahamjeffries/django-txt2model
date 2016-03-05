##django-txt2model

The purpose of this tool is simplify the creation of well appointed Django `models.py` files for projects which require database tables with many columns. In the motivating use case, large database tables are desired for holding scientific simulation model inputs and outputs. I automated the creation of these model specs to avoid the tedium of manually writing them.

##Requirements
Python (Tested with 2.7 and 3.5, presumably works on others)

##Example
Running the script is easy:

```
python txt2model.py example_input.txt --output ./models.py
```

##Text file format
The input file should be tab delimited, must include a header with column names in the first row, and include columns for `model_name`, `field_name`, and `field_type`. Any additional columns provided will be parsed as keyword arguements to be included in the field definition. Columns with blank values `''` are ignored. Currently quoted text fields in the input text file are not supported, and will yield double quoted parameter values.

##Limitations
- The script does not break lines when too long for PEP8. You'll have to do that yourself, for now.
- The above also applies to iterable objects such as `choices` which typically desire some formatting.
- Model field argument values are not validated for proper type.
- Model fields are not evaluated to ensure that required fields are provided.

##License
MIT