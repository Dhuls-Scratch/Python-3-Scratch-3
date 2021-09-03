# Copyright (C) 2021 Dhuls-Scratch
#    This file is part of Python 3-Scratch 3.
#
#    Python 3-Scratch 3 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Python 3-Scratch 3 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Python 3-Scratch 3.  If not, see <https://www.gnu.org/licenses/>.
from scratchclient import ScratchSession
import random
import time

session = ScratchSession(USERNAME, PASSWORD)
connection = session.create_cloud_connection(PROJECTID)
while "a" != "b":
    connection.set_cloud_variable(VARNAME, random.randint(0, 550))
    print(connection.get_cloud_variable(VARNAME))
    time.sleep(0.2)
