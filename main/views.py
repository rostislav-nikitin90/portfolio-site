from django.shortcuts import render
# Import the render function to return HTML templates with context data

def home(request):
    # View function for the home page

    context = {
        # Context dictionary holds dynamic data passed to the template

        'name': 'Rostislav',
        'surname': 'Nikitin',
        # Personal details displayed on the homepage

        'latest_project': {
            # Dictionary describing the latest project

            'title': 'Visit Budva - Travel Guide Website Project',
            # Title of the latest project

            'description': (
                # Long description of the project, explaining pages, features, and interactivity
                "The travel website prototype for Budva, Montenegro built as a student project showcases Budva's "
                "cultural, historical, and touristic appeal through a responsive, interactive site. It includes three "
                "main pages and one confirmation page: Home Page (home.html), Budva Attractions Page (budva.html), "
                "Contact Page (contact.html), Thank You Page (thankyou.html). Home Page welcomes visitors with a "
                "slideshow of Budva's highlights, displays current weather using OpenWeather API, introduces Budva's "
                "history and culture with rich text and images and uses finalprojecthomepage.js and finalproject.js "
                "for interactivity. Budva Attractions Page dynamically loads 15 local attractions from a JSON file, "
                "displays each attraction in a grid layout (clicking an attraction opens a modal dialog with detailed "
                "info) and uses finalprojectbudvapage.js and finalproject.js. Contact Page offers a contact form with "
                "fields for name, email, and message. It includes static contact info and a scenic image and form "
                "submission redirects to thankyou.html."
            ),
            'tools': (
                # Technical features and tools used in the project
                "Technical Features: HTML5 & CSS3 with responsive design for mobile and desktop, "
                "JavaScript for dynamic content and modal interactions, weather API integration for "
                "real-time data, JSON data loading for attractions, interactive slideshow and modal dialogs."
            )
        }
    }
    return render(request, 'home.html', context)
    # Render the home.html template with the context data

