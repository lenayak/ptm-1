import unittest

from tire_pressure_monitoring import Alarm


class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self) -> None:
        alarm = Alarm()
        assert not alarm.is_alarm_on
