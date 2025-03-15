import data_fetcher

def serialize_animal(animal):
    """Transforms each animal object in HTML-tags."""
    output = '<li class="cards__item">'

    output += f"<div class='card__title'>{animal['name']}</div><br/>\n"

    scientific_name = animal.get("taxonomy", {}).get("scientific_name")
    if scientific_name:
        output += f"<div class='card__subtitle'>{scientific_name.upper()}</div>\n"

    output += '<div class="card__text">'
    output += '<ul>'
    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        output += f"<li><strong>Diet:</strong> {characteristics['diet']}</li>\n"
    if "prey" in characteristics:
        output += f"<li><strong>Prey:</strong> {characteristics['prey']}</li>\n"
    if "predators" in characteristics:
        output += f"<li><strong>Predators:</strong> {characteristics['predators']}</li>\n"
    if "type" in characteristics:
        output += f"<li><strong>Type:</strong> {characteristics['type']}</li>\n"
    locations = animal.get("locations", [])
    if locations:
        output += f"<li><strong>Location:</strong> {locations[0]}</li>\n"

    output += "</ul></div></li>"

    return output


def print_animals_info(animals):
    """Creates the full HTML list for the animals."""
    output = ''
    for animal in animals:
        output += serialize_animal(animal)
    return output


def read_html_template(file_path):
    """Reads the HTML template with the placeholder."""
    with open(file_path, "r", encoding="utf-8") as template:
        return template.read()


def create_animals_html(template, output_path, animals_info):
    """Replaces the placeholder in the template with the generated HTML string."""
    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    with open(output_path, "w", encoding="utf-8") as animals_html_file:
        animals_html_file.write(new_html)
        print("Animals_HTML file was generated successfully!")


def main():
    """Coordinates the all over process of getting data and generating the final
    HTML Page for the browser."""
    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    if not animals_data:
        print("Sorry, there are no animals to find today!")
        error_message = \
            (f"<h2>🙀 OH NO!🙀</h2>"
             f"<h3>The animal <b>'{animal_name}'</b> doesn't exist in database.</h3>"
             f"<h3>Please try again! </h3>"
             )
        template = read_html_template("animals_template.html")
        create_animals_html(template, "animals.html", error_message)
        return
    animals_info = print_animals_info(animals_data)
    template = read_html_template("animals_template.html")
    create_animals_html(template, "animals.html", animals_info)


if __name__ == "__main__":
    main()
