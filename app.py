import streamlit as st

# Create a list of topics
topics = ["Topic 1", "Topic 2", "Topic 3"]

# Create a search bar
search_query = st.text_input("Search:", "")

# Create a select box for topic selection
selected_topic = st.selectbox("Select a topic:", topics)

# Filter and display content based on search query and selected topic
if search_query:
    # Filter content based on search query
    # Display filtered content
    st.write(f"Displaying results for search query: {search_query}")
elif selected_topic:
    # Filter content based on selected topic
    # Display filtered content
    st.write(f"Displaying results for topic: {selected_topic}")
else:
    # Display default content
    st.write("Welcome to the project showcase!")


# Define a function to create project cards
def create_project_card(title, image, tech_stack, description, github_link):
    # Add CSS style for project card
    st.markdown(
        """
        <style>
        .project-card {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Start project card container
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    
    # Display project title
    st.header(title)
    
    # Display project image
    st.image(image, width=200)
    
    # Display colored blocks indicating tech stack
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("Tech Stack:")
    for tech in tech_stack:
        st.markdown(f'<span style="background-color:{tech["color"]}; color:white; padding: 5px; border-radius: 5px; margin-right: 5px;">{tech["name"]}</span>', unsafe_allow_html=True)
    
    # Display project description
    st.write(description)
    
    # Display button to visit GitHub
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Visit GitHub"):
        # Redirect to GitHub link
        st.markdown(f"[GitHub Repository]({github_link})")

    # End project card container
    st.markdown('</div>', unsafe_allow_html=True)

# Example projects data
projects = [
    {
        "title": "Project 1",
        "image": "https://via.placeholder.com/200",
        "tech_stack": [
            {"name": "Python", "color": "blue"},
            {"name": "Streamlit", "color": "green"},
            # Add more tech stack items as needed
        ],
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "github_link": "https://github.com/example/project1"
    },
    # Add more projects as needed
]

# Display each project card
for project in projects:
    create_project_card(
        title=project["title"],
        image=project["image"],
        tech_stack=project["tech_stack"],
        description=project["description"],
        github_link=project["github_link"]
    )
