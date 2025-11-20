from prefect import flow, task
from extract import extract_data
from load import load_data

@task
def extract_task():
    return extract_data()

@task
def load_task(data):
    return load_data(data)

@flow
def main_flow():
    data = extract_task()
    result = load_task(data)
    print("ID inserido:", result)

if __name__ == "__main__":
    main_flow()
