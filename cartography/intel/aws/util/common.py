import logging

from typing import List

logger = logging.getLogger(__name__)

def parse_and_validate_aws_requested_syncs(aws_requested_syncs: str) -> List[str]:
  from cartography.intel.aws.resources import RESOURCE_FUNCTIONS
  validated_resources: List[str] = []
  for resource in aws_requested_syncs.split(','):
    resource = resource.strip()

    if resource in RESOURCE_FUNCTIONS:
      validated_resources.append(resource)
    else:
      valid_syncs: str = ', '.join(RESOURCE_FUNCTIONS.keys())
      raise ValueError(
        f'Error parsing `aws-requested-syncs`. You specified "{aws_requested_syncs}". '
        f'Please check that your string is formatted properly. '
        f'Example valid input looks like "s3,iam,rds" or "s3, ec2:instance, dynamodb". '
        f'Our full list of valid values is: {valid_syncs}.',
      )
  return validated_resources

def extract_name_from_tags(resource_with_tags, key = 'Tags'):
  # logger.info(f"extract_name_from_tags.resource_with_tags: {resource_with_tags}")
  name_tag = [tag['Value'] for tag in resource_with_tags.get(key, {}) if tag.get('Key', None) == 'Name']
  name = name_tag[0] if len(name_tag) > 0 else '-'
  #logger.info(f"extract_name_from_tags.name: {name}")
  return name
