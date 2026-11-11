import requests

class CompanyHelp:

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str, users: dict = None) -> requests.Response:
        #Создание проекта
        payload = {"title": title}
        if users:
            payload["users"] = users

        return requests.post(
            url=f"{self.base_url}/api-v2/projects",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id: str, headers: dict = None) -> requests.Response:
        #Получение проекта
        current_headers = headers if headers is not None else self.headers
        return requests.get(
            url=f"{self.base_url}/api-v2/projects/{project_id}",
            headers=current_headers
        )

    def update_project(self, project_id: str, title: str) -> requests.Response:
         #Изменение проекта
        payload = {"title": title}
        return requests.put(
            url=f"{self.base_url}/api-v2/projects/{project_id}",
            json=payload,
            headers=self.headers
        )