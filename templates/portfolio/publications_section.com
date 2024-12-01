{% extends 'base.html' %}

{% block content %}
<!-- templates/portfolio/publications_section.html -->
<!-- Publications Section -->
<section id="publications">
    <h2>Publications and Articles</h2>
    <ul>
        {% for publication in publications %}
            <li>
                <h3>{{ publication.title }}</h3>
                {% if publication.link %}
                    <p><a href="{{ publication.link }}" target="_blank">{{ publication.link }}</a></p>
                {% endif %}
                {% if publication.file %}
                    <p><a href="{{ publication.file.url }}" download>Download File</a></p>
                {% endif %}
                <p>Posted on: {{ publication.date_posted|date:"F j, Y" }}</p>
            </li>
        {% empty %}
            <li>No publications available at this time.</li>
        {% endfor %}
    </ul>
</section>

{% endblock %}