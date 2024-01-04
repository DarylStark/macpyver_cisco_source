"""Tests for the CiscoSource class."""
# pylint: disable=protected-access

import pytest
from macpyver_core import Software

from macpyver_cisco_source import CiscoSource


@pytest.mark.parametrize(
    'client_key, client_secret',
    [
        ['key', 'secret'],
        ['lksjfsldfjsdlfkj', 'pqpweuqoweiuwqi']
    ])
def test_set_credentials(
        client_key: str,
        client_secret: str) -> None:
    """Test if we can set credentials.

    Args:
        client_key: the key to test.
        client_secret: the secret to test.
    """
    CiscoSource.set_credentials(
        client_key=client_key,
        client_secret=client_secret
    )
    assert CiscoSource._client_key == client_key
    assert CiscoSource._client_secret == client_secret


@pytest.mark.parametrize(
    'date, expected_date',
    [
        ['26-Oct-1986', (1986, 10, 26)],
        ['16-Sep-1988', (1988, 9, 16)],
        ['20-Jan-2022', (2022, 1, 20)],
    ])
def test_convert_cisco_datetime_to_datetime(
        software: Software,
        date: str,
        expected_date: tuple[int, int, int]) -> None:
    """Test if we can convert a datetime from Cisco to a Python Datetime.

    Args:
        software: a Software object to use in testing.
        date: the Cisco date to convert.
        expected_date: a tuple with year, month and day to expect.
    """
    source = CiscoSource(software=software)
    datetime_obj = source._convert_cisco_datetime_to_datetime(
        date)
    assert datetime_obj.year == expected_date[0]
    assert datetime_obj.month == expected_date[1]
    assert datetime_obj.day == expected_date[2]
