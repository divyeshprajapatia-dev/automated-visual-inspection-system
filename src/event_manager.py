import time

class EventManager:
    def __init__(self, min_duration=2.0):
        """
        min_duration: seconds object must persist before becoming an event
        """
        self.min_duration = min_duration
        self.objects = {}
        # structure:
        # {
        #   "person": {
        #       "first_seen": timestamp,
        #       "logged": True/False
        #   }
        # }

    def update(self, detected_objects):
        """
        detected_objects: set of object names detected in current frame
        Returns: list of object names that are NEW events
        """
        current_time = time.time()
        events_to_log = []

        # Handle detected objects
        for obj in detected_objects:
            if obj not in self.objects:
                # First time seeing this object
                self.objects[obj] = {
                    "first_seen": current_time,
                    "logged": False
                }
            else:
                elapsed = current_time - self.objects[obj]["first_seen"]
                if (
                    elapsed >= self.min_duration
                    and not self.objects[obj]["logged"]
                ):
                    events_to_log.append(obj)
                    self.objects[obj]["logged"] = True

        # Handle disappeared objects (reset state)
        for obj in list(self.objects.keys()):
            if obj not in detected_objects:
                del self.objects[obj]

        return events_to_log
