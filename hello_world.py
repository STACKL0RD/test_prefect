from prefect import flow


@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")


if __name__ == "__main__":
    hello_world.from_source(
        source="https://github.com/STACKL0RD/test_prefect.git", 
        entrypoint="repo_info.py:get_repo_info"
    ).deploy(
        name="my-first-deployment", 
        work_pool_name="my-managed-pool", 
    )


#if __name__ == "__main__":
#    hello_world.serve(name="my-first-deployment",
#                      tags=["onboarding"],
#                      parameters={"goodbye": True},
#                      interval=60)