# Wazo auth example backend

[![Build Status](https://travis-ci.org/wazo-pbx/wazo-auth-example-backend.svg)](https://travis-ci.org/wazo-pbx/wazo-auth-example-backend)

this is an example implementation of a wazo-auth plugin. It should _NEVER_ be used in production
as the username and password combination are public and will result in a valid wazo-auth token
being issued.

## Installation

```sh
cd wazo-auth-example-backend
python setup.py install
```

## Enabling the plugin

```sh
cat << EOF > /etc/wazo-auth/conf.d/enable_example.yml
enabled_backend_plugins:
    example: true
EOF
systemctl restart wazo-auth
```

## Disabling the plugin

```sh
rm -f /etc/wazo-auth/conf.d/enable_example.yml
systemctl restart wazo-auth
```
