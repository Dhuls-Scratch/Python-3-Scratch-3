from scratchclient import ScratchSession
import random
import time

session = ScratchSession(USERNAME, PASSWORD)
connection = session.create_cloud_connection(PROJECT ID)
while "a" != "b":
    connection.set_cloud_variable(VARNAME, random.randint(0, 550))
    print(connection.get_cloud_variable(VARNAME))
    time.sleep(0.2)
