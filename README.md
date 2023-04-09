# spikex_web


# :computer:	SpikeX - Open Source OSINT Framework :detective:	

__This project is made with lots of caffiene :cup_with_straw:	:cup_with_straw: :cup_with_straw:	(or love, both are the same things .... )__  		


## :star2:	Introduction

SpikeX is an open-source OSINT framework that is designed for manual web scanning, web scraping, and gathering comprehensive information from the internet. It provides a web interface with a GUI mode for testing and is a passive reconnaissance tool for cybersecurity and penetration testers.

The tool is powered by the Shodan search engine and can gather a vast amount of data that will expand the attack surface of the penetration testers and provide fast threat intel. SpikeX is also a community project that provides REST API to other developers, allowing them to add more functionalities and use them.


## :bookmark_tabs:	 Core Concept

SpikeX offers several features that make it a valuable tool for cybersecurity professionals. It can be used for both manual and automated scans, making it versatile and flexible. The tool can assist security teams in carrying out vulnerability assessments and patching them before hackers have a chance to exploit them.
The open-source nature of SpikeX means that developers are free to add more functionalities and use them. This allows the tool to evolve and adapt to the ever-changing landscape of cybersecurity threats. Overall, SpikeX is a valuable contribution to the open-source community and the development of software cultures.

## :cloud:	Accessibility and Usage

SpikeX is availabe in Web Interface that has been deployed and made availabe accross the world. 

