# Copyright (C) 2019 ditekshen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class RemcosRegkeys(Signature):
    name = "remcos_regkeys"
    description = "Creates known Remcos registry keys"
    severity = 3
    categories = ["RAT"]
    families = ["Remcos"]
    authors = ["ditekshen"]
    minimum = "0.5"

    def run(self):
        remcos_keys = False
        
        indicators = [
            ".*\\\\Software\\\\Remcos-[A-Z0-9]{6}.*",
        ]

        for indicator in indicators:
            match = self.check_key(pattern=indicator, regex=True)
            if match:
                self.data.append({"Key": match})
                remcos_keys = True

        return remcos_keys