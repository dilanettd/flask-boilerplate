from .. import ma

# -------
# Schemas
# -------

class NewEntrySchema(ma.Schema):
    """Schema defining the attributes when creating a new journal entry."""
    entry = ma.String(required=True)


class EntrySchema(ma.Schema):
    """Schema defining the attributes in a journal entry."""
    id = ma.Integer()
    entry = ma.String()
