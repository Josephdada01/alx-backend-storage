#!/usr/bin/env python3
"""
a Python function that lists all documents in a collection:
"""


def list_all(mongo_collection):
    """
    Return an empty list if no document in the collection
    """
    documents = list(mongo_collection.find({}))

    # if documents.count() == 0:
        # return []
    return documents
