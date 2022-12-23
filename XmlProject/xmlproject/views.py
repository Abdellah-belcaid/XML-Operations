from asyncio.windows_events import NULL
from django.shortcuts import render ,redirect
from . import functions 
from django.core.files.storage import FileSystemStorage
import codecs


def home(request): 
    return render(request, 'index.html')    

    
def validate_xml_with_DTD(request):
    if request.method == 'POST':           
        if(request.POST['operation'] == "text_op"):
            if(request.POST['text_xml'] and request.POST['text_dtd']):
                xml=request.POST['text_xml']
                dtd=request.POST['text_dtd']
                                                                                                                        
                xml_file = codecs.open("media/inputs/xml_file.xml", "w","utf-8")
                dtd_file = codecs.open("media/inputs/dtd_file.dtd", "w","utf-8")                                                                                  
                                                                
                xml_file.write(xml) 
                dtd_file.write(dtd)                                                                                                                            
                
                xml_file.close()        
                dtd_file.close()        
                
                status,msg=functions.DTD_validation(xml_file.name,dtd_file.name)                
                
                context={"status":status,"msg":msg,"xml_validation":True}                                                                     
                return render(request,'index.html',context) 
                                      
        elif(request.FILES['xml_file'] and request.FILES['dtd_file']):               
            xml=request.FILES['xml_file']
            dtd=request.FILES['dtd_file']
            fss = FileSystemStorage()
            
            # Enregistrer le fichier importer dans le fichier ./media
            dtd_file = fss.save(dtd.name, dtd)
            xml_file = fss.save(xml.name, xml)
            
            dtd_url ="."+str(fss.url(dtd_file))
            xml_url ="."+str(fss.url(xml_file))
                        
            status,msg=functions.DTD_validation(xml_url,dtd_url)            
           
            fss.delete(xml_file)            
            fss.delete(dtd_file)            
            
            context={"status":status,"msg":msg,"xml_validation":True}
            return render(request,'index.html',context)
                        
    return render(request,'index.html')         
    

def validate_xml_with_XSD(request):
    if request.method == 'POST':           
        if(request.POST['operation'] == "text_op" ):
            if(request.POST['text_xml'] and request.POST['text_xsd']):
                xml=request.POST['text_xml']
                xsd=request.POST['text_xsd']
                                                
                xml_file = codecs.open("media/inputs/xml_file.xml", "w","utf-8")
                xsd_file = codecs.open("media/inputs/xsd_file.xsd", "w","utf-8")
                                
                xml_file.write(xml) 
                xsd_file.write(xsd)                 

                xml_file.close()        
                xsd_file.close()        
                                            
                status,msg=functions.XSD_Validate(xml_file.name,xsd_file.name)
                            
                context={"status":status,"msg":msg,"xml_validation":True}                                           
                return render(request,'index.html',context)                            
                                                
                
        elif(request.FILES['xml_file'] and request.FILES['xsd_file']):               
            xml=request.FILES['xml_file']
            xsd=request.FILES['xsd_file']
            fss = FileSystemStorage()
            
            # Enregistrer le fichier importer dans le fichier ./templates/myFiles
            xsd_file = fss.save(xsd.name, xsd)
            xml_file = fss.save(xml.name, xml)
            
            xsd_url ="."+str(fss.url(xsd_file))
            xml_url ="."+str(fss.url(xml_file))
                        
            status,msg=functions.XSD_Validate(xml_url,xsd_url)
            
            context={"status":status,"msg":msg,"xml_validation":True}
            fss.delete(xml_file)            
            fss.delete(xsd_file)            
            return render(request,'index.html',context)
                        
    return render(request,'index.html')         
    

    
