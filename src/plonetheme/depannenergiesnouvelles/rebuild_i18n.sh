#!/bin/sh

# Synchronise the .pot with the templates.
i18ndude rebuild-pot --pot locales/plonetheme.depannenergiesnouvelles.pot --merge locales/manual.pot --create plonetheme.depannenergiesnouvelles .

# Synchronise the resulting .pot with the .po files
i18ndude sync --pot locales/plonetheme.depannenergiesnouvelles.pot locales/*/LC_MESSAGES/plonetheme.depannenergiesnouvelles.po