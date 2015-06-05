# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Avencall
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

from collections import namedtuple

from xivo_auth import BaseAuthenticationBackend

User = namedtuple('User', ['username', 'password', 'uuid'])


class ExampleBackend(BaseAuthenticationBackend):
    '''
    A simple backend implementing the authentification for a static user list
    define in the constructor.

    This is a toy example but the same logic would apply to a plugin searching
    an ldap server or querying an other external service.
    '''

    def __init__(self, configuration):
        '''
        Does any initialisation that is required for this backend to work
        properly. The process configuration is received as the only argument.
        '''
        super(ExampleBackend, self).__init__(configuration)
        self._users = {
            'alice': User('alice', 's3cre7', '63f3dc3c-865d-419e-bec2-e18c4b118224'),
            'bob': User('bob', 'abc123', '6a6fb854-d2b3-4911-a0e2-d6de4b9030d4'),
            'charlie': User('charlie', 'lovecat', '02d94074-4f99-42ec-9df7-51b6765185ac'),
        }

    def get_uuid(self, username):
        '''
        returns the unique id of this entry, this does not have to be a UUID.
        '''
        return self._users[username].uuid

    def verify_password(self, username, password):
        '''
        returns True of False for a given username password combination.
        '''
        try:
            return self._users[username].password == password
        except KeyError:
            return False
