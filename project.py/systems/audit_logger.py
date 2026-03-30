import datetime

class AuditLogger:
    def log(self, msg):
        print(f"[{datetime.datetime.now()}] {msg}")