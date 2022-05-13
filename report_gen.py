# License information
# Jinja2 - BSD

import jinja2
from datetime import date



def render_html(name, values):
    """
    Render html page using jinja
    """
    template_loader = jinja2.FileSystemLoader(searchpath="./report/template/")
    template_env = jinja2.Environment(loader=template_loader)
    template_file = "template.html"
    template = template_env.get_template(template_file)
    output_text = template.render(
        date=date.today(),
        filename=name,
        image=f"img/{name}.png",
        step_from=values["from"],
        step_to=values["to"],
        gain=values["gain"],
        resp =values["resp"],
        kp_value=f'{values["kp"]:.2f}',
        ti_value=values["ti"],
        theta=values["theta"],
        tau=values["tau"],
        max=values["max"],
        sixthree=values["63%val"],

        )

    html_path = f'./report/{name}.html'
    html_file = open(html_path, 'w')
    html_file.write(output_text)
    html_file.close()



if __name__ == "__main__":
    render_html("test")


