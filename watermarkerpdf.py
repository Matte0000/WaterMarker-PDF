import PyPDF2
import sys

watermark_file = sys.argv[1]
original_file_name = sys.argv[2]
new_file = sys.argv[3]
  
origin_file = PyPDF2.PdfFileReader(open(original_file_name, 'rb'))
watermark = PyPDF2.PdfFileReader(open(watermark_file, 'rb'))
output = PyPDF2.PdfFileWriter()

try:
	for i in range(origin_file.getNumPages()):
	  page = origin_file.getPage(i)
	  page.mergePage(watermark.getPage(0))
	  output.addPage(page)

	  with open(new_file, 'wb') as file:
	    output.write(file)
	print('All done')
except:
	print('Error')

