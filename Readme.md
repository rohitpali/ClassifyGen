\# 🛠 Asset Classifier (ClassifyGen)

1\. Overview

The Asset Classifier project allows users to input details of
IT/computer hardware assets (e.g., laptops, servers, printers, etc.),
and classifies them with enriched metadata such as product line,
summary, and source URL using AI logic.

The project supports retries and logs all activities, and it features a
clean command-line or Streamlit-based UI interface.

2\. Features

\- Input form fields: product name, asset classification, manufacturer,
model number  - Retry logic if product not found  - Log generation for
tracking system events  - Output saved as JSON file  - Clean modular
code with:  - \`main.py\` for logic  - \`utils.py\` for reusable
functions  - \`config.json\` for settings - Streamlit-based UI for
simple web interface

3\. Project Setup

You can run this project locally in \*\*VS Code\*\* or any Python
environment.

Install Required Libraries:

\| Library \| Version \| Install Command \|
\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|
\| \`streamlit\` \| latest \| \`pip install streamlit\` \| \| \`json\`
\| built-in \| \*(No install needed)\* \| \| \`logging\` \| built-in \|
\*(No install needed)\* \|

4\. Folder Structure

ClassifyGen/ └── asset_processor/ ├── main.py ├── utils.py ├── app.py ←
(Streamlit UI) ├── config.json ├── input.json ├── output.json ←
(Generated after run) └── logs/ └── classifygen.log ← (Auto-generated
logs)

5\. How to Run (Command Line)

1\. Open terminal in \`asset_processor/\` folder 2. Run:python main.py
