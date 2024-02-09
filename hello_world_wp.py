
from prefect import flow


@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")


if __name__ == "__main__":
    hello_world.from_source(
        entrypoint="hello_world_wp.py:hello_world"
    ).deploy(
        name="my-first-deployment", 
        work_pool_name="my-managed-pool", 
    )

# Authenticate with Prefect Cloud
#client = Client(api_token="pnu_gxfq22qpQ1k13tvnr1Y2hvSBREL3AA19oOGf")

# Register the flow with Prefect Cloud
#flow_id = flow.register(project_name="project-test")

# Create a deployment for the flow
#deployment_id = client.create_deployment(flow_id=flow_id, deployment_name="my-first-deployment")

# Trigger a run for the deployment
#run = client.create_flow_run(deployment_id=deployment_id)
