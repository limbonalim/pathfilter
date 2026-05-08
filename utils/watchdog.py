from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from init import init

from utils.config import config
data = config.get_config()
const_path = data['path']

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        init()
        print(f"File created: {event.src_path}")

event_handler = Handler()
observer = Observer()

observer.schedule(event_handler, path=const_path, recursive=False)

def run_watchdog():
    if not observer.is_alive():
        try:
            observer.start()
            print("Watchdog started")
        except RuntimeError:
            reinit_observer()
            observer.start()
            print("Reinitialized and started watchdog")
  
def reinit_observer():
    global observer
    observer = Observer()
    observer.schedule(event_handler, path=const_path, recursive=False)

def stop_watchdog():
    if observer.is_alive():
        observer.stop()
        print("Watchdog stopped")
