import json
import os
from datetime import datetime

class DetectionLogger:
    def __init__(self, log_file="outputs/logs/detections.json"):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Ensure file exists and contains valid JSON list
        if not os.path.exists(self.log_file):
            self._initialize_log_file()
        else:
            self._validate_log_file()

    def _initialize_log_file(self):
        with open(self.log_file, "w") as f:
            json.dump([], f)

    def _validate_log_file(self):
        try:
            with open(self.log_file, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError
        except (json.JSONDecodeError, ValueError):
            # Reset corrupted or invalid file
            self._initialize_log_file()

    def log(self, source, object_name, confidence):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "source": source,
            "object": object_name,
            "confidence": round(confidence, 3)
        }

        with open(self.log_file, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
