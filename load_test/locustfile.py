from locust import HttpUser, task, between

class AddTaskUser(HttpUser):
    wait_time = between(1, 5)  # Simulates a wait time between requests

    @task
    def trigger_add_task(self):
        # Define the payload for the POST request
        payload = {"x": 5, "y": 3}
        
        # Send a POST request to the add task endpoint
        self.client.post("/tasks/add/", json=payload)
