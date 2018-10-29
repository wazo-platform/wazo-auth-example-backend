# -*- coding: utf-8 -*-
#
# Copyright 2015-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from collections import namedtuple
from wazo_auth import BaseAuthenticationBackend

logger = logging.getLogger(__name__)
User = namedtuple('User', ['username', 'password', 'uuid'])


class ExampleBackend(BaseAuthenticationBackend):
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
        # args['metadata'] can be used here to generate ACLs
        return []

    def get_metadata(self, username, args):
        """
        returns information concerning this user that will be included in the user's
        token metadata.

        metadatas can also be used to render ACLs.
        """
        # Using the BaseAuthenticationBackend will set the following values in the
        # metadata. "xivo_user_uuid" = None, "auth_id" = None, "username" = username
        # "xivo_uuid" = the value of the XIVO_UUID environment variable.
        # These fields should be in the metadata if the you do not wish to use
        # inheritance.
        metadata = super(ExampleBackend, self).get_metadata(username, args)
        metadata['auth_id'] = self._users['username'].uuid
        return metadata

    def verify_password(self, username, password, args):
        """Checks if a username/password combination matches, return True or False"""
        try:
            return self._users[username].password == password
        except KeyError:
            return False
