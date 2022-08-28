# python marshmallow
https://marshmallow.readthedocs.io/en/stable/quickstart.html
# Some common terms
- **dump** - for serializing data which returns a dictionary with the  required format. Data validation not occurs here.

- **dumps** - for returning json

- **load** - for deserializing an input dictionary to an application-level data structure. It **validates** the input. Raises error if validation not successful

- **loads** - for json input