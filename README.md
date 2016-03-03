##django-txt2model

The purpose of this tool is simplify the creation of well appointed Django `models.py` files for projects which require database tables with many columns. In the motivating use case, large database tables are desired for holding scientific simulation model inputs and outputs. I automated the creation of these model specs to avoid the tedium of manually writing them.

##Using the script
Running the script is easy:

```
python txt2model.py -i example.txt -o ./models.py
```

##Text file format
Forthcoming...