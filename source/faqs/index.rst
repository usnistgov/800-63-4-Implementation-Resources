Frequently asked questions
===========================

.. container:: faq-meta

  Answers from the NIST Digital Identity Group. Last updated 30 September 2026.

Direct answers to the questions we hear most from agencies and CSPs implementing
SP 800-63 Revision 4. Use the search in the sidebar to jump to a specific term,
or pick a volume below.

.. container:: faq-toc

  **Jump to a volume**

  :ref:`SP 800-63 - Revision 4 <sp-800-63>` :ref:`SP 800-63A - Identity proofing <sp-800-63a>`  :ref:`SP 800-63B - Authentication <sp-800-63b>`  :ref:`SP 800-63C - Federation <sp-800-63c>`  :ref:`General and cross-volume <general>`


.. _sp-800-63:

SP 800-63 - Revision 4
----------------------

.. faq-entry:: Does a CSP have to perform a Digital Identity Risk Management (DIRM) process? 

  **A:** CSPs and IdPs are expected to offer services at assurance levels that are requested by the RPs they serve. However, CSPs and IdPs that choose to deviate from this guideline or augment their services (including when supplemental or compensating controls are added) are expected to conduct an abbreviated digital identity risk assessment and document their modifications in a Digital Identity Acceptance Statement (DIAS) that is provided to RPs (see Sec. 3.4.4). 
  
  RPs use the DIAS provided by a CSP or IdP to determine whether the xALs offered as well as any tailoring and related deviations are acceptable for the intended functionality of RP's online service and the user populations that it serves.  

.. faq-entry:: How do we ensure that tailoring of the xALs and related controls does not adversely impact interoperability between CSPs and RPs?

  **A:** When CSPs and IdPs tailor the xALs for the services they offer or otherwise deviate from the normative guidance, they are expected to prepare a DIAS to document their claimed xALs, related controls, and rationale for any deviations from normative guidance. This should include all supplemental and compensating controls that are implemented. As a result, DIASs can serve as a starting point for trust agreements and risk-based decision-making when RPs are considering entering a federated relationship with CSPs. 
  
  Tailoring is a common practice already used by most agencies. NIST SP 800-63-4 provides a framework, structure, and output to help agencies apply and document tailoring consistently. This allows agencies to meet the security, privacy, and customer experience needs of the services, populations, and use cases they support, while providing a clear starting point for federation determinations.

.. faq-entry:: What metrics should we focus on for continuous monitoring and fraud prevention?

  **A:** See Table 4. Performance Metrics in the NIST SP 800-63-4 base volume for recommended metrics. As part of a continuous evaluation and improvement program, these metrics can be used as is, tailored, or supplemented as determined appropriate for the given organization or use cases. It is also worth noting that organizations may require internal discussions, approvals, and governance to access the data as it may not all reside with a single source or organization. What metrics are collected, what performance thresholds are set, and reporting mechanisms (e.g., automated v. manual) should all be part of each organization's plan to implement and mature an continuous improvement program.


.. _sp-800-63a:

SP 800-63A - Identity proofing and enrollment
---------------------------------------------

.. faq-entry:: What are core attributes and what should a CSP consider when determining its set of core attributes? Why doesn't NIST provide a list of minimum required core attributes?

   **A:** Revision 4 of SP 800-63A introduces the concept of core attributes and defines them as
   "the set of identity attributes that the CSP has determined and documented to be required for
   identity proofing and [to] provide services." This provided a mechanism to allow for CSPs and
   RPs to know which attributes are critical to achieving the goals of resolution, validation, and
   verification as well as necessary for service delivery. This also avoided overly generic
   requirements such as "shall validate all biographic information" when much of that data is not
   useful to online uses of identity (e.g., height, weight, eye color).

   When determining which attributes to include in its set of core attributes, a CSP should
   consider:

   - The evidence collection requirements for the IALs it offers.
   - Additional attributes it needs to accomplish resolution, validation, and identity verification
     at these IALs.
   - Additional attributes required for fraud detection, if applicable.
   - Attributes that will be stored in the subscriber accounts for ongoing operations of the
     identity service and, if applicable, will be shared with RPs and federated partners.

   To provide CSPs with the greatest amount of flexibility in designing and implementing their
   identity services, only mandates the collection of a government identifier within the Core
   Attributes. This is mandated to support identity resolution within government systems that are
   highly dependent on government identifiers to support linking of users with their data spread
   across numerous systems. In addition to the government identifier, section 2.2 provides a set of
   recommended attributes for identity proofing and enrollment processes. These include name, date
   of birth, and a physical address. A CSP may choose to include all or some of these recommended
   attributes depending on the needs of the RPs they serve. They may also expand the attributes
   they define as "core" based on their RP needs.

   However, in keeping with good privacy risk management practices, a CSP should limit its set of
   core attributes to the minimum needed to conduct its identity service operations, as documented
   in its practices statement. CSPs that collect and process attributes beyond what it determines to
   be its core attributes must do so in alignment with the privacy requirements provided in section
   3.3.

