"""
The 'journal_api' blueprint handles the API for managing journal entries.
Specifically, this blueprint allows for journal entries to be added, edited,
and deleted.
"""

from apifairy import body, other_responses, response
from flask import Blueprint, abort

from project.schemas.journal import EntrySchema, NewEntrySchema


# --------
# Database
# --------

messages = [
    dict(id=1, entry="The sun was shining when I woke up this morning."),
    dict(id=2, entry="I tried a new fruit mixture in my oatmeal for breakfast."),
    dict(id=3, entry="Today I ate a great sandwich for lunch."),
]

journal = Blueprint("journal_api", __name__)


@journal.route("/", methods=["GET"])
@response(EntrySchema)
def get_journals():
    """Return all journal entries"""
    return messages


@journal.route("/", methods=["POST"])
@body(NewEntrySchema)
@response(EntrySchema, 201)
def add_journal_entry(kwargs):
    """Add a new journal entry"""
    new_message = dict(**kwargs, id=messages[-1]["id"] + 1)
    messages.append(new_message)
    return new_message
