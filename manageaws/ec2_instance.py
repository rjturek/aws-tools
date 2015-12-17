# boto3 brings back a dict, so json processing is not needed
import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')

reservations = ec2_client.describe_instances().get('Reservations')
# pprint(reservations)

def get_instances_matching_tag(partial_tag):
    print('Looking for EC2 instances with "' + partial_tag + '" in one of the tags')
    matching_instances = []
    for res in reservations:
        all_instances = res.get('Instances')
        for inst in all_instances:
            tags = inst.get('Tags')
            for tag in tags:
                if partial_tag in tag.get('Value'):
                    matching_instances.append(inst)
                    break
    return matching_instances



def main():
    matching_instances = get_instances_matching_tag('rjt')
    print(len(matching_instances))

if __name__ == "__main__":
    main()