[SpikeX Dashboard Page](http://spikex.co)

This website gives access to the scanning tool. This Framework provides no restrictions on scanning as it is a community project. The project is in the development stages and will always be (being an community based project) and is aimed to be available for command-line usage in the future. 


## :sparkles:	 Technologies Used

### :test_tube:	[Flask Framework](https://flask.palletsprojects.com/en/2.2.x/)

Flask is a lightweight and extensible web framework for Python that allows developers to quickly build web applications with minimal boilerplate code. It provides routing, request/response handling, and support for templates, and has a rich ecosystem of extensions for additional functionality. Flask is designed to be simple and easy to use, making it a popular choice for building web applications in Python.

### :star:	[Python](https://www.python.org/)
Python is a high-level, interpreted programming language that emphasizes simplicity, readability, and ease of use. It was first released in 1991 and has since become one of the most popular programming languages in the world. Python is known for its clean and intuitive syntax, versatility, and cross-platform compatibility. It can be used for a wide range of applications, including web development, data science, machine learning, automation, and more. Overall, Python is a powerful and flexible language that is popular among both beginners and experienced developers.

### :mechanical_arm:	[NGINX](https://www.nginx.com/)
Nginx is a popular open-source web server software that is known for its high performance, scalability, and reliability. It is used to serve static content quickly and efficiently, handle a large number of concurrent connections, and distribute incoming traffic across multiple servers. Nginx also has built-in support for reverse proxying, load balancing, and SSL encryption, and can be configured to serve a wide range of applications and workloads. Overall, Nginx is a powerful and flexible web server software that is widely used by businesses and organizations around the world.

### :unicorn:	[Gunicorn](https://gunicorn.org/)
Gunicorn (short for "Green Unicorn") is a Python Web Server Gateway Interface (WSGI) HTTP server that is designed to be simple, fast, and lightweight. It was first released in 2010 and has since become one of the most popular WSGI servers for Python web applications. Gunicorn is designed to work with a variety of Python web frameworks, including Django and Flask, and is known for its ease of use and performance. It uses pre-fork worker model to handle requests and can handle multiple requests simultaneously.

### :japanese_castle:	[Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
Jinja is a popular and powerful templating engine for Python that is used to generate dynamic HTML, XML, and other markup formats. It was inspired by the Django template engine but is designed to be more flexible and extensible. Jinja allows developers to separate the presentation layer from the application logic, making it easier to build complex web applications. It provides a wide range of features for working with templates, including template inheritance, macros, filters, and more.

### :hammer:	[Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/)

Werkzeug provides a wide range of utilities and features for building web applications, including request and response handling, URL routing, cookie and session management, and more. It is also compatible with a variety of web frameworks, including Flask, Django, and Pyramid.

### :desktop_computer:	[Ubuntu Server](https://ubuntu.com/)

Ubuntu Server is a popular operating system for web hosting due to its stability, security, and flexibility. It is designed to be easy to manage, with a command-line interface that allows administrators to quickly and easily configure and manage their servers.

Ubuntu Server comes with a range of pre-installed tools and packages that are well-suited to web hosting, including Apache or Nginx web servers, PHP and other scripting languages, and a range of database management systems.

In addition to its built-in features, Ubuntu Server also has a large and active community of developers and users, which means that there are many resources available for troubleshooting, customization, and optimization.

Overall, Ubuntu Server is a reliable and robust platform for web hosting, and is widely used by businesses and organizations around the world.






## Web Application Data Fields

### Sitemap Data

A sitemap is a file that provides information about the pages, videos, and other files on a website and how they are organized. It is used by search engines to better understand the content and structure of a website, which can improve its visibility and ranking in search results.

Sitemaps typically include information such as the URL of each page on the site, when it was last updated, and how frequently it is updated. They can also include additional metadata, such as the importance of the page relative to other pages on the site.

Sitemaps are important for websites with a large number of pages or complex structures, as they can help search engines to better understand the site's organization and hierarchy. They can also be useful for identifying and resolving crawl errors, and for optimizing the site's internal linking structure.

[Sitemap Wikipedia](https://en.wikipedia.org/wiki/Site_map)
### Href Data

SpikeX crawls through the target url and finds all the websites that are in the href tags in the html source code. Domains related to the target is only being displayed and no out-of-scope urls are displayed.

### Robots.txt file contents 
A robots.txt file is a text file that is placed in the root directory of a website and provides instructions to search engine bots on which pages of the site to crawl or not to crawl. It is a tool used by webmasters to control how search engines access and index the content of their site.

The robots.txt file contains a set of rules for search engine crawlers, such as Googlebot, on which pages or directories to ignore or disallow. For example, a webmaster may use a robots.txt file to disallow access to sensitive pages, such as login pages, or to prevent search engines from indexing duplicate content.

It's important to note that while a robots.txt file can provide guidance to search engine bots, it is not a foolproof method for preventing search engines from accessing certain pages. It is possible for search engines to ignore robots.txt directives or for malicious bots to ignore them altogether.

Overall, a robots.txt file is a useful tool for webmasters to control the visibility of their site in search engine results and to prevent sensitive information from being indexed.

[Robots.txt Wikipedia](https://en.wikipedia.org/wiki/Robots.txt)
#### Robots Allowed

The web application's robots.txt file allows the crawler access the website.

#### Robots Disallowed

The web application's robots.txt file does not allow the crawler access the website.

### HTTP header Data

HTTP headers are pieces of information that are sent between a web server and a client as part of an HTTP request or response. HTTP header data contains metadata about the HTTP message, such as the type and version of the message, the language of the content, the encoding format, and any cookies associated with the request.

HTTP headers can be vulnerable to a variety of attacks and exploits that can compromise the security and privacy of web applications and their users. Here are some common HTTP header vulnerabilities:

Injection attacks: Attackers can manipulate HTTP headers to inject malicious code into web applications or to steal sensitive information, such as user credentials or session tokens.

Cross-site scripting (XSS) attacks: Attackers can use certain HTTP headers, such as the Referer header, to inject malicious scripts into web pages and hijack user sessions or steal user data.

Cross-site request forgery (CSRF) attacks: Attackers can use HTTP headers to trick users into performing unintended actions on a web application, such as making unauthorized transactions or deleting user data.

Clickjacking attacks: Attackers can use HTTP headers to overlay malicious content on top of legitimate web pages and trick users into clicking on links or buttons that execute unintended actions.

Content Security Policy (CSP) bypasses: Attackers can use certain HTTP headers, such as the Content-Security-Policy header, to bypass CSP protections and execute malicious scripts or access restricted resources.

[HTTP Header Fields List Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)

[HTTP Header Fields OWASP Vulnerabilities Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)

### Form tags detected

Form tags in html indicated input pages, potentially login pages. This might be a potential way for the hacker to get an intercation with the target web server. SpikeX counts the number of form tags and find injection points in the web application.

### Shodan Data

Shodan is a search engine that specializes in indexing devices and systems that are connected to the internet. Unlike traditional search engines like Google, Shodan does not search for websites or content on the web, but rather for devices that are connected to the internet, such as servers, routers, webcams, and other IoT devices.

Shodan works by scanning the internet for open ports, which are used by devices to communicate with other devices on the internet. Shodan then indexes the devices that it finds, along with information about the services and applications that they are running, as well as any vulnerabilities or misconfigurations that may be present.

Users can search for devices on Shodan using a variety of search filters, such as device type, location, operating system, and open ports. This can be useful for researchers, developers, and security professionals who need to identify vulnerable or misconfigured devices on the internet, or who need to gather data about the use of specific technologies or services.

[Shodan Developer Web Page](https://developer.shodan.io/)
## SpikeX REST API


#### The Power of REST API

REST (Representational State Transfer) is a web-based architectural style for building APIs (Application Programming Interfaces). A REST API is a web-based API that uses HTTP requests to GET, POST, PUT and DELETE data. REST is based on the principles of client-server architecture, statelessness, and uniform interface.

REST APIs are commonly used for web services that allow external applications to interact with a web application or database. REST APIs use standard HTTP methods to send and receive data, making them platform and language independent. This makes it easy for developers to create applications that can communicate with any REST API.

#### How SpikeX is charged with REST API
SpikeX aims to contribute to the projects of other developers and add more value to their hard written code. SpikeX provides completely open and free REST API that can be accessed without any API KEY. This makes it easier for the developer to plug and play the SpikeX functionalites. 

#### Usage:

Visit [SpikeX API PAGE](http://spikex.co/api)

Send a GET request to
```
http://spikex.co/api?url=<target_url>&mode=<mode>
```

#### Available modes: 

* href_spider
* sitemap
* http_header_data
* allow_robots
* disallow_robots
* form_count
* dir_enum
* sub_enum

#### Response to the GET Request 

SpikeX responds to the GET Request of the API page with proper parameters set with data in JSON format. This makes the data managable and easy to handle for the developers. 

#### What about spooky errors?

SpikeX return as error in JSON format to the developer. This allows the developer to configure the code in a way that the errors can be managed. 

## :sunglasses:	For Contributors 

The entire project has be uploaded to the GitHub. Developers can deploy the __Flask Application__ in their own system for development purposes. The deployment is pretty simple as shown in the walkthrough.

### Setting Development Environment on Linux system


#### Update the system

```
sudo apt-get update
```
```
sudo apt-get upgrade
```
#### Creating a pip environment in the directory

Navigate to the directory of the web application

Learn about [pipenv](https://pypi.org/project/pipenv/) virtual environment
```
pip3 install pipenv
```
Interact with the pipenv shell
```
pipenv shell
```

#### Setting Up environment variables

```
export FLASK_APP=backend.py
export FLASK_ENV=development
```

#### Run the Flask Application

```
flask run
```

#### Accessing the Web Interface
The [localhost](http://127.0.0.1:5000) of the system will be the web interface of the framework on port 5000

```
http://127.0.0.1:5000
```


## :earth_americas:	 Open Source - Community based Project :earth_asia:	

*__"Open source is a way of thinking, not just a way of doing." - Tim O'Reilly__*

### The SpikeX Mindset
SpikeX belives in the development of technology through harnessing the power of community. There are highly skilled developers around us striving to contribute for the development of cyberpunk culture. We dream of a future of where each one of us has access to cutting edge technology freely available to use as well as openly contribute their contributions. With this idea, SpikeX declares itself to be Open-Source Community Based Project that will be maintained and developed by the crowd.

### Nerds behind SpikeX
An kickstart is always necessary for starting a revolution. We are SpikeX development Team that would be responsible for smooth maintaince and updates of the project. We will be the one evaluating the project development ideas and investing in the hosting of the project. Again, we are just contributers and part of community who are working tirelessly with the SpikeX values. We don't expect for for anything, we just belive in contributing.

### Contributing to this project

#### Web Application
SpikeX is developed in a way that allows the web application to be updates effieciently and in the easiest way possible. This idea comes from the development of Framework. We will be evaluating the development ideas and contacting the contributers for further instructions. All the contributers will be acknowledged by our team. If the contributers are further intrested in joing the tribe, they will be most welcomed to join us. 

#### Command Line Interface
SpikeX is in the way of developing command-line interface for all those furious hackers out there. Contributers are most welcome to join the CMD development team and fetch their ideas and contribute to the project. 

#### Endless Possibilities
Got an awesome idea? feel free to let us know about it. New ideas from the communiy are the most pleasurable things for us. More developments on the availability, deployment, functionalilites, etc. can be suggested to us.


## :cup_with_straw: Donate us :cup_with_straw:
We are a small community of techie nerds with a dream of expanding this project better say mindset. If you like the concept of the the project and consider us buying some coffee to keep us awake at chilly nights, please consider donating us. 

[Buy me a Coffee](https://www.buymeacoffee.com/spikeX) 

![Logo](https://www.buymeacoffee.com/assets/img/guidelines/download-assets-2.svg)
