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

import argparse
import logging

from BrandOperations import *
from TesterOperations import *


logger = logging.getLogger(__name__)

def main():
  logging.basicConfig(level=logging.INFO)

  parser = argparse.ArgumentParser()

  parser.add_argument('-m', action='store',
    required=True, dest='agent_mode', help = 'Use list_brands, get_brand, add_test_device, get_tester, delete_tester or list_testers')

  parser.add_argument('-a', action='store',
    required=False, dest='agent_id', help = 'Agent id. (The part before "@rbm.goog")', default='')

  parser.add_argument('-t', action='store',
    required=False, dest='tester_id', help = 'Tester id. (Unique id assigned to a tester")', default='')

  parser.add_argument('-b', action='store',
    required=False, dest='brand_id', help = 'Brand name. (Unique name assigned to a brand - brands/<uuid>")', default='')

  parser.add_argument('-msisdn', action='store',
    required=False, dest='msisdn', help = 'Mobile number, in full international format: +CCNNNNNNNNNN', default='')

  args = parser.parse_args()


  # Brand operations
  if 'list_brands' in args.agent_mode:
    res = list_brands()
    logger.info('List of brands:')
    logger.info(res)
    return

  if 'get_brand' in args.agent_mode:
    if args.brand_id == '':
      print('-b <brand name> is required')
      return
    res = get_brand(args.brand_id)
    logger.info('Brand info:')
    logger.info(res)
    return

  # Tester operations
  if 'add_test_device' in args.agent_mode:
    if args.msisdn == '':
      print('-msisdn <mobile number> is required')
      return
    if args.agent_id == '':
      print('-a <agent id> is required')
      return
    res = add_test_device(args.agent_id, args.msisdn)
    logger.info('Tester details:')
    logger.info(res)
    return

  if 'get_tester' in args.agent_mode:
    if args.tester_id == '':
      print('-t <tester id> is required')
      return
    res = get_tester(args.agent_id, args.tester_id)
    logger.info('Tester details:')
    logger.info(res)
    return

  if 'delete_tester' in args.agent_mode:
    if args.tester_id == '':
      print('-t <tester id> is required')
      return
    delete_tester(args.agent_id, args.tester_id)
    return

  if 'list_testers' in args.agent_mode:
    if args.agent_id == '':
      print('-a <agent id> is required')
      return
    res = list_testers(args.agent_id)
    logger.info('Result of listing testers:')
    logger.info(res)
    return

  print('Unknown command: use list_brands, get_brand, add_test_device, get_tester, delete_tester or list_testers')

if __name__ == '__main__':
  main()