.. faq-entry:: What is the difference between authoritative and credible sources? What are some examples of authoritative and credible sources?

   **A:** Authoritative sources are organizations that issue evidence and attributes, or
   third-party organizations that have direct access to the issuing source of such evidence and
   associated attributes. Direct access implies that a non-issuing source have access to up-to-date
   attributes and status information about evidence.

   Examples of authoritative sources of identity evidence are state DMVs for driver's licenses,
   The US State Department of Passports, and SSA for Social Security Numbers and associated data.
   Examples of authoritative sources that are not issuers but maintain direct access to issuing
   source data include:

   - The American Association of Motor Vehicle Administrators (AAMVA) whose License Data
     Verification System (DLDV) provides mediated access to participating state DMV data.
   - Entities that participate in the Social Security Administrations Electronic Consent Based
     Social Security Number Verification program. Such organizations can query the SSA's data set
     directly for social security number data.

   A credible source has access to attribute information that can be traced to an authoritative
   source or maintains identity attribute information obtained from multiple sources that is
   correlated for accuracy, consistency, and currency. Examples of credible sources include credit
   bureaus, such as TransUnion, Equifax, and Experian, and data services such as LexisNexis.

.. faq-entry:: Must CSPs offer Trusted Referee services to be certified?

   **A:** First, NIST does not run or operate a certification program, and the final version of
   the Digital Identity Guidelines only recommends that CSPs offer Trusted Referee services.
   Trusted Referees represent a critical capability that helps deal with the inevitable exception
   cases that large scale online services must be prepared to address. For this reason, we
   recommend that these resources are made available to enable more effective deployment of
   solutions that can support a larger customer base.

   That said, the CSP doesn't need to be the sole provider of these resources. In fact, in many
   cases the RP is better positioned to provide these services due to pre-existing customer
   relationships, physical locations, and customer outreach capabilities. RPs are therefore
   encouraged to consider how they can address Trusted Referee capabilities in conjunction with
   their support CSPs. Additionally, these services could be offered by trusted third parties such
   as notaries or similar organizations.

   Trusted Referees are not required, though we encourage all participants of the ecosystem to
   explore mechanisms and collaborations to enable secure and accessible exception handling,
   including Trusted Referee services.


.. _sp-800-63b:

SP 800-63B - Authentication
---------------------------

.. faq-entry:: What are the important new password requirements in SP 800-63B-4?

   **A:** As compared with the requirements for passwords (referred to as memorized secrets) in
   the previous document revision (SP 800-63B), the following new requirements have been included:

   - Minimum password length of 15 characters for passwords being used as a single authentication
     factor at AAL1 (increased from 8 characters).
   - Composition rules (e.g., requirements for certain classes of characters in passwords) are not
     to be used. They were previously discouraged but allowed.
   - Separate requirements for PINs that the CSP randomly selects have been eliminated. They are
     replaced by new requirements for activation secrets (see below).
   - Routine periodic password changes are not to be required. They were previously discouraged but
     allowed.
   - Specific key derivation (hashing) algorithms are no longer listed because the requirements
     for password verifier storage change quickly. The use of NIST-approved algorithms is
     encouraged.

.. faq-entry:: What is the guideline's position on the use of password managers?

   **A:** SP 800-63B-4 requires verifiers to allow the use of password managers and autofill
   functionality. The use of well-designed password managers encourages the use of complex
   passwords that are unique to each service, providing protection against password guessing,
   cracking, and "spraying" attacks.

   The use of password form elements on web pages allows password managers to automatically fill in
   stored passwords without exposing them via the clipboard. 63B also recommends that applications
   and web pages allow copy-paste functionality to accommodate users who use other tools to store
   passwords.

