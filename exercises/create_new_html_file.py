import webbrowser

newString = 'WHY NOT WORKING'
htmlFormat = "<html>\n<body>\n<p>" + newString + "</p>\n</body>\n</html>" 


f = open("web_page_generator.html", "w")
f.write(htmlFormat)
f.close()

f = webbrowser.get('chrome')
f.open_new('file:///Users/jaimiebertoli/Documents/GitHub/Python/exercises/web_page_generator.html')
