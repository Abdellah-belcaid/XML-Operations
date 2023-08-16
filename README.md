# XML Validator and Transformer
This is a web application built using the Django web framework and several Python libraries such as lxml, xmltodict, and subprocess. The application provides features to validate XML using DTD or XSD and transform XML to JSON and HTML using XSLT. Additionally, the application is capable of transforming XSD to DTD using a Perl script, which requires Perl to be installed on the user's operating system.     
  
## Features   
1. Validate XML using DTD or XSD   
2. Transform XML to JSON    
3. Transform XML to HTML using XSLT   
4. Transform XSD to DTD using Perl script (Perl installation required)   

## Requirements   
The following dependencies are required to run the application:     

- Python 3.x   
- Django 3.x   
- lxml   
- xmltodict   
Additionally, if you want to use the XSD to DTD transformation feature, Perl must be installed on your operating system.    

## Installation   
To install the application, follow these steps:    
   
Clone the repository:    
```
git clone https://github.com/abdellah-belcaid/XML_Validator_Transformer.git  
```
Install the Python dependencies:    
```  
pip install -r requirements.txt    
```  
Install Perl if you want to use the XSD to DTD transformation feature.    

Run the Django development server:      
```   
python manage.py runserver   
```   
Access the application at http://localhost:8000/ in your web browser.    
   
## Usage  
### Validating XML    
* Click on the "Validate XML" link in the navigation menu.   
* Choose the type of validation (DTD or XSD) and select the XML file to validate.   
* Click on the "Validate" button to validate the XML.    
* The validation results will be displayed on the page.   
### Transforming XML to JSON   
* Click on the "Transform XML to JSON" link in the navigation menu.   
* Select the XML file to transform.   
* Click on the "Transform" button to transform the XML to JSON.   
* The transformed JSON will be displayed on the page.   
### Transforming XML to HTML using XSLT   
* Click on the "Transform XML to HTML" link in the navigation menu.   
* Select the XML file to transform.   
* Select the XSLT file to use for the transformation.   
* Click on the "Transform" button to transform the XML to HTML.   
* The transformed HTML will be displayed on the page.   
### Transforming XSD to DTD   
* Click on the "Transform XSD to DTD" link in the navigation menu.   
* Select the XSD file to transform.   
* Click on the "Transform" button to transform the XSD to DTD.   
* The transformed DTD will be displayed on the page.    
## Conclusion   
This web application provides a simple and convenient way to validate XML and transform it to JSON or HTML using XSLT. The additional feature of transforming XSD to DTD using Perl makes it even more powerful. The application is built using Python and the Django web framework, making it easy to customize and extend.

* link for video demo : https://www.linkedin.com/posts/abdellah-belcaid_xmlabrproject-masterabrisi-tde-activity-7025434335381966848-IGD2?utm_source=share&utm_medium=member_desktop
