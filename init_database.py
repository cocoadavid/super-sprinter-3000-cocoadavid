from models import *


class InitDatabase:

    def init_db():
        ConnectDatabase.db.drop_tables([UserStory], safe=True, cascade=True)
        ConnectDatabase.db.create_tables([UserStory], safe=True)