def projects(request):
    # View function for the projects page

    all_projects = [
        # List of dictionaries, each representing a project with details

        {
            'title': 'Visit Budva - Travel Guide Website Project',
            # Title of the project

            'short_description': (
                # Short summary of the project
                "A 3-page travel website prototype for Budva, Montenegro includes dynamic loading "
                "of local attractions from JSON with interactive modals, weather API integration, "
                "and a contact form."
            ),
            'long_description': (
                # Detailed description of the project
                "The travel website prototype for Budva, Montenegro built as a student project showcases Budva's "
                "cultural, historical, and touristic appeal through a responsive, interactive site. It includes three "
                "main pages and one confirmation page: Home Page (home.html), Budva Attractions Page (budva.html), "
                "Contact Page (contact.html), Thank You Page (thankyou.html). Home Page welcomes visitors with a "
                "slideshow of Budva's highlights, displays current weather using OpenWeather API, introduces Budva's "
                "history and culture with rich text and images and uses finalprojecthomepage.js and finalproject.js "
                "for interactivity. Budva Attractions Page dynamically loads 15 local attractions from a JSON file, "
                "displays each attraction in a grid layout (clicking an attraction opens a modal dialog with detailed "
                "info) and uses finalprojectbudvapage.js and finalproject.js. Contact Page offers a contact form with "
                "fields for name, email, and message. It includes static contact info and a scenic image and form "
                "submission redirects to thankyou.html."
            ),

            'tools': (
                # Tools and technologies used
                "Technical Features: HTML5 & CSS3 with responsive design for mobile and desktop, "
                "JavaScript for dynamic content and modal interactions, weather API integration for "
                "real-time data, JSON data loading for attractions, interactive slideshow and modal dialogs."
            ),

            'image_url': '/static/images/budva_travel_website.jpg',
            # Path to project image

            'category': 'web',
            # Category used for filtering (web development)

            'url': 'https://rostislav-nikitin90.github.io/wdd231/finalproject/home.html'
            # Link to the live project
        },

        # Other projects follow the same structure: title, descriptions, tools, image, category, url 
        # Poster Design Project, Budva Chamber of Commerce Website Project, Comic Book Design Project, 
        # Montexplore Travel Guide, Magazine Spread Design Project
        {
            'title': 'Poster Design Project',
            'short_description': (
                "A poster design for one of Shakespeare's plays, \"Macbeth,\" "
                "effectively uses graphic design principles to enhance the play's tragic theme."
            ),
            'long_description': (
                "Student project - The poster design for Shakespeare's play \"Macbeth\" applies the principles "
                "of graphic design effectively to reinforce the play's tragic theme. The color scheme centers "
                "on a deep, bloody red background, symbolizing violence and guilt, while the dark tones of "
                "Macbeth's bowed head create stark contrast that draws immediate attention to his grief. "
                "Alignment is clean and deliberate, with text blocks (title, theater information, dates) "
                "positioned in a structured vertical flow that guides the viewer's eye downward, echoing "
                "Macbeth's descent into guilt. The careful proximity of the title to the image ties the visual "
                "and textual elements together, ensuring they communicate a unified message. Hierarchy is "
                "established through the bold, large typeface of \"MACBETH,\" which dominates the composition, "
                "followed by smaller supporting details like dates and venue information. Finally, emphasis is "
                "achieved by isolating Macbeth's sorrowful expression against the red field, making his emotional "
                "state the focal point of the poster. Altogether, these principles combine to evoke sadness and "
                "anxiety, perfectly mirroring the play's atmosphere."
            ),
            'tools': 'Tool(s): Adobe Illustrator',
            'image_url': '/static/images/poster_design.png',
            'category': 'illustration',
            # Category used for filtering (graphic design)

            'url': 'https://drive.google.com/file/d/1Gv1zRq0sLH39n8QnLamNjd42dhp-gfaM/view?usp=sharing'
        },
        {
            'title': 'Budva Chamber of Commerce Website Project',
            'short_description': (
                "A 4-page prototype chamber of commerce website uses JavaScript to dynamically load "
                "JSON data and API responses."
            ),
            'long_description': (
                "The prototype website was created as a student project and represents a digital chamber of "
                "commerce for Budva, Montenegro. It consists of four main pages: Home Page (index.html), "
                "Directory Page (directory.html), Join Page (join.html + thankyou.html) and Discover Page "
                "(discover.html). Home Page welcomes visitors, highlights upcoming conferences, displays "
                "current weather and a three day forecast via OpenWeather API, and features company spotlights "
                "drawn from JSON data. Directory Page provides a business directory with toggleable grid and "
                "list views, dynamically populated from members.json. Join Page explains membership levels "
                "(Non Profit, Bronze, Silver, Gold) with detailed benefits, and includes a membership "
                "application form. A confirmation page displays submitted form data. Discover Page showcases "
                "Budva's history, demographics, statistics, and cultural highlights, with interactive features "
                "like visit tracking messages and a gallery of images."
            ),
            'long_description': (
                "Technical Features: HTML5 & CSS (mobile, tablet, desktop responsive styles), "
                "JavaScript for interactivity, API calls, and dynamic content rendering, "
                "JSON data file to store and load business member information, "
                "animations and responsive layouts for modern UI/UX."
            ),
            'image_url': '/static/images/budva_chamber_of_commerce_website.jpg',
            'category': 'web',
            # Category used for filtering (web development)

            'url': 'https://rostislav-nikitin90.github.io/wdd231/chamber/'
        },
        {
            'title': 'Comic Book Design Project',
            'short_description': (
                "A comic book cover and double-page spread design that effectively applies "
                "graphic design principles to create clarity and impact in a superhero-themed layout."
            ),
            'long_description': (
                "This student comic book design applies the core principles of graphic design in a clear, "
                "functional way: bold color choices (reds, blues, and blacks) establish the superhero theme "
                "and create immediate visual energy, while strong contrast between text and background ensures "
                "readability of titles and dialogue. Alignment is consistent, with speech bubbles and captions "
                "neatly positioned to guide the reader's eye across the panels without confusion. Proximity is "
                "used effectively—dialogue balloons are placed close to characters to reinforce who is speaking, "
                "and related visual elements are grouped together to maintain narrative flow. Hierarchy is "
                "established through the oversized title on the cover and the dramatic \"BIONICUS\" launch sequence "
                "inside, drawing attention to the most important story beats. Emphasis is achieved by enlarging "
                "key words (\"HELP!\", \"SOMETHING IS NOT RIGHT!!!\") and using capital letters to heighten urgency "
                "and drama. The design demonstrates a solid grasp of how these principles work together to create "
                "clarity, impact, and storytelling rhythm in a comic book format."
            ),
            'tools': 'Tool(s): Adobe Illustrator, Adobe InDesign',
            'image_url': '/static/images/comic_book_design.png',
            'category': 'illustration',
            # Category used for filtering (graphic design)

            'url': 'https://drive.google.com/file/d/1RfVkd2Jqt-RtIf2N0x08VheTMvR2BI5W/view?usp=sharing'
        },
        {
            'title': 'Montexplore - Montenegro Travel Guide Website Project',
            'short_description': (
                "A 3-page travel website for Montenegro uses JavaScript to dynamically load tourist "
                "destinations and includes a newsletter subscription form with confirmation tracking."
            ),
            'long_description': (
                "The travel guide prototype for Montenegro created as a student project presents Montenegro's "
                "natural and historical richness through a responsive, interactive site. It includes three main "
                "pages and one confirmation page: Home Page (home.html), Where to Go Page (where-to-go.html), "
                "What to See Page (what-to-see.html) and Subscription Confirmation Page (subscription-confirmation.html). "
                "Home Page welcomes users with a scenic banner and intro text and displays upcoming events with a "
                "filter by type (Culture, Music, Sports). It includes a newsletter subscription form with name/email "
                "fields and uses finalprojecthomepage.js, finalproject.js, and getdates.js. Where to Go Page highlights "
                "Montenegro's coastal towns and national parks and visitors can toggle between categories. Destinations "
                "are dynamically loaded into a grid layout using finalprojectwheretogopage.js. What to See Page features "
                "three top destinations: Kotor, Sveti Stefan, and Perast. Each section includes a heading, image, and "
                "description. Subscription Confirmation Page displays a thank-you message and tracks the number of "
                "successful submissions using counter.js and getdates.js."
            ),
            'tools': (
                "Technical Features: HTML5 & CSS3 with responsive design for mobile and tablet, "
                "JavaScript for dynamic content, form handling and event filtering, "
                "subscription tracking with local counter"
            ),
            'image_url': '/static/images/montenegro_travel_website.jpg',
            'category': 'web',
            # Category used for filtering (web development)

            'url': 'https://rostislav-nikitin90.github.io/wdd131/finalproject/home.html'
        },
        {
            'title': 'Magazine Spread Design Project',
            'short_description': (
                "A magazine cover and double-page spread design that visually centers on "
                "Jesus Christ as a model of personal development."
            ),
            'long_description': (
                "The magazine spread applies the core principles of graphic design in a way that reinforces "
                "its Christ-centered message of human development. Color is used symbolically, with blue "
                "subheadings evoking trust, wisdom, and heaven, yellow highlighting divine light and joy, "
                "and bone-colored backgrounds tying visually to the statue of Christ, creating unity across "
                "pages. Contrast is achieved through the bold, oversized title \"JESUS CHRIST\" against the sky, "
                "immediately drawing attention, while softer tones in the body text maintain readability. "
                "Alignment is consistent, with headings and text blocks neatly structured to guide the eye "
                "logically through spiritual, social, physical, and intellectual themes. Proximity groups "
                "related ideas together—subheadings, quotes, and circular images—so readers can easily connect "
                "concepts without distraction. Hierarchy is clear: the statue and title dominate the opening "
                "page, subheadings in blue establish secondary importance, and body text flows beneath them. "
                "Emphasis is placed on Christ through the full-page statue and circular imagery, with the circle "
                "symbolizing unity and eternity, visually reinforcing the article's theme of growth in His image. "
                "Altogether, the design balances symbolism and structure to immerse the reader in the spiritual "
                "and developmental journey described."
            ),
            'tools': 'Tool(s): Adobe InDesign',
            'image_url': '/static/images/magazine_spread.png',
            'category': 'illustration',
            # Category used for filtering (graphic design)

            'url': 'https://drive.google.com/file/d/1x1MF3KmyORu8Wffy-qVhKeD9_pWpw6ss/view?usp=sharing'
        },
    ]

    category = request.GET.get('category')
    # Get the category filter from the query string (e.g., ?category=web)

    if category:
        filtered_projects = [p for p in all_projects if p['category'] == category]
        # If a category is selected, filter projects by category
    else:
        filtered_projects = all_projects
        # Otherwise, show all projects

    context = {
        'projects': filtered_projects,
        # Pass the filtered list of projects to the template

        'selected_category': category
        # Pass the selected category to highlight the filter in the template
    }
    return render(request, 'projects.html', context)
    # Render the projects.html template with the context data

def contact(request):
    # View function for the contact page

    if request.method == 'POST':
        # If the form is submitted via POST

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Retrieve form data: name, email, and message

        context = {
            'submitted': True,
            # Flag to indicate form submission was successful

            'name': name,
            'email': email,
            'message': message
            # Pass submitted data back to the template for confirmation
        }
        return render(request, 'contact.html', context)
        # Render contact.html with thank-you message and submitted data

    return render(request, 'contact.html')
    # If GET request, just render the empty contact form
