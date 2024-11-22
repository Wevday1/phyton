import pytest
from television import Television

def test_init():
    # Test the initialization of the Television class
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    # Test the power toggle functionality
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    # Test mute and unmute functionality
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()  # Volume is now 2
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Muted
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"  # Unmuted

def test_channel_up():
    # Test channel up functionality with wrap-around
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Wrap-around

def test_channel_down():
    # Test channel down functionality with wrap-around
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"  # Wrap-around
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"

def test_volume_up():
    # Test volume up functionality with limits
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"  # Max volume limit

def test_volume_down():
    # Test volume down functionality with limits
    tv = Television()
    tv.power()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Min volume limit
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_mute_with_volume_change():
    # Test muting and changing volume while muted
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Muted
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Unmuted and volume restored
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"  # Max volume

def test_channel_change_with_power_off():
    # Test that channel and volume cannot change when TV is off
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # No change
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # No change
