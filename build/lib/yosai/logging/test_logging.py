"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
 
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from s_logging import LogManager
import logging


def logmanager_init():
    return LogManager().get_logger()


def test_logging(mylog):
    mylog.info('All systems operational')
    mylog.info('it works!', difficulty='easy')  


log = logging.getLogger()
print('before, hashandlers: ', log.hasHandlers())
test_logging(logmanager_init())
print('after, hashandlers: ', log.hasHandlers())


log = logging.getLogger()
print('before, hashandlers: ', log.hasHandlers())
test_logging(logmanager_init())
print('after, hashandlers: ', log.hasHandlers())
