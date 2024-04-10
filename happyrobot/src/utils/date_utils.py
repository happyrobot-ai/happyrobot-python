import datetime
import pytz


def ordinal(n):
    return "%d%s" % (n,"tsnrhtdd"[((n//10%10!=1)*(n%10<4)*n%10)::4])

def parse_date(timestamp_str: str):
    # Parse the timestamp string into a datetime object
    timestamp = datetime.datetime.fromisoformat(timestamp_str)

    # Convert the timestamp to Eastern Standard Time (EST)
    est_timezone = pytz.timezone('America/New_York')
    timestamp_est = timestamp.astimezone(est_timezone)

    # Format the timestamp into a more readable format including the timezone
    day_with_ordinal = ordinal(timestamp_est.day)
    readable_format_with_timezone = timestamp_est.strftime(f"%A, %B {day_with_ordinal}, %Y, %H:%M %Z")

    return readable_format_with_timezone



if __name__ == "__main__":
    # Test the function with a sample timestamp
    timestamp_str = "2022-03-21T12:00:00"
    print(parse_date(timestamp_str))