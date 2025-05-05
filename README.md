# session-feedback

## AI Agent for Generating PDFs

This repository contains an AI agent that generates a PDF for each participant of a session based on the presenter's profile, talks information, and feedback received from participants.

### Required Files

1. `presenter_profile.txt`: Contains information about the presenter.
2. `talks.json`: Contains information about each talk.
3. Google Sheet: Contains feedback received from participants.

### Setting Up Google Sheets API

To fetch feedback from the Google sheet, you need to set up Google Sheets API credentials. Follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the Google Sheets API for the project.
4. Create credentials for a service account.
5. Download the credentials file (JSON) and save it as `credentials.json` in the project directory.

### Using the AI Agent

1. Ensure you have the required files: `presenter_profile.txt`, `talks.json`, and `credentials.json`.
2. Run the `generate_pdfs.py` script:

```bash
python generate_pdfs.py
```

The script will generate a PDF for each participant based on the provided information.
