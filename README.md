 Unlocking Digital Evidence Utilizing Save Wizard in Forensic Analysis  

A socially relevant mini-project that explores the integration of Save Wizard with Digital Forensics to decrypt, analyze, and validate encrypted PlayStation save data using machine learning models for enhanced accuracy and evidence integrity.


 Abstract: 
Modern digital investigations often face challenges with encrypted or proprietary data formats, especially in gaming systems.  
This project demonstrates how the **Save Wizard** tool can aid forensic investigators in unlocking and analyzing encrypted game save files, maintaining chain of custody and evidence authenticity throughout the process.  
By combining forensic automation with Random Forest and Support Vector Machine (SVM) regressors, the system improves speed, accuracy, and reliability while maintaining compliance with forensic and ethical standards.



 Key Features:  
- Automated Evidence Decryption** using Save Wizard  
- Secure Analysis** with SHA-256 hashing and AES-256 encryption  
- Machine Learning Integration** (SVM & Random Forest) for data validation  
- Flask-Based Digital Forensics Chatbot** for educational simulation  
- Comprehensive Forensic Report Generation** (PDF/CSV format)  
- Compliance with Legal & Ethical Frameworks** for admissible evidence  


 System Architecture:  
1. Evidence Acquisition Layer** – Collects and preserves encrypted save files.  
2. Decryption Engine** – Integrates Save Wizard for secure decryption.  
3. Forensic Analysis Layer** – Extracts metadata, timestamps, and user behavior.  
4. Reporting Layer** – Generates structured reports and integrity hashes.  



Tools & Technologies:  
- Languages:** Python, HTML, JavaScript  
- Frameworks/Libraries: Flask, scikit-learn, NumPy, pandas, matplotlib  
- Forensic Tools:Save Wizard, FTK Imager, Autopsy, Hex Editor Neo  
- Security: AES-256 Encryption, SHA-256 Hashing  


How It Works:
1. Investigator uploads encrypted evidence file.  
2. Save Wizard decrypts and extracts save data.  
3. Python modules parse and analyze digital patterns.  
4. Machine learning models validate reliability of recovered evidence.  
5. Final forensic report is generated with all verified results.

Installation: 
You can run the chatbot locally for demonstration:

bash
Clone the repository (or download ZIP)
pip install -r requirements.txt
python src/app.py
