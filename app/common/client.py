

def query_find_to_dictionary(db, collection, query, projection):
    query_result = db[collection].find(query, projection)
    return [dict(i) for i in query_result]
