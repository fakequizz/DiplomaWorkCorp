import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SERVER_URL = "http://127.0.0.1:8000/log/"

class FileMonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"New file detected: {event.src_path}")
        requests.post(SERVER_URL, json={"event_type": "file_created", "file_path": event.src_path})

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")
        requests.post(SERVER_URL, json={"event_type": "file_modified", "file_path": event.src_path})

if __name__ == "__main__":
    path = "C:/Users/gabid/Desktop/Diploma"
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("Monitoring started...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
