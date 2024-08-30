# LitLyx Sender

LitLyx Sender is a [Python library](https://pypi.org/project/litlyx-sender/) for easily sending events to the [LitLyx](https://litlyx.com) platform.

## Installation

You can install LitLyx Sender using pip:

```
pip install litlyx-sender
```

## Usage

Here's a basic example of how to use LitLyx Sender:

```python
from litlyx_sender import LitLyxSender

# Create a sender instance
sender = LitLyxSender()

# Send a simple event
sender.send_event(name="test_event", metadata={"test": "value"})

# Use the decorator
@sender.event_decorator(name="decorated_event", metadata={"decorated": True})
def example_function():
    print("This is an example function.")

example_function()
```

## Configuration

You can configure the LitLyxSender with custom default values:

```python
sender = LitLyxSender(
    url="https://custom.litlyx.com/event",
    default_pid="custom_pid",
    default_name="custom_event",
    default_metadata={"custom": "metadata"},
    default_website="custom.website.com",
    default_user_agent="CustomApp/1.0"
)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
