import pprint

import motor.motor_asyncio
import motor
conn_str = "mongodb://fmongo"

# set a 5-second connection timeout
client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)



async def search_author_db(name):
    cursor = client.FastReadsbot.books.find({'author': {
        '$regex': f'(?i){name}(?-i)'
    }}).sort('author')
    res = []
    for document in await cursor.to_list(length=10):
        pprint.pprint(document)
        res.append(document)

    return res  # books


async def search_title_db(title):
    cursor = client.FastReadsbot.books.find({'title': {
        '$regex': f'(?i){title}(?-i)'
    }}).sort('title')  # TODO: sort results based on popularity and/or downloads
    res = []
    for document in await cursor.to_list(length=10):
        res.append(document)

    return res  # books


async def get_server_info():
    # replace this with your MongoDB connection string
    conn_str = "mongodb://localhost:27017"
    # set a 5-second connection timeout
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    try:
        print(await client.server_info())
    except Exception:
        print("Unable to connect to the server.")


async def do_insert():
    result = await client.test_collection.insert_many()(

        [{'i': i} for i in range(50)])

    print('inserted %d docs' % (len(result.inserted_ids),))


# loop = asyncio.get_event_loop(
if __name__ == '__main__':
    conn_str = "mongodb://localhost:27017"
    # set a 5-second connection timeout
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    loop = client.get_io_loop()
    books = loop.run_until_complete(search_author_db(''))
    print(books)
