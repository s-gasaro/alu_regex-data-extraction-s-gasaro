import re
from typing import Dict, List

class Data-Extractor:
    """
    A class for  handling extraction of various data patterns from the hundreds of thousands of pages of string using regex.
    """
    def __init__(self):
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'url': r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)',
            'phone': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]\d{4}',
            'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
            'time': r'(?:1[0-2]|0?[1-9]):(?:[0-5][0-9])(?:\s?(?:AM|PM))?|(?:2[0-3]|[01]?[0-9]):(?:[0-5][0-9])',
            'html_tag': r'<[^>]+>',
            'hashtag': r'#[A-Za-z0-9_]+',
            'currency': r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        }

    def extract_data(self, text: str) -> Dict[str, List[str]]:
        """
        Extract all patterns from the given text.
        
        Args:
            text (str): Input text to process
        
        Returns:
            Dict[str, List[str]]: Dictionary containing extracted data by type
        """
        results = {}
        try:
            for pattern_name, pattern in self.patterns.items():
                matches = re.findall(pattern, text)
                if matches:
                    results[pattern_name] = matches
                else:
                    results[pattern_name] = []
            return results
        except Exception as e:
            print(f"Error processing text: {e}")
            return {}

def test_extractor():
    """
    Test the DataExtractor with various test cases.
    """
    extractor = Data-Extractor()

    # Test cases
    test_text = """
    For support, email us at help@example.com or support.team@company.co.uk
    Visit our sites: https://www.example.com and http://test.com/page
    Phone numbers: (123) 456-7890, 987-654-3210, and 555.123.4567
    Credit card: 4111-1111-1111-1111
    Meeting times: 2:30 PM and 14:45
    HTML: <div class="test">Content</div> and <p>text</p>
    Tags: #Python #Coding #RegEx
    Prices: $19.99 and $1,234.56
    """

    results = extractor.extract_data(test_text)

    # Print results in a formatted way
    print("\nExtraction Results:")
    print("=" * 50)
    for pattern_type, matches in results.items():
        print(f"\n{pattern_type.upper()}:")
        if matches:
            for match in matches:
                print(f"  ✓ {match}")
        else:
            print("  No matches found")
    print("\n" + "=" * 50)

def main():
    """
    Main function to demonstrate the usage of DataExtractor.
    """
    print("RegEx Data Extraction Tool")
    print("=" * 50)

    extractor = Data-Extractor()

    while True:
        print("\nOptions:")
        print("1. Test with sample data")
        print("2. Enter custom text")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            test_extractor()
        elif choice == '2':
            print("\nEnter your text (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)

            text = "\n".join(lines)
            results = extractor.extract_data(text)

            print("\nResults:")
            print("=" * 50)
            for pattern_type, matches in results.items():
                print(f"\n{pattern_type.upper()}:")
                if matches:
                    for match in matches:
                        print(f"  ✓ {match}")
                else:
                    print("  No matches found")
        elif choice == '3':
            print("\nThank you for using the RegEx Data Extraction Tool!")
            break

            else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
