import os
import json
import requests
from functools import wraps
from typing import Dict, Any, Optional

class LitLyxSender:
    def __init__(self, url: str = "https://broker.litlyx.com/event",
                 default_pid: Optional[str] = None,
                 default_name: str = "default_event",
                 default_metadata: Dict[str, Any] = None,
                 default_website: str = "default_website.com",
                 default_user_agent: str = "LitLyxSender/1.0"):
        self.url = url
        self.default_pid = default_pid or os.environ.get('LITLYX_PID', "default_pid")
        self.default_name = default_name
        self.default_metadata = default_metadata or {"example": "value"}
        self.default_website = default_website
        self.default_user_agent = default_user_agent
        self.headers = {"Content-Type": "application/json"}

    def send_event(self, pid: Optional[str] = None,
                   name: Optional[str] = None,
                   metadata: Optional[Dict[str, Any]] = None,
                   website: Optional[str] = None,
                   user_agent: Optional[str] = None) -> requests.Response:
        """
        Send an event to LitLyx.

        :param pid: Project ID
        :param name: Event name
        :param metadata: Event metadata
        :param website: Website identifier
        :param user_agent: User agent string
        :return: Response from the LitLyx server
        """
        data = {
            "pid": pid or self.default_pid,
            "name": name or self.default_name,
            "metadata": json.dumps(metadata or self.default_metadata),
            "website": website or self.default_website,
            "userAgent": user_agent or self.default_user_agent
        }

        response = requests.post(self.url, headers=self.headers, json=data)

        if response.status_code == 200:
            print("Event sent successfully.")
        else:
            print(f"Failed to send event. Status code: {response.status_code}")
            print(f"Response: {response.text}")

        return response

    def event_decorator(self, pid: Optional[str] = None,
                        name: Optional[str] = None,
                        metadata: Optional[Dict[str, Any]] = None,
                        website: Optional[str] = None,
                        user_agent: Optional[str] = None):
        """
        Decorator for sending an event before executing a function.

        :param pid: Project ID
        :param name: Event name
        :param metadata: Event metadata
        :param website: Website identifier
        :param user_agent: User agent string
        :return: Decorated function
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                self.send_event(pid, name, metadata, website, user_agent)
                return func(*args, **kwargs)
            return wrapper
        return decorator