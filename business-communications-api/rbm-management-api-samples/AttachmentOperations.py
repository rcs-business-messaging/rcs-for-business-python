# Copyright 2025 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import logging

from BusinessComms import *

logger = logging.getLogger(__name__)

def upload_verification_document(parent, file_path, source="VERIFICATION_PAGE"):
  """
  Upload verification document (PDF) to Business Communications API.

  See https://developers.google.com/business-communications/rcs-business-messaging/reference/business-communications/rest/v1/brands.agents.attachments/create
  """
  endpoint_url = f"https://businesscommunications.googleapis.com/upload/v1/{parent}/attachments"

  params = {
      'uploadType': 'media',
      'attachmentOperationSource': source
  }

  logger.info(f"Uploading file {file_path} to {endpoint_url} with params {params}")

  with open(file_path, 'rb') as f:
    headers = {
        'Content-Type': 'application/pdf'
    }
    response = authed_session.post(endpoint_url, params=params, data=f, headers=headers)

  if response.status_code != 200:
    logger.error(f"Failed to upload document. Status code: {response.status_code}, content: {response.content}")
    raise Exception(f"Upload failed: {response.content.decode('utf-8')}")

  return json.loads(response.content)
