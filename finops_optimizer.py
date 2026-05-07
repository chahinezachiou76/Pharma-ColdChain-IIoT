import boto3
from datetime import datetime, timezone

# AWS Configuration
REGION = 'eu-west-1'
DAYS_THRESHOLD = 7

def check_unused_instances():
    # Initialize EC2 client
    ec2 = boto3.client('ec2', region_name=REGION)
    
    response = ec2.describe_instances()
    found_unused = False

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            launch_time = instance['LaunchTime']

            # Calculate the age of the instance
            age_days = (datetime.now(timezone.utc) - launch_time).days

            print(f"Checking Instance: {instance_id} | State: {state} | Age: {age_days} days")

            # Logic to identify unused/idle resources
            if state == "stopped" and age_days > DAYS_THRESHOLD:
                found_unused = True
                print(f">>> [FINOPS ALERT] Unused instance detected: {instance_id}")
                print(f">>> Recommendation: Terminate or Snapshot & Remove to save costs.")

    if not found_unused:
        print("No unused instances found. Infrastructure is cost-optimized.")

if __name__ == "__main__":
    print(f"--- FinOps Resource Optimization Scan: {datetime.now().strftime('%Y-%m-%d')} ---")
    check_unused_instances()