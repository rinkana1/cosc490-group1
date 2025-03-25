### Imports
import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    """
    Used to track the time elapsed from the beginning of a process

    Attributes:
        _start_time (float | None): The start time value of the timer.
    """

    def __init__(self):
        """Initializes a Timer object."""
        self._start_time = None

    # Start a new timer
    def start(self):
        """Sets the _start_time variable to the current value of time.perf_counter()."""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def format_time(self, seconds: float = 0.0) -> str:
        """
        Formats the elapsed time to make it more easily read

        Args:
            seconds (float): The amount of seconds that must be formatted.
        
        Returns:
            A string with the formatted version of the time.

            For example, a value of of 5430 would be formatted as `1 hrs 30 mins 30 secs`.
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60

        if hours > 0:
            return f"{hours} hrs {minutes} mins {seconds:.3f} secs"
        elif minutes > 0:
            return f"{minutes} mins {seconds:.3f} secs"
        else:
            return f"{seconds:.3f} secs"
    
    # Return the current elapsed time
    def get_elapsed_time(self) -> str:
        """
        Calculates and returns the elapsed time. Does not change _start_time.

        Returns:
            A string with the elapsed time.

        Raises:
            TimerError: Timer is not running. Use .start() to start it
        """
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        
        elapsed_time = time.perf_counter() - self._start_time

        return self.format_time(elapsed_time)
        
    # Stop the timer, and return the elapsed time
    def stop(self) -> str:
        """
        Calculates and returns the elapsed time. Also sets _start_time to None

        Returns:
            A string with the elapsed time.
        
        Raises:
            TimerError: Timer is not running. Use .start() to start it
        """
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        return self.format_time(elapsed_time)