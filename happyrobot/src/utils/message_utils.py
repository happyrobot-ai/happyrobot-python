from copy import deepcopy


def combine_messages(messages: list[dict]) -> list[dict]:
    new_messages: list[dict] = []
    tracking_message: dict = None

    for message in messages:
        if tracking_message:
            # If the new message has the same role as the tracking,
            # add the content and continue
            if message["role"] == tracking_message["role"]:
                tracking_message["content"] += " " + message["content"]
                if "tool_calls" in tracking_message:
                    if tracking_message["tool_calls"] is None:
                        tracking_message["tool_calls"] = []
                    assert tracking_message["tool_calls"] is not None, message
                    tool_calls = message.get("tool_calls", [])
                    if tool_calls is not None:
                        tracking_message["tool_calls"].extend(tool_calls)
                elif "tool_calls" in message:
                    tracking_message["tool_calls"] = message["tool_calls"]
                continue

            # Otherwise, add the traking to the list of messages
            # cause the sender changed
            new_messages.append(tracking_message)

        # Set this message as the tracking message
        tracking_message = deepcopy(message)

    # Adding the last message
    if tracking_message:
        new_messages.append(tracking_message)

    return new_messages

