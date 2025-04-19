class Television:
    """
    A class which represents a television with basic functions such as power,
    volume, channel control, and mute.
    Class Constants:
        MIN_VOLUME (int): Minimum volume level (0)
        MAX_VOLUME (int): Maximum volume level (2)
        MIN_CHANNEL (int): Minimum channel number (0)
        MAX_CHANNEL (int): Maximum channel number (3
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """ Start the Television with defualt values:
            - Power status: Off (False)
            - Muted status: Unmuted (False)
            - Volume: MIN_VOLUME (0)
            - Channel: MIN_CHANNEL (0)
        """

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """ Toggle for the Television power state, On (True) and Off (False)
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """ Toggle for the mute state if the television is powered on.
        When mute is toggled, volume will be set to 0. Unmuting changes
        back to the previous volume.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """ Increse channel by 1
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """ Decreases channel by 1
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """ Increases volume by 1 up to MAX_VOLUME.
        Unmutes if currently muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """ Decreases volume by 1 down to MIN_VOLUME.
        Unmutes if currently muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a formatted string representation of the television's state.

        Returns:
            str: String in format "Power = [status], Channel = [channel], Volume = [volume]"
                 Shows volume as 0 when muted (regardless of actual volume).
        """
        return f"Power = {'On' if self.__status else 'Off'}, Channel = {self.__channel}, Volume = {self.__volume}"