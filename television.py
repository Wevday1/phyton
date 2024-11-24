class Television:
    """
    A class to represent a television that can be powered on/off,
    change channels, adjust volume, and toggle mute.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a new Television object with default settings.
        """
        self.__status: bool = False  # TV is off by default
        self.__muted: bool = False  # TV is not muted by default
        self.__volume: int = Television.MIN_VOLUME  # Default volume is the minimum
        self.__channel: int = Television.MIN_CHANNEL  # Default channel is the minimum
        self.__previous_volume: int = Television.MIN_VOLUME  # To store volume before muting

    def power(self) -> None:
        """
        Toggles the power state of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute state of the television.
        """
        if self.__status:  # Only if the TV is on
            if not self.__muted:
                self.__previous_volume = self.__volume  # Store current volume
                self.__volume = Television.MIN_VOLUME  # Set volume to 0 when muted
                self.__muted = True
            else:
                self.__volume = self.__previous_volume  # Restore previous volume
                self.__muted = False

    def channel_up(self) -> None:
        """
        Increments the channel by 1, with wrap-around to the minimum channel
        if the maximum channel is exceeded.
        """
        if self.__status:  # Only if the TV is on
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrements the channel by 1, with wrap-around to the maximum channel
        if the minimum channel is undercut.
        """
        if self.__status:  # Only if the TV is on
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increments the volume by 1, up to the maximum volume.
        Unmutes the television if it is muted.
        """
        if self.__status:  # Only if the TV is on
            if self.__muted:  # Unmute if muted
                self.__muted = False
                self.__volume = self.__previous_volume  # Restore previous volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrements the volume by 1, down to the minimum volume.
        Unmutes the television if it is muted.
        """
        if self.__status:  # Only if the TV is on
            if self.__muted:  # Unmute if muted
                self.__muted = False
                self.__volume = self.__previous_volume  # Restore previous volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns the current state of the television as a string.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
