from scratchclient import ScratchSession
import random
import time

session = ScratchSession(username, password)
connection = session.create_cloud_connection(projectID)
while "a" != "b":
    connection.set_cloud_variable(varname, random.randint(0, 550))
    print(connection.get_cloud_variable(varname))
    time.sleep(0.2)
