from models import *

db.connect()
db.drop_table(UserStoryManager)
db.create_table(UserStoryManager)

UserStoryManager.create(title="First story",
                 story="This is the first story",
                 criteria="Here is the criteria to complete the first user story",
                 value=100,
                 estimation=0.5,
                 status="To Do")

UserStoryManager.create(title="Second story",
                 story="This is the second story",
                 criteria="Here is the criteria to complete the second user story",
                 value=1500,
                 estimation=1.5,
                 status="To Do")