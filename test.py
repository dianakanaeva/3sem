import unittest
from main import *

class TestProgram(unittest.TestCase):
    def setUp(self):
        self.PCs = [
            PC(1, "DDR4-2400", 4),
            PC(2, "DDR3-1600", 8),
            PC(3, "DDR4-3200", 6),
            PC(4, "DDR3-1866", 4),
            PC(5, "DDR4-2666", 12)
        ]

        self.HDs = [
            HardDrive(1, "1TB", "HDD-1TB"),
            HardDrive(2, "500GB", "SSD-500GB"),
            HardDrive(3, "1TB",  "NVMe-1TB"),
            HardDrive(4, "2TB", "SATA-2TB"),
            HardDrive(5, "2TB", "SSHD-2TB"),
            HardDrive(6, "1TB", "SSD-1TB"),
            HardDrive(7, "2TB", "HDD-2TB"),
            HardDrive(8, "500GB", "NVMe-500GB")
        ]

        self.PC_HDs = [
            PC_HD(1, 1),
            PC_HD(1, 8),
            PC_HD(2, 2),
            PC_HD(2, 6),
            PC_HD(3, 4),
            PC_HD(3, 5),
            PC_HD(4, 3),
            PC_HD(5, 7)
        ]

    def test_1(self):
        expected_result = [
            ('HDD-1TB', '1TB', 'DDR4-2400', 4),
            ('HDD-2TB', '2TB', 'DDR4-2666', 12),
            ('NVMe-1TB', '1TB', 'DDR3-1866', 4),
            ('NVMe-500GB', '500GB', 'DDR4-2400', 4),
            ('SATA-2TB', '2TB', 'DDR4-3200', 6),
            ('SSD-1TB', '1TB', 'DDR3-1600', 8),
            ('SSD-500GB', '500GB', 'DDR3-1600', 8),
            ('SSHD-2TB', '2TB', 'DDR4-3200', 6)
        ]
        result = b1_solution(self.HDs, self.PCs, self.PC_HDs)
        self.assertEqual(result, expected_result)

    def test_2(self):
        expected_result = [
            ('DDR3-1866', 4, 1),
            ('DDR4-2666', 12, 1),
            ('DDR4-2400', 4, 2),
            ('DDR3-1600', 8, 2),
            ('DDR4-3200', 6, 2)
        ]
        result = b2_solution(self.PCs, self.PC_HDs)
        self.assertEqual(result, expected_result)

    def test_3(self):
        expected_result = [
            ('HDD-1TB', 'DDR4-2400'),
            ('NVMe-1TB', 'DDR3-1866'),
            ('SSD-1TB', 'DDR3-1600')
        ]
        result = b3_solution(self.HDs, self.PCs, self.PC_HDs)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()