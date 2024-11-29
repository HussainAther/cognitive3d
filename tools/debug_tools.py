import logging

logging.basicConfig(level=logging.DEBUG)

def debug_event(event_name, details):
    """Log event details for debugging."""
    logging.debug(f"Event: {event_name}, Details: {details}")

