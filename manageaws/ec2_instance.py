# boto3 brings back a dict, so json processing is not needed
import boto3
from pprint import pprint

def get_instances_matching_tag(partial_tag):
    """
    Args:
        param1 (str): String which identifies Instances of interest. Will be matched against all tag values

    Returns:
        List of instances with one or more tags containing the supplied partial_tag string
    """
    print('Looking for EC2 instances with "' + partial_tag + '" in one of the tags')

    ec2_client = boto3.client('ec2')
    pprint(ec2_client.describe_instances())

    ec2 = boto3.resource('ec2')
    all_instances = ec2.instances.all()

    matching_instances = []
    for inst in all_instances:
        pprint(inst)
        for tag in inst.tags:
            if tag.get('Key') == "Name" and partial_tag in tag.get('Value'):
                matching_instances.append(inst)
                break
    return matching_instances

def start_both_rjt_instances():
    """
    Start both rjt instances.  Only starts an instance if it is stopped.
    If an instance is pending, it will be left alone, assuming it is starting
    If an instance is stopping

    Returns:
        bool - success
    """
    instances = get_instances_matching_tag('rjt')
    if len(instances) != 2:
        raise Exception('Did not find exactly 2 instances.  Found ' + str(len(instances)) + ' instances')

    for inst in instances:
        if inst.state.get('Name') == "stopped":
           print( "Starting instance: ", inst.id)
           inst.start()
        # any of these statuses cannot be started
        elif inst.state.get('Name') in ['shutting-down', 'terminated', 'stopping']:
            return False
    return True

def stop_both_rjt_instances():
    """
    Stop both rjt instances.  Only stops an instance if it is running.
    If an instance is pending, it will be left alone, assuming it is starting
    If an instance is stopping

    Returns:
        bool - success
    """
    instances = get_instances_matching_tag('rjt')
    for inst in instances:
        if inst.state.get('Name') == "running":
            print( "Stopping instance: ", inst.id)
            inst.stop()
        # This status cannot be stopped
        elif inst.state.get('Name') in ['pending']:
            return False
    return True


def main():
    # success = start_both_rjt_instances()
    success = stop_both_rjt_instances()
    #success = toggle_rjt_instances()
    print('Did it work: ', success)


if __name__ == "__main__":
    main()

