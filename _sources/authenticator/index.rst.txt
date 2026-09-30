Authenticator Examples
======================

.. role:: auth-badge-yes
   :class: auth-status auth-status-yes

.. role:: auth-badge-no
   :class: auth-status auth-status-no

.. container:: authenticator-table-wrap

   .. rst-class:: authenticator-examples-table

   .. list-table::
      :header-rows: 1
      :widths: 18 34 24 12 12

      * - Authenticator Type
        - Description
        - Examples
        - Replay Resistant?
        - Supports Phishing Resistance?
      * - `Password <https://pages.nist.gov/800-63-4/sp800-63b.html#password>`__
        - Memorizable secret (something you know) used for repeated authentications
        - * Password
          * Passphrase
        - :auth-badge-no:`No`
        - :auth-badge-no:`No`
      * - `Look-up secret <https://pages.nist.gov/800-63-4/sp800-63b.html#lookupsecrets>`__
        - One-time authentication secret, typically printed for later use by subscriber
        - * Printed one-time passwords
          * Grid cards
        - :auth-badge-yes:`Yes`
        - :auth-badge-no:`No`
      * - `Out-of-band device <https://pages.nist.gov/800-63-4/sp800-63b.html#out-of-band>`__
        - Device having a communication channel independent of the authentication session through which an authentiction secret is conveyed
        - * SMS
          * Push notification
        - :auth-badge-yes:`Yes`
        - :auth-badge-no:`No`
      * - `Single-factor OTP <https://pages.nist.gov/800-63-4/sp800-63b.html#singlefactorOTP>`__
        - Device or application that generates a single-use authentication secret
        - * TOTP hardware device (e.g., SecureID)
          * TOTP smartphone app (e.g., Google Authenticator)
        - :auth-badge-yes:`Yes`
        - :auth-badge-no:`No`
      * - `Multi-factor OTP <https://pages.nist.gov/800-63-4/sp800-63b.html#multifactorOTP>`__
        - Device or application that generates a single-use authentication secret when provided with a memorized or biometric activation factor
        - * OTP hardware device with PIN keypad
        - :auth-badge-yes:`Yes`
        - :auth-badge-no:`No`
      * - `Single-factor cryptographic <https://pages.nist.gov/800-63-4/sp800-63b.html#sfc>`__
        - Device or application that generates a cryptographically computed response to a challenge nonce from the verifier
        - * FIDO U2F
          * Client certificate
          * Smartcards
          * Passkeys (without user verification)
        - :auth-badge-yes:`Yes`
        - :auth-badge-yes:`Yes`
      * - `Multi-factor cryptographic <https://pages.nist.gov/800-63-4/sp800-63b.html#mfc>`__
        - Device or application that generates a cryptographically computed response to a challenge nonce from the verifier when provided with a memorized or biometric activation factor
        - * FIDO2 passkeys with user verification
          * Client certificate with unlock secret
          * PIV
          * CAC
          * PIV-I
        - :auth-badge-yes:`Yes`
        - :auth-badge-yes:`Yes`

Community Resources
-------------------

.. grid:: 1 1 2 2
   :class-container: scw-card-grid scw-resources-grid
   :gutter: 2

   .. grid-item-card::
      :class-card: scw-card scw-resource-card

      **Passkeys Developer Site:** `<https://passkeys.dev/>`__

   .. grid-item-card::
      :class-card: scw-card scw-resource-card

      **What Are Passkeys:** `<https://whatarepasskeys.info/en/>`__

.. container:: community-resources-disclaimer

   **Representations and Warranties**

   Certain commercial entities, equipment, or materials may be identified in this Web site or linked Web sites in order to support Framework understanding and use. Such identification is not intended to imply recommendation or endorsement by NIST, nor is it intended to imply that the entities, materials, or equipment are necessarily the best available for the purpose.
