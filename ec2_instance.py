# boto3 brings back a dict, so json processing is not needed
import boto3
import pprint

ec2 = boto3.resource('ec2')

for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    pprint.pprint(status)
    print('instanceId ' + status['InstanceId'])

