SECRET_KEY = 'secret_key_for_site1'

SAML_SETTINGS = {
    'strict': True,
    'debug': True,
    'sp': {
        'entityId': 'urn:auth0:your-application-id',  # Servis sağlayıcısının kimliği
        'assertionConsumerService': {
            'url': 'http://localhost:5001/callback',  # Flask uygulamanızın SAML yanıtını alacağı URL
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
        },
        'singleLogoutService': {
            'url': 'https://localhost:5001/logout',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
        },
        'attributeConsumingService': {
            'serviceName': 'Flask SSO',
            'requestedAttributes': [
                {
                    'name': 'NameID',
                    'isRequired': True,
                }
            ],
        },
        'x509cert': '',  # Buraya SP'nin sertifikası konabilir. SP sertifikası yoksa boş bırakılabilir.
        'privateKey': '',  # Özel anahtar (opsiyonel, gerekirse eklenir)
    },
    'idp': {
        'entityId': 'urn:dev-owpabftso6evygyk.us.auth0.com',  # Auth0'nun entityID'si
        'singleSignOnService': {
            'url': 'https://dev-owpabftso6evygyk.us.auth0.com/samlp/MPaGAp8z40kyUHl78a5izZkPq1sblyI9',  # SSO URL'si
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
        },
        'singleLogoutService': {
            'url': 'https://dev-owpabftso6evygyk.us.auth0.com/samlp/MPaGAp8z40kyUHl78a5izZkPq1sblyI9/logout',
            'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
        },
        'x509cert': '''MIIDHTCCAgWgAwIBAgIJbhjL6OhtToTvMA0GCSqGSIb3DQEBCwUAMCwxKjAoBgNVBAMTIWRldi1vd3BhYmZ0c282ZXZ5Z3lrLnVzLmF1dGgwLmNvbTAeFw0yNDA5MTYwOTIwMDZaFw0zODA1MjYwOTIwMDZaMCwxKjAoBgNVBAMTIWRldi1vd3BhYmZ0c282ZXZ5Z3lrLnVzLmF1dGgwLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALYMqp6UCGsQk/8bkBexdW/gblz435UlmM9Dn0wIsybUm+Nzd31i6V4BP7ud6bDW+FajPl0JpVG/HnOQzBpxx6L9oroPiBbwxKyymHZv8WkCffndRsBAP6BnqLx8vqM+XepWoKjQc+Do40XWX3co1gk3/sOaLN7InF0QIOhUVjv43YmcopMggLHwbVRSwj5+qsEd/om5tiGvtNk1F+ln7FYE3zgew+zRThXaozPbkcflMnTEBRnjPEI3jfGG6v/gIvzzneiLqu5BNEVuyY9TiRpmzVW0c2woIAFNa76Q14Y7H3ldpAAdU4QEsRa3pY8ylidpGGctDkBhvqS4eK4aTRcCAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUcB7W9nsu4g8E6hJ19/1GfzPAANwwDgYDVR0PAQH/BAQDAgKEMA0GCSqGSIb3DQEBCwUAA4IBAQBpBvjnp6AMKP/MxNSvhI0QpveqR5mdJ0ZMd+VlFaCEfCDPLD2+E/VEO7gQeUqsPjzWY7m+q9wTOuYvtBVNTyLV+19hG/DNjttIHcan9AoiVGB+PHQ2j+JkrtT+V/t6drdsHnxXIsMtDgzHjLVNVAfvhdAOm4yJkxm/Z/FbAuJQf4XR3j0E2StYOY5OeTuJ4Kl81gmonwr7QHFRSESmytZRAD7NSPmYrO6RZjBV+rOIc576hptyI4K6//4O9lqU93Ha7CU35p4ZXyb+6TXy9rlx2O/kD6/IumzFlxGW6YgKwv3/gTI3LgRIBB4OZUMxJD0pFMDWhBBhPhtxJ+mlNGCR''',  # Auth0'nun SAML sertifikası
    }
}
