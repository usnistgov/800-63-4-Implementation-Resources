Conformance Criteria Overview
=============================

.. container:: criteria-lede

   This page provides an initial release, version 0.1, of the conformance criteria for NIST Special Publication 800-63-4 Digital Identity Guidelines. They are intended to be used by agencies and organizations seeking to evaluate products for alignment with the requirements defined in each volume of the digital identity guidelines. The versions presented here are an initial version. Any comments on the criteria can be submitted  :doc:`here </comments/index>`.

.. container:: criteria-note

   Note: NIST does not conduct certification or conformity assessment against these criteria.
   They are provided pursuant to OMB Memo 19-17: Enabling Mission Delivery through Improved Identity, Credential, and Access Management.

This set of conformance criteria presents all normative requirements and controls (SHALL statements) for the four volumes of SP 800-63 guidelines, including SP 800-63A-4 Identity Proofing and Enrollment, SP 800-63B-4 Authentication and Authenticator Management, and SP 800-63C-4 Federation and Assertions as well as the base SP 800-63-4 document itself. Recommendations (SHOULD statements) and implementation options (MAY statements) are only included where they result in further normative requirements resulting from the selection of a recommended or optional control.

Conformance Criteria Structure
------------------------------

The conformance criteria are structured in the following format:

.. rst-class:: criteria-structure-table

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Field
     - Description
   * - **Control Identifier**
     - A short unique identifier for each control.
   * - **Control name**
     - A short descriptive name for the control.
   * - **Control text**
     - Excerpt from the relevant SP 800-63-4 volume with the text of the control. (**Note:** *some of these statements have been modified slightly to allow for them to be stand-alone criteria. While wording has changed slightly, the intent and outcome of the control have not been changed*).
   * - **Objective**
     - The intended outcome of the implemented control.
   * - **Assessment method**
     - One or more candidate methods to verifying conformance with the control. Where more than one assessment method is provided, assessors may use one or both when evaluating the control implementation. Assessors are encouraged to use test methods to confirm implemented, rather than just documented, procedures. Assessors should determine what testing capabilities they have and select the assessment methods based on these capabilities.
   * - **Index**
     - Section in the relevant SP 800-63-4 volume in which the control can be found.
   * - **Target**
     - Functional element to which the control applies.
   * - **Profile/XAL Level**
     - Assurance level at which the control applies.
   * - **Discussion**
     - Additional limitations on applicability of the control, or additional information.

Conformance Criteria v0.1 Available Formats
-------------------------------------------

To accommodate the broadest possible consumption the criteria are offered in three different formats.

.. grid:: 1 1 3 3
   :class-container: criteria-format-grid
   :gutter: 2

   .. grid-item-card:: Excel Spreadsheet
      :class-card: criteria-format-card criteria-format-excel
      :text-align: center

      .. rst-class:: criteria-format-icon

      XLS

      Basic .xlsx document with all identified elements. Editable to allow for sorting, modification, or tailoring.

      `Download .xlsx (296 KB) <../_static/downloads/sp800-63-4-conformance-criteria-v0.1.xlsx>`__

   .. grid-item-card:: PDF
      :class-card: criteria-format-card criteria-format-pdf
      :text-align: center

      .. rst-class:: criteria-format-icon

      PDF

      .pdf version of the excel version. Not editable to provide authoritative version and comparison to tailored criteria.

      `Download .pdf (4.6 MB) <../_static/downloads/sp800-63-4-conformance-criteria-v0.1.pdf>`__

   .. grid-item-card:: OSCAL
      :class-card: criteria-format-card criteria-format-oscal
      :text-align: center

      .. rst-class:: criteria-format-icon

      OSCAL

      OSCAL conformant version of the criteria in JSON, XML, or YAML format.

      `Download .json (2.2 MB) <../_static/downloads/sp800-63-4-conformance-criteria-v0.1-oscal.json>`__

      `Download .xml (1.4 MB) <../_static/downloads/sp800-63-4-conformance-criteria-v0.1-oscal.xml>`__

      `Download .yaml (1.4 MB) <../_static/downloads/sp800-63-4-conformance-criteria-v0.1-oscal.yaml>`__

.. card::
   :class-card: criteria-comment-card

   Comments on each of these versions can be provided :doc:`here </comments/index>`.
