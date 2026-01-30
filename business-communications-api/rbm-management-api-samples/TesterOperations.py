# Copyright 2025 Google Inc. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import logging

from BusinessComms import *

logger = logging.getLogger(__name__)

def add_test_device(agentId, msisdn):
  """
  Add tester.

  See https://developers.google.com/business-communications/rcs-business-messaging/reference/business-communications/rest/v1/testers/create
  """

  endpoint_url = (BASE_ENDPOINT + 'testers')

  logger.info('Calling ' + endpoint_url)

  body = {
    "agentId": agentId,
    "phoneNumber": msisdn
  }

  resp, content = http_auth.request(endpoint_url,
    method='POST',
    headers={'Content-Type':'application/json',},
    body=json.dumps(body))
    
  return json.loads(content)

def get_tester(agentId, testerId):
  """
  Get tester.

  See https://developers.google.com/business-communications/rcs-business-messaging/reference/business-communications/rest/v1/testers/get
  """

  endpoint_url = (BASE_ENDPOINT +
    testerId +
    '?agentId=' + agentId)

  logger.info('Calling ' + endpoint_url)

  resp, content = http_auth.request(endpoint_url,
    method='GET',
    headers={'Content-Type':'application/json'})
    
  return json.loads(content)


def delete_tester(agentId, testerId):
  """
  Delete agent tester.

  See https://developers.google.com/business-communications/rcs-business-messaging/reference/business-communications/rest/v1/testers/delete
  """

  endpoint_url = (BASE_ENDPOINT +
    testerId +
    '?agentId=' + agentId)

  logger.info('Calling ' + endpoint_url)

  resp, content = http_auth.request(endpoint_url,
    method='DELETE',
    headers={'Content-Type':'application/json'})

  return


def list_testers(agentId):
  """
  List testers of an agent.

  See https://developers.google.com/business-communications/rcs-business-messaging/reference/business-communications/rest/v1/testers/list
  """

  endpoint_url = (BASE_ENDPOINT +
    'testers?' +
    'agentId=' + agentId)

  logger.info('Calling ' + endpoint_url)

  resp, content = http_auth.request(endpoint_url,
    method='GET',
    headers={'Content-Type':'application/json'})

  return json.loads(content)

