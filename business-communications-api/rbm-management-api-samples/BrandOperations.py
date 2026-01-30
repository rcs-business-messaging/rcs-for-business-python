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

def list_brands():
  """
  List brands.

  See https://developers.google.com/business-communications/rcs-business-messaging/reference/business-communications/rest/v1/brands/list
  """

  endpoint_url = (BASE_ENDPOINT + 'brands')

  logger.info('Calling ' + endpoint_url)

  response = authed_session.get(endpoint_url)

  return json.loads(response.content)


def get_brand(brandId):
  """
  Get brand definition.

  See https://developers.google.com/business-communications/rcs-business-messaging/reference/business-communications/rest/v1/brands/get
  """

  endpoint_url = (BASE_ENDPOINT + brandId)

  logger.info('Calling ' + endpoint_url)

  response = authed_session.get(endpoint_url)

  return json.loads(response.content)