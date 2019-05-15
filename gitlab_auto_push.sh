#!/bin/bash

PROJECT_NAME="Sao-Carlos-Speed-Gun-Localization"
PROJECT_ID="1UNIZlzBiSnGXQElFsJMnyhEd000rIh49QI65U1EdBLYIN6rrq4-jskQO"

MESSAGE_UP_TO_DATE="nothing to commit, working tree clean"

echo -e "\nGETTING THE UPDATES FROM GOOGLE APPS SCRIPT PROJECT: $PROJECT_NAME\n"
clasp pull .clasp.json

OUTPUT_STATUS=$(git status)

  if [[ $OUTPUT_STATUS = *$MESSAGE_UP_TO_DATE ]]; then
    echo -e "\nNOTHING TO COMMIT TO GITLAB PROJECT $PROJECT_NAME\n"
  else
    git add .
    echo -e "\nWRITE THE COMMIT MESSAGE: "
    read COMMIT
    git commit -m "$COMMIT"
    git push
  fi

echo -e "\nTHE SCRIPT WAS SUCCESSFULLY PLAYED\n"