.. faq-entry:: What are activation factors?

   **A:** Activation factors are a new concept in SP 800-63B-4. An activation factor is a second
   authentication factor that is locally verified on the authenticator or endpoint (e.g., your
   phone). When successfully verified, the activation factor provides access to an authentication
   key in the possession of the subscriber.

   There are two classes of activation factors. Activation secrets are passwords or PINs that are
   verified on the authenticator or endpoint. Biometric activation uses a locally verified
   biometric comparison to obtain access to the authentication key.

   Because the threats at the user endpoint are different from those at the CSP/verifier, the
   requirements for activation secrets differ somewhat from centrally verified passwords - for
   example they can be substantially shorter (4 characters rather than 8 or 15).

.. faq-entry:: What are the requirements for activation factors?

   **A:** Activation secrets are required to be at least four characters in length but are
   encouraged to be at least six characters. Because of the shorter minimum length as compared with
   passwords, a maximum of only ten consecutive incorrect entries of the activation secret are
   permitted before the authenticator is disabled.

   Biometric activation shares the general requirements for biometric comparison in authentication.
   Local comparison of biometrics is recommended over central verification because tight integration
   between the biometric sensor and verifier minimizes the potential for biometric injection
   attacks.


.. _sp-800-63c:

SP 800-63C - Federation
-----------------------

.. faq-entry:: What is the difference between Holder-of-Key and Bound Authenticators?

   **A:** A Holder-of-Key (HoK) assertion uses a single cryptographic authenticator known to both
   the Identity Provider (IdP) and the Relying Party (RP), whereas a Bound Authenticator is managed
   and verified solely by the RP.

   FAL3 requires additional confidence that the individual requesting access to a resource at an RP
   is the same individual who authenticated to the IdP.

   This can be achieved by the RP directly authenticating the user after the IdP's assertion, using
   either a HoK assertion or a bound authenticator.

   If HoK is used, the assertion from the IdP will contain the public key of a public-private key
   pair controlled by the subscriber. For example, if the subscriber has a PIV card, the public key
   of the PIV Authentication Certificate can be included in the assertion, allowing the RP to use
   that public key to issue a challenge to the subscriber, who will respond using the associated
   private key.

   If a bound authenticator is used, the IdP's assertion indicates that additional authentication is
   required at the RP but does not specify the authenticator. Instead, the RP binds a unique
   phishing-resistant authenticator to the RP subscriber account and manages it. The subscriber then
   proves possession of that authenticator to the RP when accessing a resource that requires FAL3.

.. faq-entry:: Is PIV login FAL3?

   **A:** No, PIV credentials are used for direct authentication, so on their own, do not meet the
   requirements for federated login. To create a federated assertion that utilizes a PIV Card, the
   PIV can be used to authenticate to an Identity Provider (IdP), which then creates a unique and
   time-limited assertion that is provided to a Relying Party (RP). Where permitted by the IdP-RP
   trust agreement, this assertion may include attributes that are not present on the PIV card
   itself, such as authorization attributes.

   While the PIV card is an AAL3 authenticator, most federated assertions that utilize a PIV Card
   will not require FAL3. A DIRA (Digital Identity Risk Assessment) should be conducted to determine
   whether FAL3 is required for a particular transaction or if FAL2 is sufficient. FAL3 is required
   only for the highest risk category of transactions.

   Additional guidance for PIV Federation is found in SP 800-217, PIV Federation.

.. faq-entry:: Can an mDL be used as a credential? If so, what are the IALs, AALs, and FALs for an mDL?

   **A:** Yes, an mDL can be used as a credential when presented over a federation protocol, with
   xALs that vary depending on use case and circumstances.

   NIST SP 800-63-4 introduces a new federation model, subscriber-controlled wallets. The CSP
   issues signed attribute bundles directly to the subscriber. Those attribute bundles are held in
   subscriber-controlled wallets that can act as an IdP. The subscriber authenticates to the wallet
   by presenting an activation factor, and the wallet presents the signed attribute bundle to the RP
   in an assertion. The RP can then verify both the assertion and the signed attribute bundle. For
   the mDL model, the mDoc is the signed attribute bundle, and the wallet's assertion is the
   presentation of that bundle to the RP.

   ISO/IEC 18013-5 compliant mDLs are considered digital evidence in the context of NIST SP
   800-63A. When mDLs are signed by the issuer, cryptographically bound to the device, and contain
   the same attributes as physical licenses, they qualify as superior evidence, which can support
   IAL1, IAL2, and IAL3 workflows.

   However, since xALs depend on several factors, the IAL, AAL, and FAL of an mDL presentation can
   vary depending on the application and ecosystem in which it is used.


.. _general:

General and cross-volume
------------------------

No cross-volume FAQs are posted yet.
