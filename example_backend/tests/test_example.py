# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Avencall
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import unittest

from hamcrest import assert_that, equal_to, is_

from ..example import ExampleBackend


class TestExample(unittest.TestCase):

    def test_verify_password(self):
        backend = ExampleBackend({})

        matching = backend.verify_password('alice', 's3cre7', {})
        not_matching = backend.verify_password('charlie', 'catlove', {})

        assert_that(matching, is_(True))
        assert_that(not_matching, is_(False))

    def test_get_uuid(self):
        backend = ExampleBackend({})

        uuid = backend.get_ids('bob', {})

        assert_that(uuid, equal_to(('6a6fb854-d2b3-4911-a0e2-d6de4b9030d4', None)))

    def test_get_consul_acls(self):
        backend = ExampleBackend({})

        acls = backend.get_consul_acls('bob', {})
        rule = 'path/to/give/token/access/{identifier}'.format(identifier='6a6fb854-d2b3-4911-a0e2-d6de4b9030d4')
        assert_that(acls, equal_to(([{'rule': rule, 'policy': 'write'}])))
