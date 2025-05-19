Formative one : Regex Onboarding Hackathon
 This project implements regular expressions to extract specific data types from text strings, including email addresses, URLs, phone numbers, and cre dit card numbers. The solution is designed to process large volumes of text data efficiently.

Key Features:
	DataExtractor Class
Stores regex patterns in a dictionary (self.patterns).
extract_data() scans input text and returns matches in a structured dictionary.

	Interactive CLI
Test Mode: Runs predefined test cases.
Custom Input: Lets users paste text for analysis.
Clear, formatted output showing extracted data.

	Error Handling
Gracefully handles regex processing errors.

EXAMPLE OUTPUT

	This Input:
Email: user@example.com  
URL: https://google.com  
Phone: (123) 456-7890  

	Outputs:
EMAIL:  
  ✓ user@example.com  
URL:  
  ✓ https://google.com  
PHONE:  
  ✓ (123) 456-7890  

How To Use

	1. Run the script (python script.py).

	2. Choose:

1 = Test with built-in samples.
2 = Paste your own text.
3 = Exit.

Strengths

  ✔ Extensible: Easy to add new regex patterns.
  ✔ User-Friendly: Interactive menu and clean output.
  ✔ Comprehensive: Covers 8 common data types.

Ideal for: Log parsing, form validation, or web scraping cleanup

DEVELOPER : s-gasaro, Email: s.gasaro1@alustudent.com, Role: Full stack developer
 
