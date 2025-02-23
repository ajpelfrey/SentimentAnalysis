cd /path/to/your/project  
python3 -m venv venv  

# For macOS/Linux  
source venv/bin/activate  

# For Windows  
venv\Scripts\activate  

pip install transformers torch  

# To run the classifier  
python text_classifier.py 
