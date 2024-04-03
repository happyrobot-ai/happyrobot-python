import datetime
import pytz


def parse_date(timestamp_str: str):
    # Parse the timestamp string into a datetime object
    timestamp = datetime.datetime.fromisoformat(timestamp_str)

    # Convert the timestamp to Eastern Standard Time (EST)
    est_timezone = pytz.timezone('America/New_York')
    timestamp_est = timestamp.astimezone(est_timezone)

    # Format the timestamp into a more readable format including the timezone
    readable_format_with_timezone = timestamp_est.strftime("%B %d, %Y %H:%M:%S %Z")

    return readable_format_with_timezone
