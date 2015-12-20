# boto3 brings back a dict, so json processing is not needed
import time
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
    If an instance is running or pending, it will be left alone, assuming it will start (become running).
    If an instance is not stopped or pending, we return failure.

    Returns:
        bool - success

    All statuses:
        pending
        running
        shutting-down
        terminated
        stopping
        stopped
    """
    instances = get_instances_matching_tag('rjt')
    if len(instances) != 2:
        raise Exception('Did not find exactly 2 instances.  Found ' + str(len(instances)) + ' instances')

    for inst in instances:
        if inst.state.get('Name') == "stopped":
           print( "Starting instance: ", inst.id)
           inst.start()
        elif inst.state.get('Name') == 'pending':
            print('Instance ', inst.id, " is already starting (pending)")
        else:
            return False

    return True

def stop_both_rjt_instances():
    """
    Stop both rjt instances.  Only stops an instance if it is running.
    If an instance is stopping, it will be left alone, assuming it will stop.
    If an instance is shutting-down

    Returns:
        bool - success
    """
    instances = get_instances_matching_tag('rjt')
    if len(instances) != 2:
        raise Exception('Did not find exactly 2 instances.  Found ' + str(len(instances)) + ' instances')
    for inst in instances:
        state = inst.state.get('Name')
        if  state == "running":
            print( "Stopping instance", inst.id)
            inst.stop()
        elif state == 'stopping':
            print('Instance', inst.id, "is already stopping")
        elif state == 'stopped':
            print('Instance', inst.id, "is already stopped")
        else:
            print ('Instance', inst.id, "cannot be stopped. Status:", state)
            return False

    start = time.time()
    instances[0].wait_until_stopped().wait()
    end = time.time()
    print("Time to stop", end - start)

    return True


def toggle_rjt_instances():
    """
    Will stop the running instance and start the stopped instance.
    Can only succeed if one rjt instance is running and the other is stopped.
    If any other combination is encountered, no state changes will be performed
    and the funciton will return False.

    Returns:
        bool - success
    """
    instances = get_instances_matching_tag('rjt')
    if len(instances) != 2:
        raise Exception('Did not find exactly 2 instances.  Found ' + str(len(instances)) + ' instances')
    statuses = [instances[0].state.get('Name'), instances[1].state.get('Name')]
    if "stopped" not in statuses or "running" not in statuses:
        print("Did not find one stopped and the other running")
        return False
    if statuses[0] == "stopped":
        instances[0].start()
        instances[1].stop()
    else:
        instances[0].stop()
        instances[1].start()
    return True

def main():
    # success = start_both_rjt_instances()
    # print('Did they start: ', success)
    success = stop_both_rjt_instances()
    print('Did they stop: ', success)
    # success = toggle_rjt_instances()
    # print('Did they toggle: ', success)


if __name__ == "__main__":
    main()

