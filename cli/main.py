import click
import yaml
import os

@click.command()
@click.option('--domain', prompt='Domain')
@click.option('--type', prompt='Site type (shop/blog)')
@click.option('--email', prompt='Admin email')

def create(domain, type, email):

  
    profile_path = f"profile/{type}/profile.yaml"

    if not os.path.exists(profile_path):
        print("❌ profile not found")
        return

    with open(profile_path) as f:
        profile = yaml.safe_load(f)

    config = {
        "site": {
            "domain": domain,
            "type": type
        },
        "wordpress": {
            "admin": {
                "email": email
            },
            "theme": profile["wordpress"]["theme"],
            "plugins": profile["wordpress"]["plugins"]
        }
    }

    site_name = domain.replace(".", "-")
    os.makedirs(f"sites/{site_name}", exist_ok=True)

    with open(f"sites/{site_name}/values.yaml", "w") as f:
        yaml.dump(config, f)

    print(f"Site config created: sites/{site_name}/values.yaml")


if __name__ == "__main__":
    create()