def Xml_to_Json_convert(request):
    if request.method == 'POST': 
                
        if(request.POST['operation'] == "text_op"):            
            if(request.POST['xml_text'] and True):
                xml=request.POST['xml_text']                
                                                
                xml_file = codecs.open("media/inputs/xml_file.xml", "w","utf-8")
                                
                xml_file.write(xml)                 

                xml_file.close()                            
                                            
                json_data=functions.xml_to_json(xml_file.name)
                            
                context={'json':json_data,"xml_to_json":True}
                return render(request,'index.html',context)
                                      
        elif(request.FILES['xml_file'] ):               
            xml=request.FILES['xml_file']            
            fss = FileSystemStorage()
                        
            # Enregistrer le fichier importer dans le fichier ./templates/myFiles            
            xml_file = fss.save(xml.name, xml)
                    
            xml_url ="."+str(fss.url(xml_file))
                                    
            json_data=functions.xml_to_json(xml_url)
            fss.delete(xml_file)    
            context={'json':json_data,"xml_to_json":True}
            return render(request,'index.html',context)
                                
    return render(request,'index.html') 
    
  
                
def xslt_to_html_transfer(request):    
    if request.method == 'POST':           
        if(request.POST['operation'] == "text_op"):
            if(request.POST['xml_text'] and request.POST['xslt_text']):
                xml=request.POST['xml_text']
                xslt=request.POST['xslt_text']
                                                
                xml_file = codecs.open("media/inputs/xml_file.xml", "w","utf-8")
                xslt_file = codecs.open("media/inputs/xslt_file.xsl", "w","utf-8")
                                
                xml_file.write(xml) 
                xslt_file.write(xslt)                 

                xml_file.close()        
                xslt_file.close()        
                                            
                status,msg=functions.xslt_transformer_to_html(xml_file.name,xslt_file.name)                                
                
                if status:                             
                    return render(request,"output-toc.html")
                else:                    
                    context={"xml_to_html":True,"msg":msg}
                    return  render(request,"index.html",context)
        
        elif(request.FILES['xml_file'] and request.FILES['xslt_file']):               
            xml=request.FILES['xml_file']
            xslt=request.FILES['xslt_file']
            fss = FileSystemStorage()
            
            # Enregistrer le fichier importer dans le fichier ./templates/myFiles
            xslt_file = fss.save(xslt.name, xslt)
            xml_file = fss.save(xml.name, xml)
            
            xslt_url ="."+str(fss.url(xslt_file))
            xml_url ="."+str(fss.url(xml_file))
                                                          
            status,msg=functions.xslt_transformer_to_html(xml_url,xslt_url)                        
            fss.delete(xml_file)            
            fss.delete(xslt_file) 
            if status:                             
                return render(request,"output-toc.html")
            else:                
                context={'xml_to_html':True,"msg":msg}
                return  render(request,"index.html",context)
                        
    return render(request,'index.html')         

def dtd_to_xsd(request):
    if request.method == 'POST':                 
        if(request.POST['operation'] == "text_op"):            
            if(request.POST['dtd_text'] and True):
                dtd=request.POST['dtd_text']                
                                                
                dtd_file = codecs.open("media/inputs/dtd_file.xml", "w","utf-8")
                                
                dtd_file.write(dtd)                 

                dtd_file.close()                            
                                            
                xsd_data=functions.DTD_to_XSD(dtd_file.name)
                            
                context={'xsd':xsd_data,"dtd_to_xsd":True}
                return render(request,'index.html',context)
                                      
        elif(request.FILES['dtd_file'] ):               
            dtd=request.FILES['dtd_file']            
            fss = FileSystemStorage()
                        
            # Enregistrer le fichier importer dans le fichier ./templates/myFiles            
            dtd_file = fss.save(dtd.name, dtd)
                    
            dtd_url ="."+str(fss.url(dtd_file))
                                    
            xsd_data=functions.DTD_to_XSD(dtd_url)
            context={'xsd':xsd_data,"dtd_to_xsd":True}
            fss.delete(dtd_file)    
            return render(request,'index.html',context)
                                
    return render(request,'index.html') 
    
  