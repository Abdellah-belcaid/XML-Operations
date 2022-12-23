<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">            
        <xsl:template match = "/">           
            <html>   
                <body>  
                    <h2>Books:-</h2>   
                    <table border = "1">   
                        <tr bgcolor = "#cd8932">   
                            <th>Book ID</th>   
                            <th>Book Name</th>   
                            <th>Author Name</th>   
                            <th>Publisher</th>   
                            <th>Price</th>                           
                            <th>Edition</th>
                        </tr>                        
                        <xsl:for-each select="store/book">   
                            <tr bgcolor = "#84cd32">   
                                <td><xsl:value-of select = "@id"/></td>   
                                <td><xsl:value-of select = "bookname"/></td>   
                                <td><xsl:value-of select = "authorname"/></td>   
                                <td><xsl:value-of select = "publisher"/></td>   
                                <td><xsl:value-of select = "price"/></td>                               
                                <td><xsl:value-of select = "edition"/></td>
                            </tr>   
                        </xsl:for-each>   
                    </table>   
                </body>   
            </html>   
        </xsl:template>   
</xsl:stylesheet>