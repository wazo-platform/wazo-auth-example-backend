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

import logging

from collections import namedtuple

logger = logging.getLogger(__name__)
User = namedtuple('User', ['username', 'password', 'uuid'])


class ExampleBackend(object):
    """
    A simple backend implementing the authentication for a static user list
    define in the constructor.

    This is a toy example but the same logic would apply to a plugin searching
    an ldap server or querying an other external service.
    """

    def __init__(self, configuration):
        """
        Does any initialisation that is required for this backend to work
        properly. The process configuration is received as the only argument.
        """
        logger.warning('example backend is enabled and should NOT be used in production')
        self._users = {
            'alice': User('alice', 's3cre7', '63f3dc3c-865d-419e-bec2-e18c4b118224'),
            'bob': User('bob', 'abc123', '6a6fb854-d2b3-4911-a0e2-d6de4b9030d4'),
            'charlie': User('charlie', 'lovecat', '02d94074-4f99-42ec-9df7-51b6765185ac'),
        }

    def get_acls(self, username, args):
        """
        Returns the ACLs for this user
        """
        return []

    def get_ids(self, username, args):
        """Finds the unique identifier for this user.

        Since this backend cannot know about xivo users uuid, it returns None
        as the second element of the tuple.

        Returns the tuple (identifier, None)
        """
        return self._users[username].uuid, None

    def verify_password(self, username, password, args):
        """Checks if a username/password combination matches, return True or False"""
        try:
            return self._users[username].password == password
        except KeyError:
            return False
