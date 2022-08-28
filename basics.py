from datetime import date
from pprint import pprint

from marshmallow import Schema , fields 

# declaring schema
class ArtistSchema(Schema):
    name = fields.Str()

class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

artist = dict(name="Arnab")
album = dict(artist=artist,title="Hun",release_date=date(2000,12,17))

# Serializing objects(dumping)
schema = AlbumSchema()
result = schema.dump(album)
pprint(result,indent=4)

# Serializing objects(dumping) to json
result = schema.dumps(album)
pprint(result,indent=4)

# filtering output
album = dict(artist=artist,title="Hun",release_date=date(2000,12,17))
summary = AlbumSchema(only=("title","artist"))
result = summary.dump(album)
pprint(result)