# ldap configurations
ldap_enable = False

if ldap_enable:
    ldap_port = config.get('ldap', 'ldap_port')

    if ldap_port:
        ldap_server = config.get('ldap', 'ldap_server') + ":" + ldap_port
    else:
        ldap_server = config.get('ldap', 'ldap_server')

    base_dn = config.get('ldap', 'base_dn')
    ldap_manager = config.get('ldap', 'ldap_manager')
    ldap_password = config.get('ldap', 'ldap_password')
    ldap_filter = config.get('ldap', 'ldap_filter')
    if ldap_filter == "OpenLDAP":
        ldap_filter = '(uid=%(user)s)'
    else:
        ldap_filter = '(sAMAccountName=%(user)s)'

    AUTH_LDAP_SERVER_URI = ldap_server

    AUTH_LDAP_BIND_DN = ldap_manager
    AUTH_LDAP_BIND_PASSWORD = ldap_password
    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        base_dn,
        ldap.SCOPE_SUBTREE,
        ldap_filter,
    )
    # Or:
    # AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=users,dc=example,dc=com'

    # Set up the basic group parameters.
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
        base_dn,
        ldap.SCOPE_SUBTREE,
        # '(objectClass=posixGroup)',
        '(objectClass=*)',
    )
    AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr='cn')
    #
    # # Simple group restrictions
    require_group = config.get('ldap', 'require_group')
    nickname = config.get('ldap', 'nickname')
    is_active = config.get('ldap', 'is_active')
    is_superuser = config.get('ldap', 'is_superuser')
    if require_group:
        # AUTH_LDAP_REQUIRE_GROUP = 'cn=enable,ou=scimall,dc=gldap,dc=com'
        AUTH_LDAP_REQUIRE_GROUP = require_group
    # AUTH_LDAP_DENY_GROUP = 'cn=disabled,ou=django,ou=groups,dc=example,dc=com'

    # Populate the Django user from the LDAP directory.
    if not nickname:
        nickname = 'cn'
    AUTH_LDAP_USER_ATTR_MAP = {
        # 'first_name': 'givenName',
        # 'last_name': 'sn',
        'nickname': nickname,
        'email': 'mail',
        'ldap_name': 'cn',
    }

    if is_active and not is_superuser:
        AUTH_LDAP_USER_FLAGS_BY_GROUP = {
            'is_active': is_active,
        }
    elif is_superuser and not is_active:
        AUTH_LDAP_USER_FLAGS_BY_GROUP = {
            'is_superuser': is_superuser,
        }
    elif is_active and is_superuser:
        AUTH_LDAP_USER_FLAGS_BY_GROUP = {
            'is_active': is_active,
            'is_superuser': is_superuser,
        }

    # This is the default, but I like to be explicit.
    AUTH_LDAP_ALWAYS_UPDATE_USER = True

    # Use LDAP group membership to calculate group permissions.
    # AUTH_LDAP_FIND_GROUP_PERMS = True

    # Cache distinguised names and group memberships for an hour to minimize
    # LDAP traffic.

    AUTH_LDAP_CACHE_TIMEOUT = 60
    # Keep ModelBackend around for per-user permissions and maybe a local
    # superuser.
    AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
