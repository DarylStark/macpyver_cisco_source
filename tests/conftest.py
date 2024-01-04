"""PyTest fixtures and configuration."""
# pylint: disable=too-few-public-methods

import pytest
from macpyver_core import Software


@pytest.fixture
def software() -> Software:
    """Fixture for a test Software object.

    Returns:
        A Software object to use in unit testing. contains information for the
        Cisco Source class.
    """
    return Software(
        name='IOS XE for C9500-32C',
        extra_information={
            'cisco_pid': 'C9500-32C'
        })
