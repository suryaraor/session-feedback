import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from fpdf import FPDF

def read_presenter_profile(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_talks(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def fetch_feedback(sheet_name, credentials_file):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet.get_all_records()

def generate_pdf(participant, presenter_profile, talks, feedback):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Session Feedback", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Participant: {participant}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Presenter: {presenter_profile}", ln=True, align='L')
    
    pdf.cell(200, 10, txt="Talks:", ln=True, align='L')
    for talk in talks:
        pdf.cell(200, 10, txt=f"- {talk['title']}: {talk['description']}", ln=True, align='L')
    
    pdf.cell(200, 10, txt="Feedback:", ln=True, align='L')
    for fb in feedback:
        if fb['participant'] == participant:
            pdf.cell(200, 10, txt=f"- {fb['feedback']}", ln=True, align='L')
    
    pdf.output(f"{participant}_feedback.pdf")

def main():
    presenter_profile = read_presenter_profile('presenter_profile.txt')
    talks = read_talks('talks.json')
    feedback = fetch_feedback('Session Feedback', 'credentials.json')
    
    participants = set(fb['participant'] for fb in feedback)
    for participant in participants:
        generate_pdf(participant, presenter_profile, talks, feedback)

if __name__ == "__main__":
    main()
