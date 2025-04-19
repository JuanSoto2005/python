import pytest
from television import Television


def tv():
    return Television()


def test_init(tv):
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"


def test_power(tv):
    tv.power()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"


def test_mute(tv):
    tv.mute()
    assert not tv._Television__muted

    tv.power()
    tv.mute()
    assert tv._Television__muted
    tv.mute()
    assert not tv._Television__muted


def test_channel_up(tv):
    tv.channel_up()
    assert tv._Television__channel == 0

    tv.power()
    tv.channel_up()
    assert tv._Television__channel == 1
    tv.channel_up()
    tv.channel_up()
    assert tv._Television__channel == 3
    tv.channel_up()
    assert tv._Television__channel == 0


def test_channel_down(tv):
    tv.channel_down()
    assert tv._Television__channel == 0

    tv.power()
    tv.channel_down()
    assert tv._Television__channel == 3
    tv.channel_down()
    assert tv._Television__channel == 2


def test_volume_up(tv):
    tv.volume_up()
    assert tv._Television__volume == 0

    tv.power()
    tv.volume_up()
    assert tv._Television__volume == 1
    tv.volume_up()
    assert tv._Television__volume == 2
    tv.volume_up()
    assert tv._Television__volume == 2

    tv.mute()
    tv.volume_up()
    assert not tv._Television__muted
    assert tv._Television__volume == 2


def test_volume_down(tv):
    tv.volume_down()
    assert tv._Television__volume == 0

    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 1
    tv.volume_down()
    assert tv._Television__volume == 0
    tv.volume_down()
    assert tv._Television__volume == 0

    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert not tv._Television__muted
    assert tv._Television__volume == 0