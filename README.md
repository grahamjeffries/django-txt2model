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
Forthcoming...

##License
MIT